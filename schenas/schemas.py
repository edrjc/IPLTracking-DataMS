from flask_marshmallow.fields import fields

from config import ma
from models.entities import TelemetryData, GeoData


class TelemetryDataSchema(ma.SQLAlchemyAutoSchema):
    dataId = fields.String(attribute="data_id")
    vehicleId = fields.String(attribute="vehicle_id")

    class Meta:
        model = TelemetryData
        load_instance = True
        exclude = ["data_id", "vehicle_id"]


class GeoDataSchema(ma.SQLAlchemyAutoSchema):
    dataId = fields.String(attribute="data_id")
    vehicleId = fields.String(attribute="vehicle_id")

    class Meta:
        model = GeoData
        load_instance = True
        exclude = ["data_id", "vehicle_id"]
