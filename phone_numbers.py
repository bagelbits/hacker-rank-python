import re

cases = int(raw_input())

results = []
for x in xrange(cases):
  phone_string = raw_input()
  match = re.search(r"^(\d+)[- ](\d+)[- ](\d+)", phone_string)
  if match:
    results.append("CountryCode=%s,LocalAreaCode=%s,Number=%s" % (match.group(1), match.group(2), match.group(3)))
print "\n".join(results)