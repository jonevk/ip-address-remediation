#! /usr/bin/python3
# Version 3.2
from datetime import datetime
from arpcleantools import add_vlan_to_list, vlans, devices_used, sites, sanitize, get_switch, parseline, contains_IP, contains_Incomplete
import re as re

sites_file = 'sites.yml'
date = datetime.now()
d = date.strftime("%m-%d-%Y")
source_file = 'files/allarp.txt'
target_file = f'{source_file[0:-4]}-OUT.txt'
working_list = []
final_list = []
interium_list = []
output_list = []
ignored_lines = 0
duplicated_lines = 0
my_range = range(63,95)
device_count = {}
delete_count = 0

# check if the current line has an IP address in it, if so
# add it to the interium list
with open (source_file) as list:
    for line in list:
        match, item = contains_IP(line)
        if match:
            interium_list.append(line)

for line in interium_list:
    working_list.append(parseline(line))

for i, line in enumerate(working_list):
    for element in line:
        print(element)
        if element == 'Incomplete':
            del(working_list[i])
            delete_count += 1
            print(f'-{element}-', end='')
        continue
    continue
print(f'The number of records deleted is: {delete_count}')

# for i, line in enumerate(working_list):
#     if len(line) == 3:
#         continue
#     vlan_str = line[3]
#     vlan_name = vlans.get(vlan_str)
#     if type(vlan_name) is None or vlan_name == 'None' or line[2]=='Incomplete':
#         continue
#     line.append(vlan_name)
#     add_vlan_to_list(vlan_str)
#
# for line in working_list:
#     site_name = sites.get(line[0])
#     line.insert(0, site_name)
#
# for line in working_list:
#     oui, mac, vendor = sanitize(line[3])
#     line.insert(4,vendor)
#     line.append(get_switch(line[2]))
#     line.append(d)
#
# for line in working_list:
#     device = line[0]
#     if device in devices_used:
#         continue
#     devices_used.append(device)
#
# for item in working_list:
#     lcl = item[0]
#     if lcl in device_count:
#         device_count[lcl] += 1
#     else:
#         device_count[lcl] = 1
# print(device_count)
#
# with open(target_file, 'w') as target:
#     target.write(f'Site\tDevice\tIP Address\tMAC Address\tVendor\tVLAN\tName\tLast Seen\n')
#     for line in working_list:
#         for item in line:
#             target.write(f'\t{item}')
#         target.write(f'\n')
with open(target_file, 'w') as target:
    target.write(f'Site\tDevice\tIP Address\tMAC Address\tVendor\tVLAN\tName\tLast Seen\n')
    for line in working_list:
        for item in line:
            target.write(f'\t{item}')
        target.write(f'\n')
