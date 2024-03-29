# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Product(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, quantity: int=None):  # noqa: E501
        """Product - a model defined in Swagger

        :param id: The id of this Product.  # noqa: E501
        :type id: int
        :param name: The name of this Product.  # noqa: E501
        :type name: str
        :param quantity: The quantity of this Product.  # noqa: E501
        :type quantity: int
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'quantity': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'quantity': 'quantity'
        }

        self._id = id
        self._name = name
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt) -> 'Product':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Product of this Product.  # noqa: E501
        :rtype: Product
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Product.


        :return: The id of this Product.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Product.


        :param id: The id of this Product.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Product.


        :return: The name of this Product.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Product.


        :param name: The name of this Product.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def quantity(self) -> int:
        """Gets the quantity of this Product.


        :return: The quantity of this Product.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this Product.


        :param quantity: The quantity of this Product.
        :type quantity: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity
