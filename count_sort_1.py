#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

case_total = int(raw_input().strip())

count_list = [0] * 100

number_list = [int(x.strip()) for x in raw_input().split(' ')]
for x in number_list:
  count_list[x] += 1

print " ".join(map(str, count_list))