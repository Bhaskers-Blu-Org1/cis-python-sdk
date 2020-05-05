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
import requests
import responses
from cis_services.routing_v1 import RoutingV1

crn = 'testString'
zone_identifier = 'testString'

service = RoutingV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GetRoutingFeatureSmartRoutingSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_routing_smart_routing
#-----------------------------------------------------------------------------
class TestGetRoutingSmartRouting():

    #--------------------------------------------------------
    # get_routing_smart_routing()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_smart_routing_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_routing_smart_routing()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_routing_smart_routing_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_smart_routing_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_routing_smart_routing()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetRoutingFeatureSmartRoutingSetting
##############################################################################

##############################################################################
# Start of Service: UpdateRoutingFeatureSmartRoutingSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_routing_smart_routing
#-----------------------------------------------------------------------------
class TestUpdateRoutingSmartRouting():

    #--------------------------------------------------------
    # update_routing_smart_routing()
    #--------------------------------------------------------
    @responses.activate
    def test_update_routing_smart_routing_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'false'

        # Invoke method
        response = service.update_routing_smart_routing(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_routing_smart_routing_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_routing_smart_routing_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_routing_smart_routing()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateRoutingFeatureSmartRoutingSetting
##############################################################################

##############################################################################
# Start of Service: GetRoutingFeatureTieredCachingSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_routing_tiered_caching
#-----------------------------------------------------------------------------
class TestGetRoutingTieredCaching():

    #--------------------------------------------------------
    # get_routing_tiered_caching()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_tiered_caching_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/tiered_caching'
        mock_response = '{"result": {"id": "tiered_caching", "value": "true", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_routing_tiered_caching()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_routing_tiered_caching_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_tiered_caching_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/tiered_caching'
        mock_response = '{"result": {"id": "tiered_caching", "value": "true", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_routing_tiered_caching()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetRoutingFeatureTieredCachingSetting
##############################################################################

##############################################################################
# Start of Service: UpdateRoutingFeatureTieredCachingSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_routing_tiered_caching
#-----------------------------------------------------------------------------
class TestUpdateRoutingTieredCaching():

    #--------------------------------------------------------
    # update_routing_tiered_caching()
    #--------------------------------------------------------
    @responses.activate
    def test_update_routing_tiered_caching_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/tiered_caching'
        mock_response = '{"result": {"id": "tiered_caching", "value": "true", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'true'

        # Invoke method
        response = service.update_routing_tiered_caching(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_routing_tiered_caching_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_routing_tiered_caching_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/tiered_caching'
        mock_response = '{"result": {"id": "tiered_caching", "value": "true", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_routing_tiered_caching()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateRoutingFeatureTieredCachingSetting
##############################################################################

##############################################################################
# Start of Service: GetRoutingLatencyAnalytics
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_routing_latency
#-----------------------------------------------------------------------------
class TestGetRoutingLatency():

    #--------------------------------------------------------
    # get_routing_latency()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_latency_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/latency'
        mock_response = '{"result": {"percent_smart_routed": 63.4, "bins": 10, "range": {"min": 0, "max": 1500}, "time_range": {"min": "2019-01-01T12:00:00", "max": "2019-01-01T12:00:00"}, "data": {"lable": ["lable"], "counts": [6], "averages": [8]}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        bins = 38

        # Invoke method
        response = service.get_routing_latency(
            bins=bins
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'bins={}'.format(bins) in query_string


    #--------------------------------------------------------
    # test_get_routing_latency_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_latency_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/latency'
        mock_response = '{"result": {"percent_smart_routed": 63.4, "bins": 10, "range": {"min": 0, "max": 1500}, "time_range": {"min": "2019-01-01T12:00:00", "max": "2019-01-01T12:00:00"}, "data": {"lable": ["lable"], "counts": [6], "averages": [8]}}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_routing_latency()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetRoutingLatencyAnalytics
##############################################################################

##############################################################################
# Start of Service: GetRoutingLatencyColosAnalytics
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_routing_latency_colos
#-----------------------------------------------------------------------------
class TestGetRoutingLatencyColos():

    #--------------------------------------------------------
    # get_routing_latency_colos()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_latency_colos_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/latency/colos'
        mock_response = '{"result": {"type": "FeatureCollection", "features": [{"code": "EWR", "smart_routing_req_count": 6696990, "pct_avg_change": 0.06003951841343536, "no_smart_routing_avg": 651.7771493198342, "smart_routing_avg": 690.9095354778789, "geometry": {"coordinates": [11], "type": "Point"}}]}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_routing_latency_colos()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_routing_latency_colos_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_routing_latency_colos_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/latency/colos'
        mock_response = '{"result": {"type": "FeatureCollection", "features": [{"code": "EWR", "smart_routing_req_count": 6696990, "pct_avg_change": 0.06003951841343536, "no_smart_routing_avg": 651.7771493198342, "smart_routing_avg": 690.9095354778789, "geometry": {"coordinates": [11], "type": "Point"}}]}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_routing_latency_colos()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetRoutingLatencyColosAnalytics
##############################################################################

