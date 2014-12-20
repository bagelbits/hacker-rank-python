flowers, friends = [int(x) for x in raw_input().split()]
prices = reversed(sorted([int(x) for x in raw_input().split()]))

money_spent = 0
purchased = [0]*friends
j = 0
for flower in prices:

  if j == friends:
    j = 0
  money_spent += (purchased[j] + 1)*flower
  purchased[j] += 1
  j += 1
print money_spent