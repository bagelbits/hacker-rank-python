count_list = [0]*100
sort_list = [0]*100
for x in xrange(int(raw_input())):
  count_list[int(raw_input().split(" ")[0])] += 1
pos = 0
count = 0
for x in count_list:
  count += x
  sort_list[pos] = count
  pos += 1
print " ".join(map(str, sort_list))