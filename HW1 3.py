# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:48:21 2020

@author: DELL
"""

import re

with open('blocklist.xml') as f:
    c = f.read()

#Q3-1
pattern1 = re.compile(r".*?blockID=.*?[ig]\d{3,4}.*?>")
content1 = re.findall(pattern1, c)
print(content1)

#Q3-2
pattern2 = re.compile(r".*?id=\"[a-zA-Z0-9._%+-]{1,10}@[a-zA-Z0-9]{1,10}[.][a-zA-Z]{1,10}.*?>")
content2 = re.findall(pattern2, c)
print(content2)