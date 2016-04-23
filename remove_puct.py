import sys
import re
PUCTUATION ='[@&;#*%()+^/]'
COMBINATION = '.com'
PUCTUATION.encode('latin-1')
# check if has the corrected argv

def validate_input():
    if len(sys.argv) < 3:
        print ('Uasge: python3 <remove_puct.py> <input> <output>')
        sys.exit()
    else:
        try:
            with open(sys.argv[1], 'r')  as f_in:
                pass
        except:
                print(sys.argv[1], ': File not found')
                sys.exit()


# remove lines contains defined chars

def remove_puctuation():
    puct = PUCTUATION
    comb = COMBINATION
    with open(sys.argv[1], 'r', encoding = 'latin-1')  as f_in:
        for line in f_in:
            # strip empty lines
            line = line.strip()
            if len(line) == 0:
                continue
            found_puct = re.findall(puct, line)
            found_comb = re.findall(comb, line)
            if (not found_puct) and (not found_comb):
                line = line + '\n'
                write_to_file(line)


def write_to_file(line):
    with open(sys.argv[2],'a', encoding = 'latin-1') as f_out:
        f_out.write(line)


def run():
    validate_input()
    remove_puctuation()


run()
