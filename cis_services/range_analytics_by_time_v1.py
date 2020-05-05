# coding: utf-8

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

"""
Retrieves a list of aggregate metrics grouped by time interval.
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class RangeAnalyticsByTimeV1(BaseService):
    """The Range Analytics By Time V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'range_analytics_by_time'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'RangeAnalyticsByTimeV1':
        """
        Return a new client for the Range Analytics By Time service using the
               specified parameters and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier of the zone for which rate
               limit is created.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_identifier,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 zone_identifier: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Range Analytics By Time service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier of the zone for which rate
               limit is created.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn
        self.zone_identifier = zone_identifier


    #########################
    # default
    #########################


    def get_range_analytics_by_time(self, *, metrics: List[str] = None, dimensions: List[str] = None, filters: str = None, sort: List[str] = None, since: datetime = None, until: datetime = None, time_delta: str = None, **kwargs) -> DetailedResponse:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

        Retrieves a list of aggregate metrics grouped by time interval.

        :param List[str] metrics: (optional) One or more metrics to compute.
        :param List[str] dimensions: (optional) Can be used to break down the data
               by given attributes.
        :param str filters: (optional) Used to filter rows by one or more
               dimensions. Filters can be combined using OR and AND boolean logic. AND
               takes precedence over OR in all the expressions. The OR operator is defined
               using a comma (,) or OR keyword surrounded by whitespace. The AND operator
               is defined using a semicolon (;) or AND keyword surrounded by whitespace.
               Comparison options are:.
        :param List[str] sort: (optional) The sort order for the result set; sort
               fields must be included in metrics or dimensions.
        :param datetime since: (optional) Start of time interval to query, defaults
               to until - 6 hours.
        :param datetime until: (optional) End of time interval to query, defaults
               to current time.
        :param str time_delta: (optional) Used to select time series resolution.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsSummaryResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_range_analytics_by_time')
        headers.update(sdk_headers)

        params = {
            'metrics': convert_list(metrics),
            'dimensions': convert_list(dimensions),
            'filters': filters,
            'sort': convert_list(sort),
            'since': since,
            'until': until,
            'time_delta': time_delta
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/analytics/events/bytime'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class GetRangeAnalyticsByTimeEnums:
    """
    Enums for get_range_analytics_by_time parameters.
    """

    class Metrics(Enum):
        """
        One or more metrics to compute.
        """
        COUNT = 'count'
        BYTESINGRESS = 'bytesIngress'
        BYTESEGRESS = 'bytesEgress'
        DURATIONAVG = 'durationAvg'
        DURATIONMEDIAN = 'durationMedian'
        DURATION90TH = 'duration90th'
        DURATION99TH = 'duration99th'
    class Dimensions(Enum):
        """
        Can be used to break down the data by given attributes.
        """
        EVENT = 'event'
        APPID = 'appID'
        COLONAME = 'coloName'
        IPVERSION = 'ipVersion'
    class TimeDelta(Enum):
        """
        Used to select time series resolution.
        """
        YEAR = 'year'
        QUARTER = 'quarter'
        MONTH = 'month'
        WEEK = 'week'
        DAY = 'day'
        HOUR = 'hour'
        DEKAMINUTE = 'dekaminute'
        MINUTE = 'minute'

