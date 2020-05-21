# coding: utf-8
# (C) Copyright IBM Corp. 2020.

"""
Sample code to execute Page rule api sdk
"""

import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.page_rule_api_v1 import PageRuleApiV1


class PageRuleV1Sample:
    """ Sample function to call page rule sdk functions """

    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.rule = PageRuleApiV1.new_instance(service_name="cis_services")
        self.rule.set_service_url(self.endpoint)

    def create_page_rule(self):
        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": os.getenv("URL_MATCH")
                }
            }
        ]
        action = [
            {
                "id": "disable_security"
            },
            {
                "id": "browser_check",
                "value": "off"
            }
        ]
        resp = self.rule.create_page_rule(crn=self.crn, zone_id=self.zone_id, targets=target, actions=action,
                                          priority=1, status="active")
        print(resp)

    def change_page_rule(self):
        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": os.getenv("CHANGE_URL_MATCH")
                }
            }
        ]
        action = [
            {
                "id": "disable_security"
            },
            {
                "id": "browser_check",
                "value": "on"
            }
        ]
        rule_id = "fb81fa8bd84fb28e16e03edc8b9efe42"
        resp = self.rule.change_page_rule(crn=self.crn, zone_id=self.zone_id, rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        print(resp)

    def update_page_rule(self):
        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": os.getenv("URL_MATCH")
                }
            }
        ]
        action = [
            {
                "id": "browser_check",
                "value": "off"
            }
        ]
        rule_id = "fb81fa8bd84fb28e16e03edc8b9efe42"
        resp = self.rule.update_page_rule(crn=self.crn, zone_id=self.zone_id, rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        print(resp)
        print(resp.get_result().get('result')[
              'targets'][0].get('constraint').get('value'))

    def list_page_rules(self):
        resp = self.rule.list_page_rules(crn=self.crn, zone_id=self.zone_id)
        print(resp)