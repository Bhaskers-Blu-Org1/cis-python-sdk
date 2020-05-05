# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
"""
Integration test code to execute zones settings functions
"""
import os
import unittest
from cis_services.zones_settings_v1 import ZonesSettingsV1


class TestZonesSettingsV1(unittest.TestCase):
    """ Sample function to call zones sdk functions """

    def setUp(self):
        """ test case setup """
        self.crn = os.getenv("CRN")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.zone_id = os.getenv("ZONE_ID")
        # create zones settings record class object
        self.zonesSettings = ZonesSettingsV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.zonesSettings.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down zone"""
        # Delete the resources
        print("Clean up complete")

    ################## zone settings integration test ###################

    def test_1_zone_settings(self):
        """ get zone dnssec """
        response = self.zonesSettings.get_zone_dnssec().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('status') == 'disabled':
            self.status = 'active'
        else:
            self.status = 'disabled'

        """ update zone dnssec """
        response = self.zonesSettings.update_zone_dnssec(
            status=self.status).get_result()

        """ get zone cname flattening """
        response = self.zonesSettings.get_zone_cname_flattening().get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        if result.get('value') == 'flatten_at_root':
            self.value = 'flatten_all'
        else:
            self.value = 'flatten_at_root'

        """ update zone cname flattening """
        response = self.zonesSettings.update_zone_cname_flattening(
            value=self.value).get_result()
        assert response is not None and response.get('success') is True

    ################## Negative test cases ###################
    def test_2_zone_settings(self):
        pass


if __name__ == '__main__':
    unittest.main()
