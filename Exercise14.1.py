file_1 = 'sampletext.txt'
file_2 = 'sampletext_replace' + '.txt'
pattern_str = 'had'
replace_str = 'CHANGED'

def sed(pattern_str, replace_str, file_1, file_2):
    try:
        file_in = open(file_1, 'r')
        file_out = open(file_2, 'w')

        for line in file_in:
            line = line.replace(pattern_str, replace_str)
            file_out.write(line)
            
        file_in.close()
        file_out.close()
           
    except:
        print('An error has occurred.')

print(sed(pattern_str, replace_str, file_1, file_2))
