#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

lane_length, case_total = [int(x.strip()) for x in raw_input().split(' ')]
lane_widths = [int(x.strip()) for x in raw_input().split(' ') if int(x.strip()) < 4 and int(x.strip()) > 0][:lane_length]

output_cases = []

for case_num in range(0, case_total):
  start, end = [int(x.strip()) for x in raw_input().split(' ')]

  min_width = 3
  for x in lane_widths[start:end + 1]:
    if x < min_width:
      min_width = x

  output_cases.append(min_width)

for x in output_cases:
  print x