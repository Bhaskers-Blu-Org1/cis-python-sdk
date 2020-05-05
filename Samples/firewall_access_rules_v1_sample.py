# coding: utf-8
# (C) Copyright IBM Corp. 2020.

"""
Instance Level Firewall Access Rules Sample code
"""

import os
import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.firewall_access_rules_v1 import FirewallAccessRulesV1


class FirewallAccessRulesV1Sample:
    """ Sample function to call firewall access rule sdk functions """

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
        self.rule = FirewallAccessRulesV1(authenticator=self.authenticator)
        self.rule.set_service_url(self.endpoint)

    def create_account_access_rule(self):
        mode = "block"
        notes = "This rule is added because of event X that occurred on date xyz"
        configuration = {
            "target": "ip",
            "value": "192.168.1.45"
        }
        resp = self.rule.create_account_access_rule(crn=self.crn, mode=mode, notes=notes,
                                                    configuration=configuration)
        print(resp.get_result().get("result")["id"])

    def delete_account_access_rule(self):
        resp = self.rule.delete_account_access_rule(crn=self.crn,
                                                    accessrule_identifier="db5def80b1d94386b3c79f195d80fa3d")
        print(resp)

    def update_account_access_rule(self):
        mode = "challenge"
        notes = "This rule is updated because of event X that occurred on date xyz"
        resp = self.rule.update_account_access_rule(crn=self.crn,
                                                    mode=mode, notes=notes, accessrule_identifier="e568e15d88b8448ba8a6ccbdb9a3d350")
        print(resp)

    def get_account_access_rule(self):
        resp = self.rule.get_account_access_rule(crn=self.crn,
                                                 accessrule_identifier="e568e15d88b8448ba8a6ccbdb9a3d350")
        print(resp)

    def list_all_account_access_rules(self):
        resp = self.rule.list_all_account_access_rules(crn=self.crn)
        print(resp)
