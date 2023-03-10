# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class Data(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_id: str=None, vehicle_id: str=None, time: datetime=None):  # noqa: E501
        """Data - a model defined in Swagger

        :param data_id: The data_id of this Data.  # noqa: E501
        :type data_id: str
        :param vehicle_id: The vehicle_id of this Data.  # noqa: E501
        :type vehicle_id: str
        :param time: The time of this Data.  # noqa: E501
        :type time: datetime
        """
        self.swagger_types = {
            'data_id': str,
            'vehicle_id': str,
            'time': datetime
        }

        self.attribute_map = {
            'data_id': 'dataId',
            'vehicle_id': 'vehicleId',
            'time': 'time'
        }
        self._data_id = data_id
        self._vehicle_id = vehicle_id
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'Data':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Data of this Data.  # noqa: E501
        :rtype: Data
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_id(self) -> str:
        """Gets the data_id of this Data.


        :return: The data_id of this Data.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id: str):
        """Sets the data_id of this Data.


        :param data_id: The data_id of this Data.
        :type data_id: str
        """
        if data_id is None:
            raise ValueError("Invalid value for `data_id`, must not be `None`")  # noqa: E501

        self._data_id = data_id

    @property
    def vehicle_id(self) -> str:
        """Gets the vehicle_id of this Data.


        :return: The vehicle_id of this Data.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id: str):
        """Sets the vehicle_id of this Data.


        :param vehicle_id: The vehicle_id of this Data.
        :type vehicle_id: str
        """
        if vehicle_id is None:
            raise ValueError("Invalid value for `vehicle_id`, must not be `None`")  # noqa: E501

        self._vehicle_id = vehicle_id

    @property
    def time(self) -> datetime:
        """Gets the time of this Data.

        Data collection date  # noqa: E501

        :return: The time of this Data.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this Data.

        Data collection date  # noqa: E501

        :param time: The time of this Data.
        :type time: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time
