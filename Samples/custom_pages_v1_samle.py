# coding: utf-8
# Copyright 2020 IBM All Rights Reserved.

"""
Sample code to execute custom pages setting
"""

import os
import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.custom_pages_v1 import CustomPagesV1


class CustomPagesV1Sample:
    """ Sample function to call custom pages sdk functions """

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
        self.cu = CustomPagesV1(authenticator=self.authenticator)
        self.cu.set_service_url(self.endpoint)

    def update_zone_custom_page_settings(self):
        """ this method set zone custom page setting to essentially_off/low/medium/high/under_attack """
        url = "https://beta.sdk.cistest-load.com/index.html"
        resp = self.cu.update_zone_custom_page(crn=self.crn,
                                               zone_identifier=self.zone_id, page_identifier="basic_challenge", url=url, state="customized")
        print(resp)

    def update_zone_custom_page_settings_default(self):
        """ this method set zone custom page setting to essentially_off/low/medium/high/under_attack """
        page_ids = ["basic_challenge"]
        state = ["default", "customized"]
        for page_id in page_ids:
            resp = self.cu.update_zone_custom_page(crn=self.crn,
                                                   zone_identifier=self.zone_id, page_identifier=page_id, url="", state=state[0])
            print(resp)

    def list_zone_custom_page(self):
        resp = self.cu.list_zone_custom_pages(
            crn=self.crn, zone_identifier=self.zone_id)
        print(resp)

    def list_instance_custom_page(self):
        resp = self.cu.list_instance_custom_pages(crn=self.crn)
        print(resp)
