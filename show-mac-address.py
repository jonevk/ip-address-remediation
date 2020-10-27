interfaces = '''
ethernet1/2.336
ethernet1/2.400
ethernet1/2.406
ethernet1/3.164
ethernet1/3.191
ethernet1/3.220
ethernet1/3.260
ethernet1/4.268
ethernet1/4.331
ethernet1/5.110
ethernet1/5.236
ethernet1/5.284
ethernet1/5.315
ethernet1/5.46
ethernet1/7.310
'''.strip().splitlines()
vlans = []
print(f'Palo Alto Commands')
for interface in interfaces:
    print(f'sh arp {interface}')
    vlan = interface.split('.')[1]
    vlans.append(vlan)

print (vlans)
print(f'Cisco Commands')
for vlan in vlans:
    print(f'show mac address-table vlan {vlan}\n')