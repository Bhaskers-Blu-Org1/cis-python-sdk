# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for Range analytics summary
"""

import os
import unittest
from cis_services.range_analytics_summary_v1 import RangeAnalyticsSummaryV1


class TestRangeAnalyticsSummaryApiV1(unittest.TestCase):
    """ Range Analytics Summary API test class """

    def setUp(self):
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.url = os.getenv("URL")
        self.rapp = RangeAnalyticsSummaryV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.rapp.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_get_range_analytics_summary(self):
        resp = self.rapp.get_range_analytics_summary()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True


if __name__ == '__main__':
    unittest.main()
