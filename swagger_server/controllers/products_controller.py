import connexion
import six

from swagger_server.models.array_of_products import ArrayOfProducts  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def get_products():  # noqa: E501
    """Get all products

     # noqa: E501


    :rtype: ArrayOfProducts
    """
    return 'do some magic!'


def update_product(productId, body):  # noqa: E501
    """Updates a product in the store with form data

     # noqa: E501

    :param productId: ID of productId to update
    :type productId: int
    :param body: Product object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
