import connexion
import six

from swagger_server.models.array_of_orders import ArrayOfOrders  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util


def delete_order(orderId):  # noqa: E501
    """Delete purchase order by ID

    For valid response try integer IDs with positive integer value.         Negative or non-integer values will generate API errors # noqa: E501

    :param orderId: ID of the order that needs to be deleted
    :type orderId: int

    :rtype: None
    """
    return 'do some magic!'


def get_orders():  # noqa: E501
    """Get all orders

     # noqa: E501


    :rtype: ArrayOfOrders
    """
    return 'do some magic!'


def place_order(body):  # noqa: E501
    """Place an order for a product

     # noqa: E501

    :param body: order placed for purchasing the product
    :type body: dict | bytes

    :rtype: Order
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
