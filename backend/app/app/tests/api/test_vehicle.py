import pytest


@pytest.mark.asyncio
async def test_get_vehicles(client):
    response = await client.get('/vehicles/')
    assert response.status == 200
    assert {
               'vehicles': [
                   {'id': 1, 'range': 500, 'title': 'Tesla Model 3', 'weight': 2000},
                   {'id': 2, 'range': 600, 'title': 'Tesla Model s', 'weight': 1500},
               ]
           } == await response.json()


@pytest.mark.asyncio
async def test_get_vehicle(client):
    response = await client.get('/vehicles/1')
    assert response.status == 200
    assert {'id': 1, 'range': 500, 'title': 'Tesla Model 3', 'weight': 2000} == await response.json()
