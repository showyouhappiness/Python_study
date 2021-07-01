import re

phone = '15901018869'
result = re.match(r'1\d{9}[0-35689]$', phone)
print(result, result.group())

phone = '029-83145678'
# result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
result = re.match(r'(\d{3,4})-(\d{8})$', phone)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
