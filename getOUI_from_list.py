from utils import parsemac
import oui_lookup
import datetime
today = '01-23-2020'
source_file = 'allarpclean-01-23-2020.txt'
# source_file = 'allarpclean-test.txt'
# target_file = f'{source_file[0:-4]}-OUT.txt'
oui_used = []
working_list = []
def add_to_oui_list(oui_str):
    if oui_str in oui_used:
        return
    oui_used.append(oui_str)

# read the lines in from the source file, strip off the new line charictors and split the entries into items
# and add them to the working list
print(f'+------------------Creating working list from {source_file}---------------------+')

with open (source_file) as list:
    for line in list:
        working_list.append(line.strip('\n').split())

for line in working_list:
    add_to_oui_list(line[3])
    print(oui_used)