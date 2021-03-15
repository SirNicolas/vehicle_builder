import logging

from aiohttp import web

from app.db import init_pg, close_pg
from app.routes import setup_routes
from app.config import settings
from app.middlewares import setup_middlewares


async def init_app():
    app = web.Application()

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_routes(app)
    setup_middlewares(app)

    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    web.run_app(app, host=settings.HOST, port=int(settings.PORT))


if __name__ == '__main__':
    main()
