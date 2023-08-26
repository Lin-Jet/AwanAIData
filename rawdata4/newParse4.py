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

new_file = open("new_result_04.txt", "w")

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


new_file.write("[\n")
for i, item in enumerate(herb_pair):

    json1 = f"\t{{\n\t\t\"instruction\": \"說明{herb_pair[i]}這個藥對的功能\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb_pair[i]}這個藥對的功能是{efficacy[i]}。\"\n\t}},\n"
    json2 = f"\t{{\n\t\t\"instruction\": \"說明{herb_pair[i]}這個藥對的應用\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb_pair[i]}這個藥對的應用是{usage[i]}。\"\n\t}},\n"
    json3 = f"\t{{\n\t\t\"instruction\": \"說明{herb_pair[i]}這個藥對的詳細說明\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb_pair[i]}這個藥對的詳細說明如下:\\n\\t{note[i]}\"\n\t}}"



    finished1 = f"{json1}{json2}{json3}"

    finished2 = finished1.replace("。。", "。")
    finished3 = finished2.replace("。。", "。")


    new_file.write(finished3)

    if i != len(herb_pair) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")

new_file.close()