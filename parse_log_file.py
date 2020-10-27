import re as re
pattern = re.compile(r'(^[JFMASOND]\w{2}\s\d{1,2})\s(\d{1,2}:\d{1,2}:\d{1,2})\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s:\s%(ASA-[1-7]-\d{6}):\s(.*)')
log_file = 'files/asa-cdc_log.txt'
log_list =[]
with open(log_file) as stream:
    for line in stream:
        matchs = pattern.finditer(line)
        for match in matchs:
            new_line = []
            new_line.append(match[1])
            new_line.append(match[2])
            new_line.append(match[3])
            print('.',end='')
        log_list.append(new_line)
    print(log_list)
