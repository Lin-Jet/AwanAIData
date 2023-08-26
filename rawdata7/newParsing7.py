# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...

fileNow = open("rawData_07_classic_symptom.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open("new_result_07.txt", "w")

yellow = []
blue = []
tempStr = ""


for i, item in enumerate(listNow):

    re_yellow = r"\[名称\]\s*(.*)\s*"
    re_pass = r"\[证型\]"
    re_blue = r"\[.*\]\s*(.*)\s*"
    
    if "THE END" in item:
        break
    elif(re.findall(re_yellow, item.strip())):
        match = re.search(re_yellow, item)
        yellow.append(match.group(1))
        tempStr = tempStr[:-1] + '。'
        blue.append(tempStr)
        tempStr = ""
    elif (re.findall(re_pass, item.strip())):
        pass
    elif (re.findall(re_blue, item.strip())):
        match = re.search(re_blue, item)
        tempStr += match.group(1).replace('+', '、') + '、'
blue.append(tempStr)
blue.pop(0)

   



print("yellow = "+str(len(yellow)))
print("blue = "+str(len(blue)))


new_file.write("[\n")
for i, item in enumerate(yellow):

    json1 = f"\t{{\n\t\t\"instruction\": \"有哪些穴位可以治療{yellow[i]}?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"治療{yellow[i]}的相關穴位有{blue[i]}\"\n\t}}"
    
    finished1 = f"{json1}"

    finished2 = finished1.replace("。。", "。")
    finished3 = finished2.replace("。。", "。")
    finished4 = finished3.replace(" 。", "。")
    finished5 = finished4.replace("、\"", "。\"")

    new_file.write(finished5)

    if i != len(yellow) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")

new_file.close()