from utils import parsemac
import oui_lookup
from datetime import datetime
today = '01-24-2020'
date = datetime.now()
d = date.strftime("%m-%d-%Y")

source_file = 'allarpclean-01-24-2020.txt'
# source_file = 'allarpclean-test.txt'
target_file = f'{source_file[0:-4]}-OUT.txt'
working_list = []
final_list = []
vlans_in_list = []
sites = {
		'smc-core-c65-1' : 'SMC',
		'franklin-core-c4k-1' : 'FRANKLIN',
		'sfh-core-c4k-2': 'SFH',
		'sfh-core-c4k-1': 'SFH',
		'sjoc-core-c4k-2' : 'SJOC',
		'sjoc-core-c4k-1': 'SJOC',
		'emh-core-c4k-2' : 'EMH',
		'emh-core-c4k-1' : 'EMH',
		'slh-core-c4k-2': 'SLH',
		'slh-core-c4k-1': 'SLH',
		'franklinmob-core-c4k-2': 'FRANKLIN-MOB',
		'franklinmob-core-c4k-1': 'FRANKLIN-MOB',
		'rawson-core-rtr-2': 'RAWSON',
		'rawson-core-rtr-1': 'RAWSON',
		'emh-core-pa-1' : 'EMH',
		'franklin-core-pa-1' : 'FRANKLIN',
		'sfh-core-pa-1' : 'SFH',
		'sjoc-core-pa-1' : 'SJOC',
		'sjh-core-pa-1': 'SJH',
		'slh-core-pa-1': 'SJH',
		'smc-core-pa-1': 'SMC'}
