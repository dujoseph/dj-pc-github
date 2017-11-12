import re

strdata = '''

'''

pattern = re.compile(r'\bSN:\s*?[0-9A-Z]{8}')
matches = pattern.findall(strdata)
print(matches)
for match in matches:
	print(match)
#print(strdata)
#print(type(data))

