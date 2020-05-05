# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Advanced Distributed Denial of Service (DDoS) Settings integration test
"""

import os
import unittest
from cis_services.advanced_ddos_settings_v1 import AdvancedDdosSettingsV1


class TestAdvancedDDoSV1(unittest.TestCase):
    """ Advanced DDoS test class """

    def setUp(self):
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.ddos = AdvancedDdosSettingsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.ddos.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_Advanced_ddos_setting(self):
        """ test to get advanced ddos setting """
        resp = self.ddos.get_advanced_ddos_settings()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "advanced_ddos"


if __name__ == '__main__':
    unittest.main()
