from datetime import datetime
from arpcleantools import getoui, ouilookup, add_vlan_to_list, vlans, vlans_used, ouis_used, devices_used, sites, unneeded_items
from operator import itemgetter
sites_file = 'sites.yml'
date = datetime.now()
d = date.strftime("%m-%d-%Y")
source_file = 'allarpclean-01-28-2020.txt'
# source_file = 'allarpclean-test.txt'
target_file = f'{source_file[0:-4]}-OUT.txt'
working_list = []
final_list = []

'''read the lines in from the source file, strip off the new line charictors and split the entries into items
and add them to the working list'''
print(f'+------------------Creating working list from {source_file}---------------------+')
with open (source_file) as list:
    for line in list:
        working_list.append(line.strip('\n').split())
print(f'+-----------------------Reordering items in working list---------------------------+')

'''check each item in list and if it is in the unneeded items list remove it
collum item Internet and ARPA'''
for item in working_list:
    if 'GigabitEthernet' in item[-1]:
        vlan_str = 'Vlan' + item.pop(6)[-3:]
        item.pop(5)
        item.pop(3)
        item.pop(1)
        item.append(vlan_str)
    elif 'Internet'in item[1]:
        item.pop(5)
        item.pop(3)
        item.pop(1)
    elif 'ethernet' in item[1] and item[4]:
        item.pop(6)
        item.pop(5)
        item.pop(4)
        vlan_str = 'Vlan' + item.pop(1)[-3:]
        item.append(vlan_str)
interium_list = []
ignored_lines = 0
duplicated_lines = 0

print(f'+-----------------------Removing unneeded lines---------------------------+')
'''Check to see if ip address is in the un-needed items list and ignore it if it is
If item is OK, add it to the final list'''
for line in working_list:
    current_ip = line[1]
    current_vlan = line[3]
    if current_ip in unneeded_items:
        ignored_lines += 1
        continue
    elif current_ip.startswith('10.114'):
        if current_vlan == 'Vlan276':
            ignored_lines += 1
            continue
    interium_list.append(line)
tmp_list  = []

print(f'+-----------------------Removing duplicate lines---------------------------+')
'''Check to see if ip address is in the un-needed items list and ignore it if it is
If item is OK, add it to the final list'''
print(f'{interium_list[0]} lenth of list is: {len(interium_list)}')
for line in interium_list:
    if line[1] in tmp_list:
        duplicated_lines += 1
        continue
    else:
        tmp_list.append(line[1])
        final_list.append(line)

print(f'+-------------------Printing statistical informaion-----------------------+')
print(f'\tThe size of the working list is {len(working_list)}')
print(f'\tlines skipped: {ignored_lines}')
print(f'\tlines with duplicates: {duplicated_lines}')

print(f'\tThe size of the final list is {len(final_list)}')

# Go through the final list and lookup the VLAN name from the Vlan Key and append it to the item
# Go through the final list and lookup MAC address and append the Vendor Name to the item
print(f'+-------------------Adding Vlan Name to list-----------------------+')
for i, line in enumerate(final_list):
    vlan_str = line[3]
    vlan_name = vlans.get(vlan_str)
    if type(vlan_name) is None or vlan_name == 'None':
        continue
    line.append(vlan_name)
    add_vlan_to_list(vlan_str)
print(f'+-------------------Adding Site Name to list-----------------------+')
for line in final_list:
    site_name = sites.get(line[0])
    line.insert(0, site_name)

print(f'+-------------------Adding Vendor Name to list-----------------------+')
for line in final_list:
    oui = getoui(line[3])
    oui_name = ouilookup(oui)
    line.insert(4,oui_name)
    line.append(d)
print(ouis_used)
print(len(ouis_used))

for line in final_list:
    device = line[0]
    if device in devices_used:
        continue
    devices_used.append(device)


print(f'+-------------------Printing final summary-----------------------+')
# print(f'The total number of Vlans used is: {len(vlans_in_list}')
print(f'Vlans used: {vlans_used}')
print(f'Devices in list: {devices_used}')
print(f'The length of the working list is {len(working_list)}')
# for i, line in enumerate(final_list):
#     print(f'the key of {i} with elements: {line}')
#     for j, element in enumerate(line):
#         print(f'\tthe key of {j} and its elements: {element}')
print(f'+-------------------Creating output file from final list-----------------------+')

output_list = []

for i, lst in enumerate(final_list):
    try:       # print(f'Idx: {i} Data: {lst}')
        tmp_line = '\t'.join(lst)
        output_list.append(tmp_line)
    except:
        print(f'the script caused an exception at index {i} with line {lst}')
    # print(f'The value of tmp_line is {tmp_line}')
# print(new_list)
# Write each line of the working list to the target file and add a newline char after.
with open(target_file, 'w') as target:
    target.write(f'Site\tDevice\tIP Address\tMAC Address\tVendor\tVLAN\tName\tLast Seen\n')
    for item in output_list:
        target.write(item +'\n')