cases = int(raw_input())
results = []
for x in xrange(cases):
  members = int(raw_input())
  results.append(str(sum(xrange(members))))
print "\n".join(results)