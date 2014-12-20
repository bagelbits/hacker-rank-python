#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

case_total = int(raw_input().strip())

for case_num in xrange(case_total):
  greeting = raw_input().strip()
  if re.search('^hi\s(?!d)', greeting, re.IGNORECASE):
    print greeting.strip()