vlans = {
'Vlan100' : 'Net-Mgmt-10.65.1.0/22',
'Vlan101' : 'ilo-10.112.194.32m28',
'Vlan102' : 'server-10.112.207.160m27',
'Vlan103' : 'premierRAD-10.112.207.192/28',
'Vlan104' : 'CDC-Wireless-Management-10.65.4',
'Vlan108' : 'Data-10.65.8.0/21',
'Vlan110' : 'clean-10.112.195.0m25',
'Vlan164' : 'Guest-10.65.64.x/21',
'Vlan171' : 'PC-Lab-10.112.192.192/27',
'Vlan172' : 'voice-10.112.200-m22',
'Vlan173' : 'elan_10.112.192.96m27',
'Vlan174' : 'tlan_10.112.192.128m26',
'Vlan191' : 'ah-aia',
'Vlan220' : 'byod-10.65.120.0/22',
'Vlan251' : 'Pharmacy-ATC',
'Vlan252' : 'Printers',
'Vlan260' : 'Vendor-10.65.160.x/22',
'Vlan268' : 'Environmental',
'Vlan272' : 'Security',
'Vlan276' : 'Wireless VOICE',
'Vlan284' : 'Clinical',
'Vlan292' : 'wirelessData-10.112.204/23',
'Vlan310' : 'GE-IX',
'Vlan312' : 'GE-Misc',
'Vlan316' : 'CDC-PDU-Control-10.6.216/23',
'Vlan318' : 'CSM-Pri-10.65.218.0',
'Vlan320' : 'WIAPP-Wireless',
'Vlan321' : 'WIAPP-Wired',
'Vlan331' : 'mychart-10.65.231/24',
'Vlan332' : 'Vendor-Pitneybowes-10.65.232.0/2',
'Vlan336' : 'Register-Net-10.65.232.16/28',
'Vlan340' : 'Facilities-Radio',
'Vlan348' : 'Carepoint',
'Vlan352' : 'WHEPP-Radio',
'Vlan356' : 'WIAPP-Public',
'Vlan357' : 'WIAPP-Transit',
'Vlan358' : 'WIAPP-TransitNEW',
'Vlan392' : 'Virus-Net-10.65.232.240/29',
'Vlan400' : 'CDC-PCI-10.65.236.0/24',
'Vlan407' : 'Lab-PCI-10.65.243.0/28',
'Vlan427' : 'API-TimeClocks-10.65.248.0/24',
'Vlan450' : 'Wander_Guard',
'Vlan514' : 'TEMP_RSPAN_for_SBC',
'Vlan607' : 'VirusPen-NoRouting',
'Vlan667' : 'Vendor-inside',
'Vlan668' : 'QS1 Inside',
'Vlan669' : 'WOC-public-internet',
'Vlan671' : 'Test-PCI-Network-L2',
'Vlan888' : 'Native-Vlan',
'Vlan950' : 'Transit',
'Vlan999' : 'DVS-Recording-SPAN'}
unneeded_items = '''172.16.130.164
10.114.4.1
10.114.4.2
10.114.4.3
10.114.4.4
10.114.0.1
10.114.0.2
10.114.0.3
10.114.0.4
10.111.0.1
192.168.101.11
192.168.101.10
192.168.101.9
192.168.101.8
10.22.1.1
10.22.1.2
10.22.1.3
10.147.136.1
10.34.1.1
10.34.1.2
10.34.1.3
10.70.8.1
10.70.8.2
10.70.8.3
172.16.48.1
172.16.48.2
172.16.48.3
172.16.89.1
172.16.89.2
172.16.89.3
172.16.132.1
10.62.172.1
10.62.172.2
10.62.172.3
10.62.232.2
10.62.232.3
10.69.176.1
10.69.176.2
10.69.176.3
10.69.232.1
10.69.232.2
10.69.232.3
10.130.8.1
10.130.8.2
10.130.8.3
10.130.152.1
10.130.152.2
10.130.152.3
10.130.172.1
10.130.172.2
10.130.172.3
172.16.12.1
172.16.12.2
172.16.12.3
172.16.128.144
172.16.130.105
172.16.130.108
172.16.132.18
172.16.132.19
172.16.136.1
172.16.136.4
172.16.136.5
172.16.176.1
172.16.176.9
172.16.176.10
172.16.251.1
172.16.251.2
172.16.251.3
10.62.232.1
10.62.232.33
10.62.232.34
10.62.232.35
10.69.212.2
10.69.212.3
10.69.176.11
10.69.212.1
10.69.212.2
10.69.212.3
10.70.232.33
10.70.232.34
10.70.232.35
10.70.232.33
10.70.232.34
10.70.232.35
10.114.232.49
10.114.232.50
10.114.232.51
10.114.232.49
10.114.232.50
10.114.232.51
10.52.232.34
10.52.232.35
10.52.232.33
10.52.232.34
10.52.232.35
10.62.184.62
192.168.3.10
10.130.184.13
10.62.184.62
192.168.3.10
10.130.184.13'''.strip().splitlines()
oui_list = {
    '00000C' : 'Cisco Systems, Inc',
    '001CC5': '3Com Ltd',
    '001c57' : 'Cisco Systems',
    '00013E' : 'Cisco Systems',
    '000732': 'AAEON Technology Inc.',
    '00190F': 'Advansus Corp.',
    '00D0C9': 'ADVANTECH CO., LTD.',
    '74FE48': 'ADVANTECH CO., LTD.',
    '000BAB': 'Advantech Technology (CHINA) Co., Ltd.',
    'C400AD': 'Advantech Technology (CHINA) Co., Ltd.',
    '080066': 'AGFA CORPORATION',
    '000299': 'Apex, Inc.',
    '008066': 'ARCOM CONTROL SYSTEMS, LTD.',
    '00187D': 'Armorlink Co .Ltd',
    '74D02B': 'ASUSTek COMPUTER INC.',
    'E03F49': 'ASUSTek COMPUTER INC.',
    '000AF7': 'Broadcom',
    '001018': 'Broadcom',
    '00B0D0': 'Dell Inc.',
    '001395': 'congatec AG',
    '000D05': 'cybernet manufacturing inc.',
    '004097': 'DATEX DIVISION OF',
    'F01FAF': 'Dell Inc.',
    '0019B9': 'Dell Inc.',
    '3417EB': 'Dell Inc.',
    '90B11C': 'Dell Inc.',
    '44A842': 'Dell Inc.',
    '842B2B': 'Dell Inc.',
    'BC305B': 'Dell Inc.',
    '00096B': 'IBM Corp',
    '001EC9': 'Dell Inc.',
    '509A4C': 'Dell Inc.',
    '000129': 'DFI Inc.',
    '00409D': 'DigiBoard',
    '00016C': 'FOXCONN',
    '001999': 'Fujitsu Technology Solutions GmbH',
    '901B0E': 'Fujitsu Technology Solutions GmbH',
    'ECB1D7': 'Hewlett Packard',
    '40A8F0': 'Hewlett Packard',
    '9C8E99': 'Hewlett Packard',
    '00306E': 'Hewlett Packard',
    '78ACC0': 'Hewlett Packard',
    '8CDCD4': 'Hewlett Packard',
    'D89D67': 'Hewlett Packard',
    '645106': 'Hewlett Packard',
    '001871': 'Hewlett Packard',
    'DC4A3E': 'Hewlett Packard',
    '480FCF': 'Hewlett Packard',
    '78E7D1': 'Hewlett Packard',
    '68B599': 'Hewlett Packard',
    'D48564': 'Hewlett Packard',
    'A45D36': 'Hewlett Packard',
    'A0481C': 'Hewlett Packard',
    'C4346B': 'Hewlett Packard',
    'B4B52F': 'Hewlett Packard',
    '0019BB': 'Hewlett Packard',
    '24BE05': 'Hewlett Packard',
    'E83935': 'Hewlett Packard',
    '001635': 'Hewlett Packard',
    'A0D3C1': 'Hewlett Packard',
    '40B034': 'Hewlett Packard',
    '5065F3': 'Hewlett Packard',
    '6C3BE5': 'Hewlett Packard',
    '0017A4': 'Hewlett Packard',
    '001185': 'Hewlett Packard',
    '30E171': 'Hewlett Packard',
    'C8D9D2': 'Hewlett Packard',
    '10E7C6': 'Hewlett Packard',
    '001083': 'Hewlett Packard',
    '5CF3FC': 'IBM Corp',
    '000012': 'INFORMATION TECHNOLOGY LIMITED',
    '00D023': 'INFORTREND TECHNOLOGY, INC.',
    '00E0F4': 'INSIDE Technology A/S',
    '001E67': 'Intel Corporate',
    '6805CA': 'Intel Corporate',
    '001B21': 'Intel Corporate',
    'A0369F': 'Intel Corporate',
    '000E0C': 'Intel Corporation',
    'E09D31': 'Intel Corporate',
    '000423': 'Intel Corporation',
    '001111': 'Intel Corporation',
    '003018': 'Jetway Information Co., Ltd.',
    '00108D': 'Johnson Controls, Inc.',
    'EC13DB': 'Juniper Networks',
    '3C6104': 'Juniper Networks',
    'F01C2D': 'Juniper Networks',
    '5C5EAB': 'Juniper Networks',
    '100E7E': 'Juniper Networks',
    '88A25E': 'Juniper Networks',
    '00900B': 'LANNER ELECTRONICS, INC.',
    'D43D7E': 'Micro-Star Int"l Co, Ltd',
    '0090E8': 'MOXA TECHNOLOGIES CORP., LTD.',
    '000FB5': 'NETGEAR',
    '00E081': 'TYAN COMPUTER CORP.',
    '00144F': 'Oracle Corporation ',
    '7C0507': 'PEGATRON CORPORATION',
    '54B203': 'PEGATRON CORPORATION',
    '008082': 'PEP MODULAR COMPUTERS GMBH',
    '00C09F': 'QUANTA COMPUTER INC.',
    '000050': 'RADISYS CORPORATION',
    '78593E': 'RAFI GmbH &amp; Co.KG',
    '004017': 'Silex Technology America',
    '008092': 'Silex Technology, Inc.',
    '00D056': 'SOMAT CORPORATION',
    '0008FB': 'SonoSite, Inc.',
    '0CC47A': 'Super Micro Computer, Inc.',
    '002590': 'Super Micro Computer, Inc.',
    '00A0A5': 'TEKNOR MICROSYSTEME, INC.',
    '0001F0': 'Tridium, Inc.',
    '000667': 'Tripp Lite',
    'FC4DD4': 'Universal Global Scientific Industrial Co., Ltd.',
    'C47DCC': 'Zebra Technologies Inc',
    '6C2B59': 'Dell Inc.',
    '84248D': 'Zebra Technologies Inc',
    '009C02': 'Hewlett Packard',
    '001517': 'Intel Corporate',
    '44E49A': 'OMNITRONICS PTY LTD',
    '00907A': 'Spectralink, Inc',
    '00013E': 'Ascom Tateco AB',
    '94FB29': 'Zebra Technologies Inc.',
    'F4CFE2': 'Cisco Systems, Inc', }
