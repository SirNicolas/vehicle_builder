import aiopg.sa
from app.config import settings


async def init_pg(app):
    engine = await aiopg.sa.create_engine(dsn=settings.DATABASE_DSN)
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
