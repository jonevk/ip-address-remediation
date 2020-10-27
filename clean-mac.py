from datetime import date
import re
from  datetime import datetime
str_interface = 'ethernet'
str_Internet = 'Internet'
str_device = 'smc-core'
str_vlan = 'Vlan276'
arp_line = []
tmp_file = []
arp_list = []
testtarget = 'allarpclean-01-10-2020.txt'
target= 'allarpclean-test.txt'
today = datetime.now()
ips_to_exclude = '''10.114.4.1
10.114.4.2
10.114.4.3
10.114.4.4
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
172.16.132.1
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
10.62.172.1
10.62.172.2
10.62.172.3
10.62.232.1
10.62.232.2
10.62.232.3
10.62.232.33
10.62.232.34
10.62.232.35
10.69.176.2
10.69.176.3
10.69.212.2
10.69.212.3
10.69.212.11
10.69.212.12
10.69.232.2
10.69.232.3
10.69.176.1
10.69.176.11
10.69.212.1
10.69.212.13
10.69.232.1
10.34.1.1
10.34.1.2
10.34.1.3
10.70.8.1
10.70.8.2
10.70.8.3
10.70.232.33
10.70.232.34
10.70.232.35
10.114.232.49
10.114.232.50
10.114.232.51
172.16.48.1
172.16.48.2
172.16.48.3
172.16.89.1
172.16.89.2
172.16.89.3
10.52.232.34
10.52.232.35
10.52.232.33
10.22.1.1
10.22.1.2
10.22.1.3
10.147.136.1
10.62.184.62
192.168.3.10
10.130.184.13
10.130.184.14
10.130.184.101
10.130.184.102'''.strip().splitlines()


def checkline(line):
    if line[5] == 'ARPA':
        return list('CISCO').append(line)
    elif 'pa' in line[0]:
        return list('PA').append(line)
    else:
        return list('UNK').append(line)


def is_exclude(line):
    pass


def fooline(lst):
    new_line = []
    new_line.append[0]
    for item in line:
        new_line.append(lst)
        return new_line

# with open(target) as f:
#     tmp_file = f.readlines()
#     for line in tmp_file:
#         my_line = line.split()
#         tmp_line = ''
#         tmp_list = []
#         # print (my_line)
#         if 'rtr' in my_line[0]:
#             my_line.pop(3)
#             my_line.append('RTR')
#             my_line.remove('ARPA')
#             my_line.remove('Internet')
#             arp_list.append(my_line)
#         elif str_Internet in my_line[1]:
#             my_line.pop(3)
#             my_line.append('SW')
#             my_line.remove('ARPA')
#             my_line.remove('Internet')
#             arp_list.append(my_line)
#         elif str_interface in my_line[1]:
#             tmp_line = 'Vlan' + str(my_line[1])[-3:]
#             my_line.append(tmp_line)
#             my_line.append('PA')
#             my_line.pop(6)
#             my_line.pop(5)
#             my_line.pop(4)
#             my_line.pop(1)
#             arp_list.append(my_line)
#         else:
#             my_line.append('UNK')
#             arp_list.append(my_line)

# for element in arp_list:
#     print(element)

with open(target) as f:
    tmp_file = f.readlines()
    for line in tmp_file:
        my_line = line.split()
        foo = fooline(my_line)
        print(foo)

new_list=[]
lines_added = 0
lines_skipped = 0
for line in arp_list:
    if str_device in line[0]:
        if str_vlan in line[3]:
            lines_skipped += 1
            continue
    new_list.append(line)
    lines_added += 1



with open ('mac-clean-OUT.txt', mode = 'w') as fout:
    # fout.write(f'---------------+----------------+--------------------------+------------------\n')
    fout.write(f'Device\tIP Address\tMAC Address\tInterface\n')
    # fout.write(f'---------------+----------------+--------------------------+------------------\n')
    for line in new_list:
        fout.write(str(line) + '\n')
    fout.write(f'{__file__.split()[-1]}\n')
    fout.write(f'{today}\n')
    fout.write(f"Total Lines added: {lines_added} Total Lines skipped: {lines_skipped}")

if __name__ == '__main__':
    print (f"{__file__}")


