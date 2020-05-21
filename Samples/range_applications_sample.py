# coding: utf-8
# (C) Copyright IBM Corp. 2020.

"""
Sample Range Application
"""
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cis_services.range_applications_v1 import RangeApplicationsV1


class RangeApplicationV1Sample:
    """ Sample Range Application Class """

    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.url = os.getenv("URL")
        self.rapp = RangeApplicationsV1.new_instance(
            service_name="cis_services")
        self.rapp.set_service_url(self.endpoint)

    def create_range_app(self):
        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_direct = ["tcp://12.1.1.1:22"]
        # origin_dns = {
        #         "name": "origin.net"
        #     }
        origin_port = 22
        ip_firewall = True
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"

        resp = self.rapp.create_range_app(crn=self.crn, zone_identifier=self.zone_id, protocol=protocol, dns=dns, origin_direct=origin_direct,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        print(resp)

    def create_range_app_origin_dns(self):
        protocol = "tcp/22"
        dns = {
            "type": "CNAME",
            "name": "example." + self.url
        }
        origin_dns = {
            "name": "origin.net"
        }
        origin_port = 22
        ip_firewall = True
        proxy_protocol = "off"
        edge_ips = {
            "type": "dynamic",
            "connectivity": "all"
        }
        traffic_type = "direct"
        tls = "off"

        resp = self.rapp.create_range_app(crn=self.crn, zone_identifier=self.zone_id, protocol=protocol, dns=dns, origin_dns=origin_dns,
                                          origin_port=origin_port, ip_firewall=ip_firewall, proxy_protocol=proxy_protocol, edge_ips=edge_ips, traffic_type=traffic_type, tls=tls)
        print(resp)
