# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_geo_data_request import CreateGeoDataRequest  # noqa: E501
from swagger_server.models.create_geo_data_response import CreateGeoDataResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.get_geo_data_response import GetGeoDataResponse  # noqa: E501
from swagger_server.models.list_geo_data_response import ListGeoDataResponse  # noqa: E501
from swagger_server.models.update_geo_data_request import UpdateGeoDataRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGeoDataController(BaseTestCase):
    """GeoDataController integration test stubs"""

    def test_create_geo_data(self):
        """Test case for create_geo_data

        Create new Geo Data
        """
        body = CreateGeoDataRequest()
        response = self.client.open(
            '/tracking/GeoData',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_geo_data(self):
        """Test case for delete_geo_data

        Delete Geo Data
        """
        response = self.client.open(
            '/tracking/GeoData/{dataId}'.format(data_id='data_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_geo_data(self):
        """Test case for get_geo_data

        Get a single Geo Data's info
        """
        response = self.client.open(
            '/tracking/GeoData/{dataId}'.format(data_id='data_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_geo_data(self):
        """Test case for list_geo_data

        Get Geo Data list
        """
        response = self.client.open(
            '/tracking/GeoData',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_geo_data(self):
        """Test case for update_geo_data

        Update Geo Data's attributes
        """
        body = UpdateGeoDataRequest()
        response = self.client.open(
            '/tracking/GeoData/{dataId}'.format(data_id='data_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
