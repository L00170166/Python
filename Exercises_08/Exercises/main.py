'''
Script: devices.py
By: CF
Purpose: Class and OO
Prerequisites: 
Tested: on Python v3.10.7 under Windows 11
Revision History:
Notes:
Do not edit the values in this script, all fixed settings are maintained at .\Python\Exercises_08\Exercises
This script has no error handling, by design.
'''
from devices import Firewall, load_balncer, switch
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")
firewall27.configure_firewall()
from devices import Firewall
# Create a switch instance
switch30 = switch("switch32")
# Configure it
switch30.configure_switch()
# Create a switch instance
switch31 = switch("switch31")
# Verify a CRC
switch30.calculate_crc("dummy data")
switch30.configure_switch()
# Create a load_balancer instance
load_balancer51 = load_balncer("load_balancer")
# Configure it
load_balancer51.configure_load_balncer()
# Create a firewall instance
load_balancer51 = load_balncer("load_balncer51")
# Verify a CRC
load_balancer51.calculate_crc("dummy data")
#load_balancer51.configure_load_balancer()

