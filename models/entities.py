from sqlalchemy.orm import relationship

from config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Data(db.Model):
    """Data table"""
    data_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehicle_id = db.Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    time = db.Column(db.DateTime(32), nullable=False)
    data_type = db.Column(db.String(32), nullable=False)

    __mapper_args__ = {'polymorphic_on': data_type}

    def get_id(self):
        return self.data_id

    def __init__(self, data_id, vehicle_id, time):
        self.data_id = data_id
        self.vehicle_id = vehicle_id
        self.time = time

    def __repr__(self):
        return 'Data(data_id=%d)' % (
            self.data_id)

    '''def json(self):
        return {'customer_id': str(self.customer_id), 'name': self.name, 'phone': self.phone, 'mail': self.mail}'''


class TelemetryData(Data):
    __tablename__ = 'telemetry_data'
    data_id = db.Column(UUID(as_uuid=True), db.ForeignKey('data.data_id'), primary_key=True)
    sensor_type = db.Column(db.String(32), nullable=False)
    value = db.Column(db.Numeric, nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'telemetry_data'}

    def get_id(self):
        return self.data_id

    def __init__(self, data_id, vehicle_id, time, sensor_type, value):
        super().__init__(data_id, vehicle_id, time)
        self.sensor_type = sensor_type
        self.value = value

    def __repr__(self):
        return 'Data(data_id=%d)' % (
            self.data_id)

    '''def json(self):
        return {'customer_id': str(self.customer_id), 'name': self.name, 'phone': self.phone, 'mail': self.mail}'''


class GeoData(Data):
    __tablename__ = 'geo_data'
    data_id = db.Column(UUID(as_uuid=True), db.ForeignKey('data.data_id'), primary_key=True)
    latitude = db.Column(db.String(32), nullable=False)
    longitude = db.Column(db.String(32), nullable=False)
    altimeter = db.Column(db.String(32), nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'geo_data'}

    def get_id(self):
        return self.data_id

    def __init__(self, data_id, vehicle_id, time, latitude, longitude, altimeter):
        super().__init__(data_id, vehicle_id, time)
        self.latitude = latitude
        self.longitude = longitude
        self.altimeter = altimeter

    def __repr__(self):
        return 'Data(data_id=%d)' % (
            self.data_id)

    '''def json(self):
        return {'customer_id': str(self.customer_id), 'name': self.name, 'phone': self.phone, 'mail': self.mail}'''