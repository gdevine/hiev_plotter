'''
Created on 08/08/2013

@author: gerarddevine
'''

import csv
import json

f = open( 'testdata/MROS_AUTO_TSOIL_R_20130807.dat', 'r' )
reader = csv.DictReader( f, fieldnames = ( "id","name","lat","lng" ) )
out = json.dumps( [ row for row in reader ] )
print out