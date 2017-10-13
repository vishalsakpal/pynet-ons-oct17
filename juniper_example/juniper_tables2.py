#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.lldp import LLDPNeighborTable
from getpass import getpass
from pprint import pprint

def hit_enter():
    try:
        raw_input("Hit enter to continue: ")
    except NameError:
        input("Hit enter to continue: ")

juniper_srx = {
    "host": "srx1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}

def juniper_print(k, v):
    print()
    print(k)
    print('-' * 20)
    pprint(v)
    print('-' * 20)

a_device = Device(**juniper_srx)
a_device.open()

eth_ports = EthPortTable(a_device)
eth_ports.get()
print('-' * 80)
print("Ethernet Ports")
for k, v in eth_ports.items():
    juniper_print(k, v)
print('-' * 80)
hit_enter()

arp = ArpTable(a_device)
arp.get()
print('-' * 80)
print("ARP")
for k, v in arp.items():
    juniper_print(k, v)
print('-' * 80)
hit_enter()

lldp = LLDPNeighborTable(a_device)
lldp.get()
print('-' * 80)
print("LLDP Neighbors")
for k, v in lldp.items():
    juniper_print(k, v)
print('-' * 80)
hit_enter()
print('-' * 80)
