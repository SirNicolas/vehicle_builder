"""Add vehicles

Revision ID: d22917c40868
Revises: 165b7dbfa7f5
Create Date: 2021-03-15 21:24:17.858890

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# revision identifiers, used by Alembic.
revision = 'd22917c40868'
down_revision = '165b7dbfa7f5'
branch_labels = None
depends_on = None


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    weight = sa.Column(sa.Integer, nullable=False)
    range = sa.Column(sa.Integer, nullable=False)


def upgrade():
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    vehicles = [Vehicle(title='Tesla Model 3', weight=2000, range=500),
                Vehicle(title='Tesla Model s', weight=1500, range=600)]
    for vehicle in vehicles:
        session.add(vehicle)
    session.commit()


def downgrade():
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    session.query(Vehicle).delete()
    session.commit()
