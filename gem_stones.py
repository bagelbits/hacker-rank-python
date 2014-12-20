#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

rock_total = int(raw_input().strip())

gem_elements = set(raw_input().strip())

for rock_num in range(1, rock_total):
  current_rock = set(raw_input().strip())
  gem_elements = gem_elements.intersection(current_rock)

print len(gem_elements)