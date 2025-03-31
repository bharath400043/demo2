import re
num = "1234567890"
print('(%s) %s-%s' % tuple(re.findall(r'\d{6}$|\d{2}', num)))
