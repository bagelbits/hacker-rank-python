#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

case_total = int(raw_input().strip())

for case_num in xrange(case_total):
  id_string = raw_input().strip()

  id_string = re.sub('[a-z]{0,3}\d{2,8}[A-Z]{3,}', '', id_string)

  if id_string:
    print "INVALID"
  else:
    print "VALID"