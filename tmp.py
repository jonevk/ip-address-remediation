working_dict = {'HEADER_ROW' : ['Site', 'Device', 'IP Address', 'MAC Address', 'Vendor', 'VLAN', 'Name', 'Last Seen']}
print(working_dict.get('HEADER_ROW'))


working_dict['HEADER_ROW2'] = ('HEADER_ROW2' , ['Site', 'Device', 'IP Address', 'MAC Address', 'Vendor', 'VLAN', 'Name', 'Last Seen'])

print(working_dict.get('HEADER_ROW2'))

print(working_dict.pop('HEADER_ROW'))

print(working_dict.get('HEADER_ROW'))
print(working_dict.items('HEADER_ROW'))
