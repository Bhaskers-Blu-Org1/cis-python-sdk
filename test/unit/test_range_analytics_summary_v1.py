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
from cis_services.range_analytics_summary_v1 import RangeAnalyticsSummaryV1

crn = 'testString'
zone_identifier = 'testString'

service = RangeAnalyticsSummaryV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GetRangeAnalytics
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_range_analytics_summary
#-----------------------------------------------------------------------------
class TestGetRangeAnalyticsSummary():

    #--------------------------------------------------------
    # get_range_analytics_summary()
    #--------------------------------------------------------
    @responses.activate
    def test_get_range_analytics_summary_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/analytics/events/summary'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"rows": 2, "data": ["data"], "totals": "unknown property type: totals", "min": "unknown property type: min", "max": "unknown property type: max", "data_lag": 8, "query": {"metrics": ["count"], "dimensions": ["event"], "filters": "event==connect AND coloName!=SFO", "sort": [{"id": "id", "desc": true}], "since": "2019-01-01T12:00:00", "until": "2019-01-01T12:00:00", "limit": 10000}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Set up parameter values
        accept = 'testString'
        metrics = ['count']
        dimensions = ['event']
        filters = 'testString'
        sort = ['testString']
        since = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        until = datetime.fromtimestamp(1580236840.123456, timezone.utc)

        # Invoke method
        response = service.get_range_analytics_summary(
            accept=accept,
            metrics=metrics,
            dimensions=dimensions,
            filters=filters,
            sort=sort,
            since=since,
            until=until
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'metrics={}'.format(','.join(metrics)) in query_string
        assert 'dimensions={}'.format(','.join(dimensions)) in query_string
        assert 'filters={}'.format(filters) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string


    #--------------------------------------------------------
    # test_get_range_analytics_summary_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_range_analytics_summary_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/range/analytics/events/summary'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"rows": 2, "data": ["data"], "totals": "unknown property type: totals", "min": "unknown property type: min", "max": "unknown property type: max", "data_lag": 8, "query": {"metrics": ["count"], "dimensions": ["event"], "filters": "event==connect AND coloName!=SFO", "sort": [{"id": "id", "desc": true}], "since": "2019-01-01T12:00:00", "until": "2019-01-01T12:00:00", "limit": 10000}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='*/*',
                      status=200)

        # Invoke method
        response = service.get_range_analytics_summary()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetRangeAnalytics
##############################################################################

