# -*- coding: utf-8 -*-
#！/usr/bin/env python
"makeTextFile.py --- create text file"
import os
ls = os.linesep

while True:
    fname = input('Please enter file name:')
    if os.path.exists(fname):
        print("ERROR,'s%' already exists" %fname)
    else:
    	break
	
all = []
print ("\nEnter lines('.' by itself to quit).\n")
while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print ('DONE')