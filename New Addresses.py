import yaml
history_files = 'history.yml'
target_file = 'summary-OUT.txt'
working_list = []
working_dict = {'Site-IP_Address' : ['Site', 'Device', 'IP_Address', 'MAC Address', 'Vendor', 'VLAN', 'Name', 'Last Seen']}
summary_list = []
output_list = []
switch_mapping = 'switch-mapping.yml'
# Open the list of history file
with open(history_files) as f:
    history = yaml.safe_load(f)
with open (switch_mapping) as f:
    switch = yaml.safe_load(f)
# add the lines of the list to the working list
for file in history:
    path = f'files/{file}'
    with open(path) as f:
        for line in f:
            line = line.strip().split('\t')
            working_list.append(line)
# Create a key by concatonating the site name and ip address, populate the working dict with data from working list by key
# This will serve to keep one copy of each unique IP address with the most recent date seen
for i, lst in enumerate(working_list):
    key = f'{lst[0]}-{lst[2]}'
    try:
        working_dict[key] = lst
    except:
        print(f'Exception found at index {i} with key of: {key} and value of {lst}  ')
#
for i, lst in enumerate(working_dict):
    print(f'The current key is {i} the current item is {lst}')
    print((working_dict[lst]))
    working_line = '\t'.join(working_dict[lst])
    print(working_line)
    output_list.append(working_line)

with open(target_file, 'w') as target:
    # target.write(f'Site\tDevice\tIP Address\tMAC Address\tVendor\tVLAN\tName\tLast Seen\n')
    for item in output_list:
        target.write(item + '\n')

with open('address-OUT.txt','w') as target:
    for key in working_dict:
        target.write(key + '\n')
