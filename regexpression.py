# text = '125map'
#
# cont_map = 'map' in text
# print(cont_map)
#
# cont_map = text.count('map')
# print(cont_map)

import re

text = 'in map i see forest. But i dont see this forest irl. Map is wrong. Mapping'
# match = re.findall('map', text)
# print(match)

# match = re.findall('[mM]ap', text)
# print(match)

# match = re.findall('[mM]ap$', text)
# print(match)

# match = re.findall(r'\Bpp\B', text)
# print(match)

# match = re.findall('m.p', text)
# print(match)

match = re.findall('[mM]ap', text)
print(match)
