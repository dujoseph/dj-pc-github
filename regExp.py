import re

strdata = '''

GCONFIG

FW:083
DT:01
SN:
00502D38
ADDR:00502D38
NC:00000001
FP:03
CN:01
XO:0000
CIT:1320
TOD:DFLT
SUP:03480
VOLTS:0FFF
AT+IRP1
AT+IRP1
ID804b01 16.2.2009
I/OK
AT+IUF01?
AT+IUF01?
192.168.10.190
I/OK
AT+IIPA?
AT+IIPA?
192.168.10.40
I/OK
AT+ISNET?
AT+ISNET?
255.255.255.0
I/OK
AT+IIPG?
AT+IIPG?
192.168.1.1
I/OK
AT+IUF02?
AT+IUF02?
15565
I/OK
AT+IMACA?
AT+IMACA?
000C59049C9A
I/OK
AT+IUF07?
AT+IUF07?

I/OK
'''

pattern = re.compile(r'\bSN:\s*?[0-9A-Z]{8}')
matches = pattern.findall(strdata)
print(matches)
for match in matches:
	print(match)
#print(strdata)
#print(type(data))

