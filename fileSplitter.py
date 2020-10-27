CHUNK_SIZE = 80 * 60000 * 4
fout = None
filenumber = 0
working_file = 'files/asa-cdc_log.txt'
with open(working_file, 'rt') as f:
    while True:
        linebuffer = f.readlines(CHUNK_SIZE)
        if not linebuffer:
            break
        outputfile = open(f'files/asa-cdc_log_{filenumber}.txt','wt')
        outputfile.writelines(linebuffer)
        outputfile.close()
        filenumber += 1
        print('.',end='')
print(f'Total number of files create is {filenumber}')