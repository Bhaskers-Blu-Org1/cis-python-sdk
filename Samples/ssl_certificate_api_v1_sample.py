# coding: utf-8
# Copyright 2020 IBM All Rights Reserved.

"""
Sample code to execute ssl certificate client functions
"""

import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.ssl_certificate_api_v1 import SslCertificateApiV1


class SSLCertV1Sample:
    """ Sample function to call ssl certificate client functions """

    def __init__(self):
        load_dotenv()
        self.token = os.getenv("TOKEN")
        self.apikey = os.getenv("APIKEY")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.iam_endpoint = os.getenv("IAM_ENDPOINT")
        self.authenticator = IAMAuthenticator(
            apikey=self.apikey, url=self.iam_endpoint)
        self.ssl = SslCertificateApiV1(authenticator=self.authenticator)
        self.ssl.set_service_url(self.endpoint)

    def list_certificates(self):
        """ this method list all ssl certificate packs """
        resp = self.ssl.list_certificates(x_auth_user_token=self.token,
                                          crn=self.crn, zone_identifier=self.zone_id)
        print(resp)

    def order_certificate(self):
        """ this method order ssl certificate packs """
        resp = self.ssl.order_certificate(
            crn=self.crn, zone_identifier=self.zone_id,
            x_correlation_id="1234", type="dedicated", hosts=["sdk.cistest-load.com"])
        print(resp)

    def delete_certificate(self):
        """ this method delete ssl certificate packs """
        resp = self.ssl.delete_certificate(
            crn=self.crn, zone_identifier=self.zone_id,
            cert_identifier="")
        print(resp)

    def get_ssl_setting(self):
        """ this method get ssl certificate settings """
        resp = self.ssl.get_ssl_setting(
            crn=self.crn, zone_identifier=self.zone_id)
        print(resp)

    def change_ssl_setting(self):
        """ this method change ssl certificate settings """
        resp = self.ssl.change_ssl_setting(
            crn=self.crn, zone_identifier=self.zone_id,
            value="strict")
        print(resp)

    def list_custom_certificates(self):
        """ this method list custom ssl certificate settings """
        resp = self.ssl.list_custom_certificates(
            crn=self.crn, zone_identifier=self.zone_id)
        print(resp)

    def upload_custom_certificate(self):
        """ this method upload given customized ssl certificate """
        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model = {
            'label': 'us'
        }
        resp = self.ssl.upload_custom_certificate(
            crn=self.crn, zone_identifier=self.zone_id,
            certificate=os.getenv("CERTIFICATE"),
            private_key=os.getenv("PRIVATE_KEY"),
            geo_restrictions=custom_cert_req_geo_restrictions_model)
        print(resp.get_result().get("result")["id"])

    def get_universal_certificate_setting(self):
        """ this method list custom ssl certificate settings """
        cert_id = "6898d249785e6e5eab1d3700a9da0bf9"
        resp = self.ssl.get_universal_certificate_setting(
            x_auth_user_token=self.token, crn=self.crn, zone_identifier=self.zone_id,
            custom_cert_id=cert_id)
        print(resp)

    def update_custom_certificate(self):
        """ this method upload given customized ssl certificate """
        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model = {
            'label': 'us'
        }
        resp = self.ssl.update_custom_certificate(
            crn=self.crn, zone_identifier=self.zone_id,
            certificate=os.getenv("UPDATE_CERTIFICATE"),
            private_key=os.getenv("UPDATE_PRIVATE_KEY"),
            bundle_method="optimal", custom_cert_id="6898d249785e6e5eab1d3700a9da0bf9",
            geo_restrictions=custom_cert_req_geo_restrictions_model)
        print(resp)

    def change_certificate_priority(self):
        cert_id = "6898d249785e6e5eab1d3700a9da0bf9"
        cust_cert_priority = {
            "id": cert_id,
            "priority": 4}
        resp = self.ssl.change_certificate_priority(
            crn=self.crn, zone_identifier=self.zone_id,
            custom_cert_id=cert_id, certificates=[cust_cert_priority])
        print(resp)

    def change_tl_s12_setting(self):
        resp = self.ssl.change_tls12_setting(
            crn=self.crn, zone_identifier=self.zone_id,
            value="on")
        print(resp)
