import requests

from config import vehicle_ms_url
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


class GeoDataService(BaseService):

    def __init__(self):
        self.repository = GeoDataRepository()
        self.entity = GeoData
