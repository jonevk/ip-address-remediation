CHUNK_SIZE = 80 * 60000 * 4
fout = None
filenumber = 0
working_file = 'files/asa-cdc_log.txt'
linebuffer_SEVERE = ''
linebuffer_CRITICAL = ''
linebuffer_ERROR = ''
linebuffer_WARNING = ''
linebuffer_DEBUG = ''

with open(working_file, 'rt') as f:
    for line in f:
        if 'ASA-1' in line:
            linebuffer_SEVERE = linebuffer_SEVERE + line
        elif 'ASA-2' in line:
            linebuffer_CRITICAL = linebuffer_CRITICAL + line
        elif 'ASA-3' in line:
            linebuffer_ERROR = linebuffer_ERROR + line
        elif 'ASA-4' in line:
            linebuffer_WARNING = linebuffer_WARNING + line
        elif 'ASA-7' in line:
            linebuffer_DEBUG = linebuffer_DEBUG + line
        print('.', end='')

outputfile = open(f'files/asa-cdc_log_SEVERE.txt', 'wt')
outputfile.writelines(linebuffer_SEVERE)
outputfile.close()
outputfile = open(f'files/asa-cdc_log_CRITICAL.txt', 'wt')
outputfile.writelines(linebuffer_CRITICAL)
outputfile.close()
outputfile = open(f'files/asa-cdc_log_ERROR.txt', 'wt')
outputfile.writelines(linebuffer_ERROR)
outputfile.close()
outputfile = open(f'files/asa-cdc_log_WARNING.txt', 'wt')
outputfile.writelines(linebuffer_DEBUG)
outputfile.close()
