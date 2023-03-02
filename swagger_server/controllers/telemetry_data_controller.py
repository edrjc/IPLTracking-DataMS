import datetime

import connexion
import json

from models.entities import TelemetryData
from schenas.schemas import TelemetryDataSchema
from services.services import TelemetryDataService
from custom_errors import EntityNotFound, InvalidPayload, BaseCustomError

from swagger_server.models.create_telemetry_data_request import CreateTelemetryDataRequest
from swagger_server.models.create_telemetry_data_response import CreateTelemetryDataResponse
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from swagger_server.models.get_telemetry_data_response import GetTelemetryDataResponse  # noqa: E501
from swagger_server.models.list_telemetry_data_response import ListTelemetryDataResponse  # noqa: E501
from swagger_server.models.update_telemetry_data_request import UpdateTelemetryDataRequest  # noqa: E501
from swagger_server import util

telemetry_data_service = TelemetryDataService()
telemetry_data_schema = TelemetryDataSchema()


def create_telemetry_data(body):  # noqa: E501
    """Create new Telemetry Data

    This operation is used to create a new Telemetry Data on System. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: CreateTelemetryDataResponse
    """
    response = None
    response_code = None
    try:
        if not connexion.request.is_json:
            raise InvalidPayload(code="CST002", message="Invalid Request Payload",
                                 details=f"Request payload is not a JSON valid")
        body = CreateTelemetryDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
        entity = TelemetryData(
            data_id=None,
            vehicle_id=body.vehicle_id,
            time=datetime.datetime.now(),
            sensor_type=body.sensor_type,
            value=body.value
        )
        entity = telemetry_data_service.save(entity)
        response = CreateTelemetryDataResponse.from_dict(json.loads(telemetry_data_schema.dumps(entity, default=str)))
        response_code = 201

    except BaseCustomError as bce:
        response_code = bce.http_code
        response = bce.to_error_response()
    except Exception as e:
        response_code = 500
        response = ErrorResponse(code="CST0002", type=ErrorTypeEnum.PERSISTENCE,
                                 message="Error on create new Customer", details=str(e))

    return response.to_dict(), response_code


def delete_telemetry_data(data_id):  # noqa: E501
    """Delete Telemetry Data

    This operation is delete a Telemetry Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_telemetry_data(data_id):  # noqa: E501
    """Get a single Telemetry Data&#x27;s info

    This operation is used to retrieve the details of a specific Telemetry Data. # noqa: E501

    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: GetTelemetryDataResponse
    """
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_telemetry_data():  # noqa: E501
    """Get Telemetry Data list

    This operation is used to retrieve a list of Telemetry Data. # noqa: E501


    :rtype: ListTelemetryDataResponse
    """
    entities = telemetry_data_service.fetch_all()

    response_list = []
    for entity in entities:
        response_list.append(GetTelemetryDataResponse.from_dict(json.loads(telemetry_data_schema.dumps(entity, default=str))))

    response = ListTelemetryDataResponse(content=response_list, total_results=len(response_list))
    return response.to_dict(), 200


def update_telemetry_data(body, data_id):  # noqa: E501
    """Update Telemetry Data&#x27;s attributes

    This operation is used to update some of the Telemetry Data&#x27;s attributes. # noqa: E501

    :param body:
    :type body: dict | bytes
    :param data_id: Unique identifier of the Data in the database
    :type data_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateTelemetryDataRequest.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        data_id = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'