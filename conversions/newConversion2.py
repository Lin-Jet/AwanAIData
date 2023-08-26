# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...


result_file = new_result_02

name_converted = new_done_02

fileNow = open(f"{result_file}.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open(f"{name_converted}.txt", "w")


tag = []
instruction = "請回答問題"
input = []
output = []

for i, item in enumerate(listNow):
    re_double = r"。。"
    
    
    if (re.findall(re_tag, item.strip())):
        match = re.search(re_tag, item)
        tag.append(match.group(1))
    elif (re.findall(re_input, item.strip())):
        match = re.search(re_input, item)
        input.append(match.group(1))
    elif (re.findall(re_output, item.strip())):
        match = re.search(re_output, item)
        unfilterednums1 = match.group(1)

        numperiodfilter = r"(\d)。"
        unfilterednums = re.sub(numperiodfilter, r"\1\.", unfilterednums1)


        # re_filter_nums = r"(\d+\.\s*)(.*?)(\s|。)(?=\d+\.\s*|$)"
        # re_filter_nums = r"(\d+\.\s*)(.*?\s?)(?=\s\d+\.\s*|$)"
        # re_filter_nums = r"(\d+\.\s*)(.*?)(?=\s\d+\.\s*|\d+。|$)"
        # re_filter_nums = r"(\d+)(\.\s*)(.*?)(?=\s\d+\.\s*|\d+。|\d+\.|$)"
        re_filter_nums = r"(\d+)(\.\s*)(.*?[^0-9])(?=\s\d+\.\s*|\d+。|\d+\.|$)"

        if (result_file != "result_01"):
            filterednums = unfilterednums1
        elif (result_file != "result_06"):
            filterednums = unfilterednums1
        else:
            filterednums = re.sub(re_filter_nums, r"\\n\\t\1\2\3 ", unfilterednums, 0)
        

        g = i+1
        tempStr = ""
        while g < len(listNow) and "[Q]" not in listNow[g]:
            tempStr += listNow[g]
            g = g+1

        tempStr = re.sub(r"\s", "", tempStr) 

        filtereddash = tempStr.replace("--", "\\n\\t--")
        # re_filter_dash = r"\-\-\s*(.*)(?=\-\-\s*(.*)|$)"
        # filtereddash = re.sub(re_filter_dash, r"\\n\\t\1", unfiltereddash, 0)

      
        
        almost_filtered_1 = filterednums + filtereddash

        almost_filtered_2 = almost_filtered_1.replace("。，", "。")

        almost_filtered_3 = almost_filtered_2.replace("。。", "。")
        
        almost_filtered_4 = almost_filtered_3.replace(" 。", "。")

        filtered = almost_filtered_4.replace(" ，", "，")

        output.append(filtered)

print("tag = "+str(len(tag)))
print("input = "+str(len(input)))
print("output = "+str(len(output)))

new_file.write("[\n")
for i, item in enumerate(tag):
    new_file.write(f"\t{{\n\t\t\"tag\": \"{tag[i]}\",\n\t\t\"instruction\": \"請回答問題\",\n\t\t\"input\": \"{input[i]}\",\n\t\t\"output\": \"{output[i]}\"\n\t}}")
    if i != len(tag) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")

new_file.close()