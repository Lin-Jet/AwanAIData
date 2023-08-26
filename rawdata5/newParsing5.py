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

new_file = open("new_result_05.txt", "w")

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


new_file.write("[\n")
for i, item in enumerate(pattern):

    json1 = f"\t{{\n\t\t\"instruction\": \"什麼是{pattern[i]}?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{pattern[i]}是一種中醫證型，有{pattern[i]}的人大多有以下的症狀:\\n\\t{main[i]}。\\n{pattern[i]}也有可能有{secondary[i]}等症狀。\"\n\t}},\n"
    json2 = f"\t{{\n\t\t\"instruction\": \"什麼是{pattern[i]}的舌象?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{pattern[i]}其舌象是{diag_tongue[i]}。\"\n\t}},\n"
    json3 = f"\t{{\n\t\t\"instruction\": \"什麼是{pattern[i]}的脈象?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{pattern[i]}其脈象是{diag_pulse[i]}。\"\n\t}}"



    finished1 = f"{json1}{json2}{json3}"

    finished2 = finished1.replace("。。", "。")
    finished3 = finished2.replace("。。", "。")
    finished4 = finished3.replace(" 。", "。")

    new_file.write(finished4)

    if i != len(pattern) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")

new_file.close()
