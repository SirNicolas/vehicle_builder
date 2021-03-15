from aiohttp import web
from app.common import models
from app.common.exceptions import RecordNotFound


async def get_vehicles(request):
    async with request.app['db'].acquire() as conn:
        vehicles = await models.get_vehicles(conn)
        vehicles = [dict(q) for q in vehicles]
        return web.json_response({'vehicles': vehicles})


async def get_vehicle(request):
    async with request.app['db'].acquire() as conn:
        vehicle_id = int(request.match_info['vehicle_id'])
        try:
            vehicle = await models.get_vehicle(conn, vehicle_id)
        except RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        return web.json_response(dict(vehicle))
