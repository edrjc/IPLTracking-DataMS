import datetime

import connexion
import json

from models.entities import GeoData
from schenas.schemas import GeoDataSchema
from services.services import GeoDataService
from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError

from swagger_server.models.create_geo_data_request import CreateGeoDataRequest  # noqa: E501
from swagger_server.models.create_geo_data_response import CreateGeoDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from swagger_server.models.get_geo_data_response import GetGeoDataResponse  # noqa: E501
from swagger_server.models.list_geo_data_response import ListGeoDataResponse  # noqa: E501
from swagger_server.models.update_geo_data_request import UpdateGeoDataRequest  # noqa: E501

geo_data_service = GeoDataService()
geo_data_schema = GeoDataSchema()


def create_geo_data(body):  # noqa: E501
    """Create new Geo Data

    This operation is usedto create a new Geo Data on System. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateGeoDataResponse
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateGeoDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        if not GeoDataService.has_vehicle(body.vehicle_id):
            raise EntityNotFound(code="", message='Vehicle Not Found', details='It is not possible to add Data to a non'
                                                                               'existing vehicle')
        entity = GeoData(
            data_id=None,
            vehicle_id=body.vehicle_id,
            time=datetime.datetime.now(),
            latitude=body.latitude,
            longitude=body.longitude,
            altimeter=body.altimeter
        )
        entity = geo_data_service.save(entity)
        response = CreateGeoDataResponse.from_dict(json.loads(geo_data_schema.dumps(entity)))
        response_code = 201

    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CST0002", type=ErrorTypeEnum.PERSISTENCE,
                                 message="Error on create new Customer", details=str(e))

    return response.to_dict(), response_code


def delete_geo_data(data_id):  # noqa: E501
    """Delete Geo Data

    This operation is delete a Geo Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        entity = geo_data_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Geo Data not found",
                                 details=f"Unable to find Geo Data ID {data_id}")
        geo_data_service.delete(data_id)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code


def get_geo_data(data_id):  # noqa: E501
    """Get a single Geo Data&#x27;s info

    This operation is used to retrieve the details of a specific Geo Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: GetGeoDataResponse
    """
    response = None
    response_code = None
    try:
        entity = geo_data_service.fetch_by_id(entity_id=data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Data not found",
                                 details=f"Unable to find data ID {data_id}")
        response = GetGeoDataResponse.from_dict(json.loads(geo_data_schema.dumps(entity)))
        response_code = 200
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))
    return response.to_dict(), response_code


def list_geo_data():  # noqa: E501
    """Get Geo Data list

    This operation is used to retrieve a list of Geo Data. # noqa: E501


    :rtype: ListGeoDataResponse
    """
    entities = geo_data_service.fetch_all()

    response_list = []
    for entity in entities:
        response_list.append(GetGeoDataResponse.from_dict(json.loads(geo_data_schema.dumps(entity))))

    response = ListGeoDataResponse(content=response_list, total_results=len(response_list))
    return response.to_dict(), 200


def update_geo_data(body, data_id):  # noqa: E501
    """Update Geo Data&#x27;s attributes

    This operation is used to update some of the Geo Data&#x27;s attributes. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = UpdateGeoDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = geo_data_service.fetch_by_id(data_id)
        if entity is None:
            raise EntityNotFound(code="CST001", message="Geo Data not found",
                                 details=f"Unable to find Geo Data ID {data_id}")
        entity.time = body.time
        entity.latitude = body.latitude
        entity.longitude = body.longitude
        entity.altimeter = body.altimeter
        geo_data_service.save(entity)
        response_code = 204
    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CSM999", type=ErrorTypeEnum.UNKNOWN,
                                 message="Ops.. Unknown error..", details=str(e))

    if response is None:
        return None, response_code
    else:
        return response.to_dict(), response_code
