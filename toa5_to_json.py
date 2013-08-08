'''
Created on 08/08/2013

@author: gerarddevine
'''

import csv
import json

ifile = open( 'testdata/MROS_AUTO_TSOIL_R_20130807.dat', 'rb')
reader = csv.reader(ifile)
 
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 1:
        header = row
    elif rownum > 4:
        colnum = 0
        for col in row:
            #print '%-8s: %s' % (header[colnum], col)
            print json.dumps( row, indent=4 )
            colnum += 1
             
    rownum += 1

ifile.close()
print 'done'