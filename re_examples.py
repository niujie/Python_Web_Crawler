import re

match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

print(type(match))
print(match.string)
print(match.re)
print(match.pos)
print(match.endpos)
print(match.start())
print(match.end())
print(match.span())
print(match.string[match.start():match.end()])
print(match.group)

match = re.match(r'[1-9]\d{5}', '100081 BIT')
if match:
    print(match.group(0))

ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)

print(re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084'))

print(re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1))

for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))

print(re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084'))

match = re.search(r'PY.*N', 'PYANBNCNDN')
print(match.group(0))

match = re.search(r'PY.*?N', 'PYANBNCNDN')
print(match.group(0))