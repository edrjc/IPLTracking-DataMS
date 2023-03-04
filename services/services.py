import requests

from config import vehicle_ms_url, telemetry_profile_ms_url
from models.entities import Data, TelemetryData, GeoData
from models.repositories import BaseRepository, DataRepository, TelemetryDataRepository, GeoDataRepository
from typing import List, Type


class BaseService:

    repository: BaseRepository = NotImplementedError
    entity: Type = NotImplementedError

    def fetch_by_id(self, entity_id) -> entity:
        return self.repository.fetch_by_id(entity_id)

    def fetch_all(self) -> List[entity]:
        return self.repository.fetch_all()

    def save(self, entity) -> entity:
        return self.repository.create(entity)

    def update(self, entity) -> entity:
        return self.repository.update(entity)

    def delete(self, entity_id) -> None:
        self.repository.delete(entity_id)

    @staticmethod
    def has_vehicle(vehicle_id) -> bool:
        url = vehicle_ms_url.format(vehicle_id)
        return requests.get(url).status_code == 200


class DataService (BaseService):

    def __init__(self):
        self.repository = DataRepository()
        self.entity = Data


class TelemetryDataService (BaseService):

    def __init__(self):
        self.repository = TelemetryDataRepository()
        self.entity = TelemetryData

    @staticmethod
    def is_valid_telemetry(vehicle_id, sensor_type, value) -> bool:
        vehicle_url = vehicle_ms_url.format(vehicle_id)
        vehicle_response = requests.get(vehicle_url)
        if vehicle_response.status_code != 200:
            return False
        vehicle_json_response = vehicle_response.json()
        telemetry_profile_id = vehicle_json_response['telemetryProfileId']
        telemetry_data_url = telemetry_profile_ms_url.format(telemetry_profile_id)
        telemetry_data_response = requests.get(telemetry_data_url)
        if telemetry_data_response.status_code != 200:
            return False
        telemetry_data_response_json_response = telemetry_data_response.json()
        for sensor in telemetry_data_response_json_response['sensors']:
            if sensor['sensor_type'] == sensor_type:
                if sensor['minValue'] <= value <= sensor['maxValue']:
                    return True
        return False


class GeoDataService(BaseService):

    def __init__(self):
        self.repository = GeoDataRepository()
        self.entity = GeoData
