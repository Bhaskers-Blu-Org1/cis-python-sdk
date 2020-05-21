# coding: utf-8
# Copyright 2019 IBM All Rights Reserved.

"""
Sample code to execute caching api
"""

import os
import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.caching_api_v1 import CachingApiV1


class CachingApiV1Sample:
    """ Sample function to call caching api sdk functions """

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
        self.cache = CachingApiV1(authenticator=self.authenticator)
        self.cache.set_service_url(self.endpoint)

    def get_cache_level(self):
        """ this method get cache level settings """
        response = self.cache.get_cache_level(
            crn=self.crn, zone_id=self.zone_id)
        print(response.get_result().get("result")["value"])

    def update_cache_level(self):
        """ this method set cache level setting to basic/simplified/aggressive """
        resp = self.cache.update_cache_level(
            crn=self.crn, zone_id=self.zone_id, value="aggressive")
        print(resp)

    def get_browser_cache_ttl(self):
        """ This method get browser cache ttl value """
        resp = self.cache.get_browser_cache_ttl(
            crn=self.crn, zone_id=self.zone_id)
        print(resp)

    def update_browser_cache_ttl(self):
        """ This method update browser cache ttl value """
        resp = self.cache.get_browser_cache_ttl(
            crn=self.crn, zone_id=self.zone_id, value=14000)
        print(resp)
