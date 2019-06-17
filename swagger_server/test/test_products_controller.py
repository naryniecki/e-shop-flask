# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.array_of_products import ArrayOfProducts  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_get_products(self):
        """Test case for get_products

        Get all products
        """
        response = self.client.open(
            '/v1/products',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product(self):
        """Test case for update_product

        Updates a product in the store with form data
        """
        body = Product()
        response = self.client.open(
            '/v1/products/{productId}'.format(productId=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
