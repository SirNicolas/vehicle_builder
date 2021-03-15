import pytest
from aiohttp import web

from app.routes import setup_routes
from app.db import init_pg, close_pg


@pytest.fixture
def loop(event_loop):
    return event_loop


@pytest.fixture
def app(loop):
    app = web.Application(loop=loop)
    setup_routes(app)
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    return app


@pytest.fixture
async def client(aiohttp_client, app):
    client = await aiohttp_client(app)
    return client
