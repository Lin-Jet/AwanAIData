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

new_file = open("result_07.txt", "w")

yellow = []
blue = []
blue1 = []
blue2 = []
blue3 = []
blue1Now = ""
blue2Now = ""
blue3Now = ""


for item in listNow:

    re_yellow = r"\[名称\]\s*(.*)\s*"
    re_blue1 = r"\[孫培榮、周左宇\]\s*(.*)\s*"
    re_blue2 = r"\[倪海廈\]\s*(.*)\s*"
    re_blue3 = r"\[楊維傑\]\s*(.*)\s*"
    
    if "THE END" in item:
        break
    elif(re.findall(re_blue1, item.strip())):
        match = re.search(re_blue1, item)
        apQ = match.group(1).split("+")
        newQ = []
        [newQ.append(item) for item in apQ if item not in newQ]
        tempStr = ""
        for i in newQ:
            tempStr += f"{i}、"
        if apQ == "":
            blue1Now = ""
        else:
            blue1Now = tempStr
    elif(re.findall(re_blue2, item.strip())):
        match = re.search(re_blue2, item)
        apQ = match.group(1).split("+")
        newQ = []
        [newQ.append(item) for item in apQ if item not in newQ]
        tempStr = ""
        for i in newQ:
            tempStr += f"{i}、"
        if apQ == "":
            blue2Now = ""
        else:
            blue2Now = tempStr
    elif(re.findall(re_blue3, item.strip())):
        match = re.search(re_blue3, item)
        apQ = match.group(1).split("+")
        newQ = []
        [newQ.append(item) for item in apQ if item not in newQ]
        tempStr = ""
        for i in newQ:
            tempStr += f"{i}、"
        if apQ == "":
            blue3Now = ""
        else:
            blue3Now = tempStr
    elif(re.findall(re_yellow, item.strip())):
        match = re.search(re_yellow, item)
        yellow.append(match.group(1))

        bluetotal = []
        bluetotalStr = ""
        bluetotal.append(blue1Now)
        bluetotal.append(blue2Now)
        bluetotal.append(blue3Now)
        
        for i in bluetotal:
            bluetotalStr += f"{i}"
        if bluetotalStr.endswith("、"):
            bluetotalStr = bluetotalStr[:-1] + "。"
        blue.append(bluetotalStr)



print("yellow = "+str(len(yellow)))
print("blue = "+str(len(blue)))
print("blue1 = "+str(len(blue1)))
print("blue2 = "+str(len(blue2)))
print("blue3 = "+str(len(blue3)))

for i in blue:
    print(i)

for i, item in enumerate(yellow):
    new_file.write(f"""[Q]有哪些穴位可以治療{yellow[i]}?
[TAG]{yellow[i]}
[A]治療{yellow[i]}的相關穴位有{blue[i]}\n\n""")

    
new_file.close()