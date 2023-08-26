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

new_file = open("result_02.txt", "w")

fNameQ = []
sourceQ = []
orgQ = []
contentQ = []
makeQ = []
funcQ = []
usageQ = []
noteQ = []

fNameNow = ""
sourceNow = ""
orgNow = ""
contentNow = ""
makeNow = ""
funcNow = ""
usageNow = ""
noteNow = ""

qCnt = 0
for i, item in enumerate(listNow):
    regex = r"\[方名\]\s*(\S+)"
    regex2 = r"\[出處\]\s*(\S+)"
    regex3a = r"\[原文\]\s*(\S+)"
    regex3 = r"\[原文\]"    
    regex4 = r"\[原文劑量\]\s*(\S+)"        
    regex5 = r"\[用法\]\s*(.*)"
    regex6 = r"\[功用\]\s*(\S+)"        
    regex7 = r"\[適用症狀\]\s*(\S+)"
    regex8 = r"\[方解\]"
    if "#" in item:
        pass
    elif (re.findall(regex, item.strip())):
        fNameNow = ""
        sourceNow = ""
        orgNow = ""
        contentNow = ""
        makeNow = ""
        funcNow = ""
        usageNow = ""
        noteNow = ""
        
        qCnt += 1
        match = re.search(regex, item)
        fNameNow = match.group(1)
    elif (re.findall(regex2, item.strip())):
        qCnt += 1
        match = re.search(regex2, item)
        sourceNow = match.group(1)
    elif (re.findall(regex3a, item.strip())):
        qCnt += 1
        match = re.search(regex3a, item)
        orgNow = "，書中原文提到: "+match.group(1)
    elif (re.findall(regex3, item.strip())):
        qCnt += 1
        g = i+1
        tempStr = ""
        while "[原文劑量]" not in listNow[g]:
            tempStr += listNow[g]
            g = g+1
        if tempStr == "":            
            orgNow = ""
        else:            
            orgNow = "，書中原文提到: \n"+tempStr
    elif (re.findall(regex4, item.strip())):
        qCnt += 1
        match = re.search(regex4, item)
        contentNow = match.group(1)
    elif (re.findall(regex5, item.strip())):
        qCnt += 1
        match = re.search(regex5, item)
        makeNow = match.group(1)
    elif (re.findall(regex6, item.strip())):
        qCnt += 1
        match = re.search(regex6, item)
        funcNow = match.group(1)
    elif (re.findall(regex7, item.strip())):
        qCnt += 1
        match = re.search(regex7, item)
        usageNow = match.group(1)
    elif (re.findall(regex8, item.strip())):
        qCnt += 1
        g = i+1
        tempStr = ""
        while "[自動調整劑量]" not in listNow[g]:
            tempStr += listNow[g]
            g = g+1
        noteNow = tempStr
        if qCnt != 8:
            print ("[ERROR]: "+fNameNow)

        fNameQ.append(fNameNow)
        sourceQ.append(sourceNow)
        orgQ.append(orgNow)
        contentQ.append(contentNow)
        makeQ.append(makeNow)
        funcQ.append(funcNow)
        usageQ.append(usageNow)
        noteQ.append(noteNow)


            
    elif "END" in item:
        break


print("fNameQ = "+str(len(fNameQ)))
print("sourceQ = "+str(len(sourceQ)))
print("orgQ = "+str(len(orgQ)))
print("contentQ = "+str(len(contentQ)))
print("makeQ = "+str(len(makeQ)))
print("funcQ = "+str(len(funcQ)))
print("usageQ = "+str(len(usageQ)))
print("noteQ = "+str(len(noteQ)))

for i, item in enumerate(fNameQ):
    tempStr = f"""[Q]什麼是{fNameQ[i]}?
[TAG] {fNameQ[i]}
[A] {fNameQ[i]}是出自{sourceQ[i]}的方劑{orgQ[i]}
{fNameQ[i]}的組成是 {contentQ[i]} 
{fNameQ[i]}的功用是{funcQ[i]}可應用在{usageQ[i]}{makeQ[i]} 
{noteQ[i]} 
"""
    new_file.write(tempStr.replace("。。", ""))


    
new_file.close()