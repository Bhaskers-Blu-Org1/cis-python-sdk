# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for Routing
"""

import os
import unittest
from cis_services.routing_v1 import RoutingV1


class TestRoutingApiV1(unittest.TestCase):
    """ Routing API test class """

    def setUp(self):
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.route = RoutingV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.route.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_routing_smart_routing(self):
        value = "on"
        resp = self.route.update_routing_smart_routing(value=value)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "smart_routing"
        assert resp.get_result().get("result")["value"] == value

        resp = self.route.get_routing_smart_routing()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "smart_routing"
        assert resp.get_result().get("result")["value"] == value

        value = "off"
        resp = self.route.update_routing_smart_routing(value=value)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "smart_routing"
        assert resp.get_result().get("result")["value"] == value

    def test_1_routing_tiered_caching(self):
        value = "on"
        resp = self.route.update_routing_tiered_caching(value=value)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "tiered_caching"
        assert resp.get_result().get("result")["value"] == value

        resp = self.route.get_routing_tiered_caching()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "tiered_caching"
        assert resp.get_result().get("result")["value"] == value

        value = "off"
        resp = self.route.update_routing_tiered_caching(value=value)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "tiered_caching"
        assert resp.get_result().get("result")["value"] == value

    def test_1_get_routing_latency(self):
        resp = self.route.get_routing_latency()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True

    def test_1_get_routing_latency_colos(self):
        resp = self.route.get_routing_latency_colos()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True


if __name__ == '__main__':
    unittest.main()
