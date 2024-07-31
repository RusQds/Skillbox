import os

def cipder_text(path_old, path_new):
    open_old_file = open(path_old, 'r')
    open_new_file = open(path_new, 'w')
    for i, line in enumerate(open_old_file.read().split('\n')):
        for sym in line:
            if sym in alhabet.lower():
                open_new_file.write(alhabet[(alhabet.index(sym.lower()) + i + 1)%len(alhabet)].lower())
            elif sym in alhabet.upper():
                open_new_file.write(alhabet[(alhabet.index(sym.lower()) + i + 1) % len(alhabet)].upper())
            else:
                open_new_file.write(sym)
        open_new_file.write('\n')
    open_new_file.close()
    open_old_file.close()


alhabet = 'abcdefghijklmnopqrstuvwxyz'

path_old = os.path.abspath('text.txt')
path_new = os.path.abspath('cipher_text2.txt')
cipder_text(path_old, path_new)
