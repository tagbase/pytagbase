# coding: utf-8

"""
    tagbase-server API

    tagbse-server provides HTTP endpoints for ingestion of various files \\ into a Tagbase SQL database. Input file support currently includes eTUFF (see [here](https://doi.org/10.6084/m9.figshare.10032848.v4) \\ and [here](https://doi.org/10.6084/m9.figshare.10159820.v1)). The REST API complies with [OpenAPI v3.0.3](https://spec.openapis.org/oas/v3.0.3.html). 

    The version of the OpenAPI document: v0.14.0
    Contact: tagtuna@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from pytagbase.models.ingest200 import Ingest200  # noqa: E501

class TestIngest200(unittest.TestCase):
    """Ingest200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Ingest200:
        """Test Ingest200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Ingest200`
        """
        model = Ingest200()  # noqa: E501
        if include_optional:
            return Ingest200(
                code = '200',
                elapsed = '',
                message = 'Data file eTUFF-sailfish-117259.txt successfully ingested into Tagbase DB.'
            )
        else:
            return Ingest200(
        )
        """

    def testIngest200(self):
        """Test Ingest200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
