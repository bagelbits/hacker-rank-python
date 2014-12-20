#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

test_cases = int(raw_input().strip())

for case_num in range(0, test_cases):
  stones_num = int(raw_input().strip())
  step_a = int(raw_input().strip())
  step_b =  int(raw_input().strip())
  if step_a < step_b:
    step_a, step_b = step_b, step_a
  if step_a == step_b:
    print step_a * (stones_num - 1)
  else:
    print " ".join([str(step_a * x + step_b * (stones_num - x - 1)) for x in xrange(0, stones_num)])