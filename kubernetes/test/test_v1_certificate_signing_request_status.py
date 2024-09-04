# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.31
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.models.v1_certificate_signing_request_status import V1CertificateSigningRequestStatus

class TestV1CertificateSigningRequestStatus(unittest.TestCase):
    """V1CertificateSigningRequestStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CertificateSigningRequestStatus:
        """Test V1CertificateSigningRequestStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CertificateSigningRequestStatus`
        """
        model = V1CertificateSigningRequestStatus()
        if include_optional:
            return V1CertificateSigningRequestStatus(
                certificate = 'YQ==',
                conditions = [
                    kubernetes.client.models.v1/certificate_signing_request_condition.v1.CertificateSigningRequestCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', 
                        status = '', 
                        type = '', )
                    ]
            )
        else:
            return V1CertificateSigningRequestStatus(
        )
        """

    def testV1CertificateSigningRequestStatus(self):
        """Test V1CertificateSigningRequestStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
