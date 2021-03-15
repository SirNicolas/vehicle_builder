from typing import List
from sqlalchemy import (
    MetaData, Table, Column, Integer, String,
)

from app.common.exceptions import RecordNotFound

meta = MetaData()

Vehicle = Table(
    'vehicle', meta,

    Column('id', Integer, primary_key=True),
    Column('title', String(200), nullable=False),
    Column('weight', Integer, nullable=False),
    Column('range', Integer, nullable=False),
)


async def get_vehicle(conn, vehicle_id: int) -> Vehicle:
    result = await conn.execute(
        Vehicle.select()
        .where(Vehicle.c.id == vehicle_id)
    )
    vehicle_record = await result.first()
    if not vehicle_record:
        msg = "Vehicle with id: {} does not exists"
        raise RecordNotFound(msg.format(vehicle_id))
    return vehicle_record


async def get_vehicles(conn):
    cursor = await conn.execute(Vehicle.select())
    vehicles = await cursor.fetchall()
    return vehicles
