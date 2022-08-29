#!/usr/bin/python
# -*- coding: utf-8; -*-

import a2s

l1 = a2s.players("0.0.0.0", 30815)
l2 = a2s.info("0.0.0.0", 30815)

print(*l1, sep = "\n")
print(*l2, sep = "\n")
