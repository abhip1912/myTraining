from urllib import request
import re
data = request.urlopen('http://www.py4inf.com/code/mbox-short.txt').read()
info = data.decode()
# pattern = re.compile(r'.+:')
# matches = pattern.findall(info)
matches = re.findall(r'From:? ([\w.]+@[\w.]+)', info)
#print(matches)


for match in matches:
    print(match)

# print(info)
# for line in data:
# 	info += line.decode('utf-8')
#0.7002


# matches = pattern.finditer(subbed)
# for match in matches:
# 	print(match)


# print(matches)
# matches = pattern.finditer(info)
	# if pattern.match(info):
	# 	print(info, end = '')



# print(re.search(pattern, line))
# print(re.search('Received:', line))

# for line in data:
# 	if re.search(pattern, data):
# 		print(line)
