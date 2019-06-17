# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.array_of_orders import ArrayOfOrders  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_delete_order(self):
        """Test case for delete_order

        Delete purchase order by ID
        """
        response = self.client.open(
            '/v1/orders/{orderId}'.format(orderId=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_orders(self):
        """Test case for get_orders

        Get all orders
        """
        response = self.client.open(
            '/v1/orders',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_place_order(self):
        """Test case for place_order

        Place an order for a product
        """
        body = Order()
        response = self.client.open(
            '/v1/orders',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
