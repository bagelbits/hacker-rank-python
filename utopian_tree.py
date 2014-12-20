#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

case_total = int(raw_input().strip())

output_cases = []

for case_num in range(0, case_total):
  current_case = int(raw_input().strip())

  tree_height = 1
  for cycle in range(1, current_case + 1):
    if cycle % 2 == 0:
      tree_height += 1
    else:
      tree_height *= 2

  output_cases.append(tree_height)


for x in output_cases:
  print x