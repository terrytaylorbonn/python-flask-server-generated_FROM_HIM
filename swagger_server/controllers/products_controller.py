from datetime import datetime
import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def create_product(body=None):  # noqa: E501
    """Create a product

    Use this endpoint to add a new product to the catalog # noqa: E501

    :param body: Product Details
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

def delete_product(id):  # noqa: E501
    """Delete product

    Use this endpoint to remove a product from the catalog # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic! delete_product'


def get_all_products(offset=None, limit=None):  # noqa: E501
    """List products

    Use this endpoint to browse all products in the catalog # noqa: E501

    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    :rtype: InlineResponse200
    """
    aaa1 = Product(1111,"aaa2", 11.11, "aaa3", datetime.now())
    bbb1 = Product("2222","bbb2", 22.22, "bbb3", datetime.now())
    return [aaa1, bbb1]

#    return 'do some magic get_all_products!'


def get_product(id):  # noqa: E501
    """Get product details

    Use this endpoint to get details about a specific product # noqa: E501

    :param id: 
    :type id: str

    :rtype: Product
    """
    return 'do some magic (GET get_product)!'



def update_product(id, body=None):  # noqa: E501
    """Update product&#x27;s details

    Use this endpoint to update the product&#x27;s details # noqa: E501

    :param id: 
    :type id: str
    :param body: Product Details
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic! update_product'
