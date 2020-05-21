# coding: utf-8
# (C) Copyright IBM Corp. 2020.

"""
Sample Zone Rate Limits
"""
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.zone_rate_limits_v1 import ZoneRateLimitsV1


class ZoneRateLimitsV1Sample:
    """ Sample Zone Rate Limits Class """

    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.rate_limit = ZoneRateLimitsV1.new_instance(
            service_name="cis_services")
        self.rate_limit.set_service_url(self.endpoint)

    def create_zone_rate_limits(self):
        threshold = 40
        period = 2
        action = {
            "mode": "simulate",
            "timeout": 60,
            "response": {
                    "content_type": "text/plain",
                    "body": "This request has been rate-limited."
            }
        }
        correlate = {
            "by": "nat"
        }
        match = {
            "request": {
                "methods": [
                    "_ALL_"
                ],
                "schemes": [
                    "_ALL_"
                ],
                "url": "*.example.org/path*"
            }
        }

        bypass = [
            {
                "name": "url",
                "value": "api.example.com/*"
            }
        ]
        resp = self.rate_limit.create_zone_rate_limits(
            crn=self.crn, zone_identifier=self.zone_id, threshold=threshold, period=period, action=action, match=match, bypass=bypass, correlate=correlate)
        print(resp)
