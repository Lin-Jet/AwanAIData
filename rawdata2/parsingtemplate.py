# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...

fileNow = open("rawData_02_formulaNote-繁體.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open("rStemp.txt", "w")

name = []
blue = []
grey = []
brown = []
lightblue = []
pink = []
teal = []


for item in listNow:
    re_name = r"^\[方名\]\s*(?P<name>.*)"
    if (re.findall(re_name, item.strip())):
        match = re.search(re_name, item)
        name.append(match.group("name"))

    re_blue = r"^\[出處\]\s*(?P<blue>.*)"
    if (re.findall(re_blue, item.strip())):
        match = re.search(re_blue, item)
        blue.append(match.group("blue"))
    
    re_grey = r"^[方解]\s+(\-\-(.*))*"
    if (re.findall(re_grey, item.strip())):
        match = re.search(re_grey, item)
        # for i, item in enumerate(match):
            # greys = []
            # greys.append(item.group(grey))
            # grey.append("「" + greys[i] +"」" + "\n")
        grey.append(match.group("grey"))

    re_brown = r"^\[原文劑量\]\s*(?P<brown>.*)"
    if (re.findall(re_brown, item.strip())):
        match = re.search(re_brown, item)
        brown.append(match.group("brown"))

    re_lightblue = r"^\[用法\]\s*(?P<lightblue>.*)"
    if (re.findall(re_lightblue, item.strip())):
        match = re.search(re_lightblue, item)
        lightblue.append(match.group("lightblue"))

    re_pink = r"^\[功用\]\s*(?P<pink>.*)"
    if (re.findall(re_pink, item.strip())):
        match = re.search(re_pink, item)
        pink.append(match.group("pink"))
    
    re_teal = r"^\[適用症狀\]\s*(?P<teal>.*)"
    if (re.findall(re_teal, item.strip())):
        match = re.search(re_teal, item)
        teal.append(match.group("teal"))


for i, item in enumerate(name):
    new_file.write ("[Q]什麼是" + name[i] + "?\n" )
    new_file.write ("[TAG] " + name[i] + '\n')
    new_file.write("[A] "+ name[i] + "是出自" + blue[i] + "的方劑，書中原文提到:" + '\n')
    new_file.write("「" + grey[i] +"」" + "\n" + "「" + grey[i+1] +"」"+ '\n')
                
new_file.close()
