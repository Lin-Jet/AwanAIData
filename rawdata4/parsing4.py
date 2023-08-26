# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...

fileNow = open("rawData_04_TCM_herbPair_list.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open("result_04.txt", "w")

herb_pair = []
efficacy = []
usage = []
note = []

for item in listNow:

    re_herb_pair = r"\[herb pair\](.*)"
    re_efficacy = r"\[efficacy\](.*)"
    re_usage = r"\[usage\](.*)"
    re_note = r"\[note\](.*)"

    if "#" in item:
        pass
    elif "# ========= 以下為線性智能加減" in item:
        break
    elif(re.findall(re_herb_pair, item.strip())):
        match = re.search(re_herb_pair, item)
        herb_pair.append(match.group(1))
    elif(re.findall(re_efficacy, item.strip())):
        match = re.search(re_efficacy, item)
        efficacy.append(match.group(1))
    elif(re.findall(re_usage, item.strip())):
        match = re.search(re_usage, item)
        usage.append(match.group(1))
    elif(re.findall(re_note, item.strip())):
        match = re.search(re_note, item)
        note.append(match.group(1))

for i, item in enumerate(herb_pair):
    new_file.write(f"""[Q]說明「{herb_pair[i]}」這個藥對
[TAG]{herb_pair[i]}
[A]{herb_pair[i]}這個藥對的功能是{efficacy[i]}其應用是{usage[i]} {note[i]}\n\n
""")


    
new_file.close()