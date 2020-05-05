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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
from cis_services.zones_settings_v1 import ZonesSettingsV1

crn = 'testString'
zone_identifier = 'testString'

service = ZonesSettingsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GetZoneDNSSEC
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_zone_dnssec
#-----------------------------------------------------------------------------
class TestGetZoneDnssec():

    #--------------------------------------------------------
    # get_zone_dnssec()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_dnssec_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_dnssec_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_dnssec_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetZoneDNSSEC
##############################################################################

##############################################################################
# Start of Service: UpdateZoneDNSSEC
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_zone_dnssec
#-----------------------------------------------------------------------------
class TestUpdateZoneDnssec():

    #--------------------------------------------------------
    # update_zone_dnssec()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_dnssec_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        status = 'active'

        # Invoke method
        response = service.update_zone_dnssec(
            status=status,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['status'] == status


    #--------------------------------------------------------
    # test_update_zone_dnssec_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_dnssec_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/dnssec'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_zone_dnssec()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateZoneDNSSEC
##############################################################################

##############################################################################
# Start of Service: GetZoneCNAMEFlattening
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_zone_cname_flattening
#-----------------------------------------------------------------------------
class TestGetZoneCnameFlattening():

    #--------------------------------------------------------
    # get_zone_cname_flattening()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_cname_flattening_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.12345Z", "editable": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_zone_cname_flattening()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_cname_flattening_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_cname_flattening_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.12345Z", "editable": true}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_zone_cname_flattening()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetZoneCNAMEFlattening
##############################################################################

##############################################################################
# Start of Service: UpdateZoneCNAMEFlattening
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_zone_cname_flattening
#-----------------------------------------------------------------------------
class TestUpdateZoneCnameFlattening():

    #--------------------------------------------------------
    # update_zone_cname_flattening()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_cname_flattening_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.12345Z", "editable": true}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'flatten_all'

        # Invoke method
        response = service.update_zone_cname_flattening(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_zone_cname_flattening_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_cname_flattening_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/cname_flattening'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.12345Z", "editable": true}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_zone_cname_flattening()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateZoneCNAMEFlattening
##############################################################################

