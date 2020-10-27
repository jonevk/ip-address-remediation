import yaml
import re as re

'''This tool uses locally stored files that contain the necessary data to run
   These include:
        sites.yml - Contains a list of device keys and associated site Names
        ignore_list.yml -  lists intafaces and other items to exlude from output, such as HSRP, etc.
        oiu.yml - OUI string as a key, with associated Vendor Name
        vlans.yml - VLAN string as a key with associated VLAN Name
        '''
# Defines the support file
sites_file = 'sites.yml'
oui_file = 'oui.yml'
ignored_file = 'ignore_list.yml'
vlan_file = 'vlans.yml'
switch_mapping = 'switch-mapping.yml'
# Defines the support lists
vlans_used = []
ouis_used = []
devices_used = []
device_count = {}
#Used for contains_IP function
search_string_IP = r'\s\S{1,3}\.\S{1,3}\.\S{1,3}\.\S{1,3}\s'
search_string_Incomplete = r'Incomplete'
search_string_Fortinet = r'^wigle\S+\s\d+\.\d+\.\d+\.\d+\s\w\s[0-9,a-f,:]{17}\s[a-z,\-,1-9]+'

with open(sites_file) as f:
    sites = yaml.safe_load(f)

with open(oui_file) as f:
    vendors = yaml.safe_load(f)

with open(ignored_file) as f:
    unneeded_items = yaml.safe_load(f)

with open(vlan_file) as f:
    vlans = yaml.safe_load(f)

with open(switch_mapping) as f:
    switch = yaml.safe_load(f)

# Creates a temport list that will display a summary of OUIs in this run
def add_oui_to_list(oui):
    if oui in ouis_used:
        pass
    ouis_used.append(oui)

# Sanitze the format of a MAC address string to strip off delimitors
# Returns the OUI of the MAC, the original MAC and the output of the
# Vendor lookup based on the OUI
def sanitize(mac):
    mac = mac.upper()
    if '.' in str(mac):
        mac = mac.replace('.', '')
        oui = mac[:6]
    elif ':' in str(mac):
        mac = mac.replace(':', '')
        oui = mac[:6]
    elif '-' in str(mac):
        mac = mac.replace('-', '')
        oui = mac[:6]
    else:
        oui = mac[:6]
        return oui, mac, vendors.get(oui)
    mac_split = (mac[0:2], mac[2:4],mac[4:6],mac[6:8],mac[8:10], mac[10:12])
    mac_normal = ':'.join(mac_split)
    return oui, mac, vendors.get(oui), mac_normal

def is_fortinet(line):
    match = re.search(search_string_Fortinet,line)
    return match, line

def contains_IP(line):
    match = re.search(search_string_IP,line)
    return match, line

def contains_Incomplete(line):
    match = re.search(search_string_Incomplete,line)
    return match, line

# Creates a temport list that will display a summary of VLANs in this run
def add_vlan_to_list(vlan):
    if vlan in vlans_used:
        return False
    vlans_used.append(vlan)
    return True
# Lookup and retrun the value of the Switch field by IP address lookup.
def get_switch(ip):
    value = switch.get(ip)
    return value
# Strip off periods and colons and replace with empty string 
def strip_from_string(string):
    if '.' in str(string):
        return string.replace('.', '')
    elif ':' in str(string):
        return string.replace(':', '')
def parseline(line):
    item = line.split()
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
    elif len(item) == 5:
        item.pop(2)
    return item

# Perform local tests to display expected output functions
if __name__ == '__main__':
    foo = sanitize('0040.9716.5971')
    foo2 = vendors.get('000AF7')
    foo5 = strip_from_string('00:d0:c9:da:6b:03')
    foo6 = strip_from_string('0000.1202.0003')
    foo7 = switch['10.114.210.17']
    foo8 = get_switch('10.62.210.16')
    foo9 = sanitize('c4:7d:cc:00:dc:30')
    print(f'The result for Lookup: smc-g12-c4k-2 should be "SMC" and is {foo2}')
    print(f'The result for Lookup: 000AF7 should be "Broadcom" and is {foo2}')
    print(f'result of strip from string for:00:d0:c9:da:6b:03 {foo5}')
    print(f'result of strip from string for:0000.1202.0003 {foo6}')
    print(f'result of normal from string for: c4:7d:cc:00:dc:30 {foo9[3]}')
    print(f'The Value of switch map is {foo7} and should be emh-603-sw-2_Gi1/0/21')
    print(f'The Value of get switch map for 10.62.210.16 is {foo8} and should be franklin-301-c4k-3_Gi5/14')
    print (foo)
    print (foo9)