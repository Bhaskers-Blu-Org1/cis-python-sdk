# coding: utf-8
# Copyright 2019 IBM All Rights Reserved.

"""
Sample code to execute dns record functions
"""

import os
import json
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.dns_records_v1 import DnsRecordsV1


class DnsRecordV1Sample:
    """ Sample function to call dns record sdk functions """

    def __init__(self):
        load_dotenv()
        self.token = os.getenv("TOKEN")
        self.apikey = os.getenv("APIKEY")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.iam_endpoint = os.getenv("IAM_ENDPOINT")
        self.authenticator = IAMAuthenticator(
            apikey=self.apikey, url=self.iam_endpoint)
        self.dns = DnsRecordsV1(authenticator=self.authenticator)
        self.dns.set_service_url(self.endpoint)

    def list_all_dns_records_v1_sample(self):
        """ this method list all dns records """
        response = self.dns.list_all_dns_records(
            crn=self.crn,
            zone_identifier=self.zone_id).get_result()
        print(response)

    def get_dns_record_sample(self):
        """ this method get dns record """
        response = self.dns.get_dns_record(
            self.crn, self.zone_id, "12345")
        print(response)

    def create_dns_record_sample(self):
        """ create dns record """
        record_type = 'A'
        name = 'sample_ibm'
        content = '1.1.1.1'
        response = self.dns.create_dns_record(
            x_auth_user_token=self.token, crn=self.crn,
            zone_identifier=self.zone_id, type=record_type,
            name=name, content=content)
        print(response)

    def delete_dns_record_sample(self):
        """ delete dns record """
        dns_record_id = 'c77650cfb45d37058bda571159f21b6b'
        response = self.dns.delete_dns_record(
            crn=self.crn,
            zone_identifier=self.zone_id,
            dnsrecord_identifier=dns_record_id)
        print(response)

    def update_dns_record_sample(self):
        """ update dns record """
        dns_record_id = 'ec6037e7388450c19b0c7a4dff3232cf'
        record_type = 'A'
        name = 'sample_ibm'
        content = '2.2.2.2'
        response = self.dns.update_dns_record(
            crn=self.crn,
            zone_identifier=self.zone_id,
            dnsrecord_identifier=dns_record_id, type=record_type,
            name=name, content=content)
        print(response)
