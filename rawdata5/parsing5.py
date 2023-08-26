# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...

fileNow = open("rawData_05_TCM_pattern_symptom_linking_list.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open("result_05.txt", "w")

pattern = []
main = []
secondary = []
diag_tongue = []
diag_pulse = []

for item in listNow:

    re_pattern = r"\[pattern\]\s*(.*)\s*"
    re_main = r"\[main\]\s*(.*)\s*"
    re_secondary = r"\[secondary\]\s*(.*)\s*"
    re_diag_tongue = r"\[diag_tongue\]\s*(.*)\s*"
    re_diag_pulse = r"\[diag_pulse\]\s*(.*)\s*"

    if "#" in item:
        pass
    elif "[cate] 其它" in item:
        break
    elif(re.findall(re_pattern, item.strip())):
        match = re.search(re_pattern, item)
        pattern.append(match.group(1))
    elif(re.findall(re_main, item.strip())):
        match = re.search(re_main, item)
        filteredmatch = re.sub("\+", "、", match.group(1))
        main.append(filteredmatch)
    elif(re.findall(re_secondary, item.strip())):
        match = re.search(re_secondary, item)
        filteredmatch = re.sub("\+", "、", match.group(1))
        secondary.append(filteredmatch)
    elif(re.findall(re_diag_tongue, item.strip())):
        match = re.search(re_diag_tongue, item)
        diag_tongue.append(match.group(1))
    elif(re.findall(re_diag_pulse, item.strip())):
        match = re.search(re_diag_pulse, item)
        diag_pulse.append(match.group(1))

for i, item in enumerate(pattern):
    new_file.write(f"""[Q]什麼是{pattern[i]}?
[TAG]{pattern[i]}
[A]{pattern[i]}是一種中醫證型，有{pattern[i]}的人大多有以下的症狀: {main[i]}。也有可能有{secondary[i]}等症狀。其脈象是{diag_tongue[i]}，脈象是{diag_pulse[i]}。\n\n
""")

    
new_file.close()