oui_used = []
dev_list = []
def getoui(mac):
    mac = mac.upper()
    if len(mac) == 17:
        return mac[:8]
    elif len(mac) == 14:
        return mac[:7]
def ouilookup(oui):
    oui_list = {'0000.0C': 'Cisco Systems, Inc',
             '001C.57': 'Cisco Systems, Inc',
             '009C.02': 'Hewlett Packard',
             '54B2.03': 'PEGATRON CORPORATION',
             'C8D9.D2': 'Hewlett Packard',
             '0000.12': 'INFORMATION TECHNOLOGY LIMITED',
             '0040.9D': 'DigiBoard',
             '00C0.9F': 'QUANTA COMPUTER INC.',
             '001E.C9': 'Dell Inc.',
             '0090.E8': 'MOXA TECHNOLOGIES CORP., LTD.',
             '0001.6C': 'FOXCONN',
             '0030.18': 'Jetway Information Co., Ltd.',
             '44E4.9A': 'OMNITRONICS PTY LTD',
             '90B1.1C': 'Dell Inc.',
             '8424.8D': 'Zebra Technologies Inc',
             '0006.F6': 'Cisco Systems, Inc',
             'B0FA.EB': 'Cisco Systems, Inc',
             '0001.3E': 'Ascom Tateco AB',
             'BC16.65': 'Cisco Systems, Inc',
             '7CAD.74': 'Cisco Systems, Inc',
             '001C.C5': '3Com Ltd',
             '0090.0B': 'LANNER ELECTRONICS, INC.',
             '0006.67': 'Tripp Lite',
             '0019.0F': 'Advansus Corp.',
             'F0D5.BF': 'Intel Corporate',
             'A048.1C': 'Hewlett Packard',
             'C434.6B': 'Hewlett Packard',
             '000E.0C': 'Intel Corporation',
             'F01C.2D': 'Juniper Networks',
             '0015.17': 'Intel Corporate',
             '74:FE:48': 'ADVANTECH CO., LTD.',
             '00:D0:C9': 'ADVANTECH CO., LTD.',
             '00:40:97': 'DATEX DIVISION OF',
             '40:A8:F0': 'Hewlett Packard',
             '00:15:17': 'Intel Corporate',
             '00:D0:56': 'SOMAT CORPORATION',
             '3C:61:04': 'Juniper Networks',
             '00:0B:AB': 'Advantech Technology (CHINA) Co., Ltd.',
             'A0:48:1C': 'Hewlett Packard',
             'C4:00:AD': 'Advantech Technology (CHINA) Co., Ltd.',
             'F0:1F:AF': 'Dell Inc.',
             '00:10:83': 'Hewlett Packard',
             'EC:13:DB': 'Juniper Networks',
             '00:30:6E': 'Hewlett Packard',
             '10:E7:C6': 'Hewlett Packard',
             '00:19:0F': 'Advansus Corp.',
             'C4:7D:CC': 'Zebra Technologies Inc',
             '00:40:17': 'Silex Technology America',
             'D4:3D:7E': "Micro-Star Int'l Co, Ltd", '64:51:06': 'Hewlett Packard',
             '00:14:4F': 'Oracle Corporation ',
             '08:00:66': 'AGFA CORPORATION',
             'A0:36:9F': 'Intel Corporate',
             '68:05:CA': 'Intel Corporate',
             '00:00:50': 'RADISYS CORPORATION',
             '78:E7:D1': 'Hewlett Packard',
             '44:A8:42': 'Dell Inc.',
             '74:D0:2B': 'ASUSTek COMPUTER INC.',
             'FC:4D:D4': 'Universal Global Scientific Industrial Co., Ltd.',
             'CC:46:D6': 'Cisco Systems, Inc',
             'B4:B5:2F': 'Hewlett Packard',
             '68:B5:99': 'Hewlett Packard',
             'A4:5D:36': 'Hewlett Packard',
             '00:80:82': 'PEP MODULAR COMPUTERS GMBH',
             '00:9C:02': 'Hewlett Packard',
             '30:E1:71': 'Hewlett Packard',
             '00:D0:23': 'INFORTREND TECHNOLOGY, INC.',
             '00:10:18': 'Broadcom',
             '50:9A:4C': 'Dell Inc.',
             '00:19:BB': 'Hewlett Packard',
             '00:0A:F7': 'Broadcom',
             '78:59:3E': 'RAFI GmbH & Co.KG',
             '00:25:90': 'Super Micro Computer, Inc.',
             '00:0F:B5': 'NETGEAR',
             '00:19:99': 'Fujitsu Technology Solutions GmbH',
             '00:13:95': 'congatec AG',
             '8C:DC:D4': 'Hewlett Packard',
             '9C:8E:99': 'Hewlett Packard',
             '24:BE:05': 'Hewlett Packard',
             '6C:2B:59': 'Dell Inc.',
             '84:2B:2B': 'Dell Inc.',
             '00:11:11': 'Intel Corporation',
             'BC:30:5B': 'Dell Inc.',
             '00:02:99': 'Apex, Inc.',
             '00:09:6B': 'IBM Corp',
             'EC:B1:D7': 'Hewlett Packard',
             '00:E0:F4': 'INSIDE Technology A/S',
             'D4:85:64': 'Hewlett Packard',
             '3C:A8:2A': 'Hewlett Packard',
             '88:51:FB': 'Hewlett Packard',
             '50:65:F3': 'Hewlett Packard',
             '18:60:24': 'Hewlett Packard',
             '00:10:20': 'Hand Held Products Inc',
             'F4:CF:E2': 'Cisco Systems, Inc',
             '5C:5E:AB': 'Juniper Networks',
             '00:1B:21': 'Intel Corporate',
             '00:90:0B': 'LANNER ELECTRONICS, INC.',
             '00:B0:D0': 'Dell Inc.',
             '00:E0:81': 'TYAN COMPUTER CORP.',
             '00:16:35': 'Hewlett Packard',
             'A0:D3:C1': 'Hewlett Packard',
             '40:B0:34': 'Hewlett Packard',
             '00:01:F0': 'Tridium, Inc.',
             '00:18:7D': 'Armorlink Co .Ltd',
             '00:0E:0C': 'Intel Corporation',
             '00:04:23': 'Intel Corporation',
             '00:16:B9': 'ProCurve Networking by HP',
             '00:11:85': 'Hewlett Packard',
             '00:01:6C': 'FOXCONN',
             '00:1D:B3': 'HPN Supply Chain',
             '00:0D:05': 'cybernet manufacturing inc.',
             '90:1B:0E': 'Fujitsu Technology Solutions GmbH',
             '10:0E:7E': 'Juniper Networks',
             '88:A2:5E': 'Juniper Networks',
             '00:19:B9': 'Dell Inc.',
             '00:17:A4': 'Hewlett Packard',
             '5C:F3:FC': 'IBM Corp',
             'D8:9D:67': 'Hewlett Packard',
             '00:80:92': 'Silex Technology, Inc.',
             'E0:9D:31': 'Intel Corporate'}
    try:
        vendor = oui_list.get(oui)
        if vendor is None:
            return 'not available'
        return oui_list.get(oui)
    except:
        return f'Not available'
def add_vlan_to_list(vlan):
    if vlan in vlans_in_list:
        return False
    vlans_in_list.append(vlan)
    return True
def add_oui_to_list(oui):
    if oui in oui_used:
        pass
    oui_used.append(oui)
# read the lines in from the source file, strip off the new line charictors and split the entries into items
# and add them to the working list
print(f'+------------------Creating working list from {source_file}---------------------+')
with open (source_file) as list:
    for line in list:
        working_list.append(line.strip('\n').split())
        # print(working_list)
print(f'+-----------------------Reordering items in working list---------------------------+')

# cheack each item in list and if it is in the unneeded items list remove it
# collum item Internet and ARPA
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
print(oui_used)
print(len(oui_used))

for line in final_list:
    device = line[0]
    if device in dev_list:
        continue
    dev_list.append(device)


print(f'+-------------------Printing final summary-----------------------+')
# print(f'The total number of Vlans used is: {len(vlans_in_list}')
print(f'Vlans used: {vlans_in_list}')
print(f'Devices in list: {dev_list}')
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