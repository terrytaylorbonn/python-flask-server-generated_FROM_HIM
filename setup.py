# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Products API TT 24.1211",
    author_email="",
    url="",
    keywords=["Swagger", "Products API TT 24.1211"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This a sample specification part of a YT tutorial showcasing how to design a RESTful API contract using OpenAPI.  We are going to create an API to manage products with the the following operations: * List all Products * Create a Product * Get Product details * Update Product * Delete Product  We will cover also the following topics: * Result pagination * Security (Auth&#x27;n / Auth&#x27;z)  We will use a simple **Product** resource representation with the following properties: * ID * Name * Price * Description (optional) * Last updated date-time 
    """
)
