# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_comedy_shows_get(self):
        """Test case for comedy_shows_get

        List comedy shows
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/comedy-shows',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
