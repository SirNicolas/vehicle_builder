from app.api.api_v1.endpoints import common, vehicles


def setup_routes(app):
    app.router.add_get('/', common.index)
    app.router.add_get('/vehicles/', vehicles.get_vehicles, name='vehicles')
    app.router.add_get('/vehicles/{vehicle_id}', vehicles.get_vehicle, name='vehicle')
