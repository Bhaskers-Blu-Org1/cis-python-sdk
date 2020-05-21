# coding: utf-8
# (C) Copyright IBM Corp. 2020.

"""
Sample code to execute dns record import/export api
"""

import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.dns_record_bulk_v1 import DnsRecordBulkV1
from http.client import HTTPConnection


class DNSRecordBulkV1Sample:
    """ Sample function to call DNS Record import/export sdk functions """

    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        HTTPConnection.debuglevel = 1
        self.dns = DnsRecordBulkV1.new_instance(service_name="cis_services")
        self.dns.set_service_url(self.endpoint)

    def get_dns_records_bulk(self):
        resp = self.dns.get_dns_records_bulk(
            crn=self.crn, zone_identifier=self.zone_id)
        print(resp.get_result().text)

    def post_dns_records_bulk(self):
        data = open("~/Downloads/test.txt", "rb")
        resp = self.dns.post_dns_records_bulk(
            crn=self.crn, zone_identifier=self.zone_id, file=data)
        print(resp)

# curl --location --request POST 'https://{{cis_int_endpoint}}/v1/{{crn}}/zones/{{zone_id}}/dns_records_bulk' --header 'Authorization: Bearer <token>' --header --form 'file=@~/Downloads/test.txt' -v
