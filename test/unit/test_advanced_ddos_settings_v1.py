# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
from cis_services.advanced_ddos_settings_v1 import AdvancedDdosSettingsV1

crn = 'testString'
zone_identifier = 'testString'

service = AdvancedDdosSettingsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GetAdvancedDDoSProtectionStatusForAZone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_advanced_ddos_settings
#-----------------------------------------------------------------------------
class TestGetAdvancedDdosSettings():

    #--------------------------------------------------------
    # get_advanced_ddos_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_advanced_ddos_settings_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/advanced_ddos'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "advanced_ddos", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_advanced_ddos_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_advanced_ddos_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_advanced_ddos_settings_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/advanced_ddos'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "advanced_ddos", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_advanced_ddos_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetAdvancedDDoSProtectionStatusForAZone
##############################################################################

