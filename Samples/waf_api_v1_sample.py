# coding: utf-8
# Copyright 2020 IBM All Rights Reserved.

"""
Sample code to execute waf api
"""

import os
import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.waf_api_v1 import WafApiV1


class WafApiV1Sample:
    """ Sample function to call waf api sdk functions """

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
        self.waf = WafApiV1(authenticator=self.authenticator)
        self.waf.set_service_url(self.endpoint)

    def get_waf_settings(self):
        """ this method get security level settings """
        response = self.waf.get_waf_settings(
            crn=self.crn, zone_id=self.zone_id)
        print(response.get_result().get("result")["value"])

    def update_waf_settings(self):
        """ this method set security level setting to essentially_off/low/medium/high/under_attack """
        resp = self.waf.update_waf_settings(
            crn=self.crn, zone_id=self.zone_id, value="off")
        print(resp)
