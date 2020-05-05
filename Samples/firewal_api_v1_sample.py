# coding: utf-8
# Copyright 2020 IBM All Rights Reserved.

"""
Sample code to execute firewall api
"""

import os
import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.firewall_api_v1 import FirewallApiV1


class FirewallApiV1Sample:
    """ Sample function to call firewall api"""

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
        self.firewall = FirewallApiV1(authenticator=self.authenticator)
        self.firewall.set_service_url(self.endpoint)

    def get_security_level_setting(self):
        """ this method get security level settings """
        response = self.firewall.get_security_level_setting(
            crn=self.crn,
            zone_identifier=self.zone_id)
        print(response)

    def set_security_level_setting(self):
        """ this method set security level setting to essentially_off/low/medium/high/under_attack """
        resp = self.firewall.set_security_level_setting(
            crn=self.crn, zone_identifier=self.zone_id, value="medium")
        print(resp)
