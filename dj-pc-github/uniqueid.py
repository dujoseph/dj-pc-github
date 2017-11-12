#!/usr/bin/python2.7
# By Dukel Joseph
# This module will read the UID from a text file
# Increament it by one return the result
# Save the the result by overwriting the old value from the text file
import os

class uniqueID(object):
    uidic = {}
    UID = ""
    
    def __init__(self):
        pass
    def inUID(self, inc):
        # result = 1
        # READ VALUE FROM FILE
        uidVar = open("unicID.txt", "r")
        uid = uidVar.read()
        uid = int(uid, 10)
        self.uidic['DEC'] = str(uid)
        hexUID = self.convert(uid)
        hexUID = hexUID.upper()
        self.uidic['HEX'] = hexUID
        #print "Current: %s "%uid
        # INCREAMENT THE VALUE THE VALUE BY N#
        result = uid + inc
        #print(result)
        result = str(result)
        # WRITE VALUE TO FILE
        wrtUID = open("unicID.txt", "w")
        wrtUID.write(result + "\n")
        wrtUID.close()
        #self.uidic['NEXT'] = result
        self.uidic['NEXT'] = self.convert(int(result))
        # RETURN VALUE TO CALLER
        return str(self.uidic['HEX'])
        
    # CONVERT TO HEX AND RETURN 8 DIGIT VALUE
    def convert(self, int_value):
        encoded = format(int_value, 'x')
        length = len(encoded)
        encoded = encoded.zfill(8)
        return encoded

