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

new_file = open("new_result_02.txt", "w")

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
        if (match.group(1) == ""):
            print(f"{fNameNow} 's fnamenow is empty")
    elif (re.findall(regex2, item.strip())):
        qCnt += 1
        match = re.search(regex2, item)
        sourceNow = match.group(1)
        if (match.group(1) == ""):
            print(f"{fNameNow} 's sourceNow is empty")
    elif (re.findall(regex3a, item.strip())):
        qCnt += 1
        match = re.search(regex3a, item)
        # orgNow = "，書中原文提到: "+match.group(1)
        orgNow = match.group(1)
        if (match.group(1) == ""):
            print(f"{fNameNow} 's orgNow is empty")
    elif (re.findall(regex3, item.strip())):
        qCnt += 1
        g = i+1
        tempStr = ""
        while "[原文劑量]" not in listNow[g]:
            tempStr += listNow[g].strip()
            g = g+1
        if tempStr == "":            
            orgNow = ""
            print(f"{fNameNow}'s orgNow is empty")
        else:            
            # orgNow = "，書中原文提到: \n"+tempStr
            orgNow = tempStr.strip()
            if (tempStr == ""):
                print(f"{fNameNow} 's orgNow22222 is empty")
    elif (re.findall(regex4, item.strip())):
        qCnt += 1
        match = re.search(regex4, item)
        contentNow = match.group(1)
        if (match.group(1) == ""):
            print(f"{fNameNow} 's contentNow is empty")
    elif (re.findall(regex5, item.strip())):
        qCnt += 1
        match = re.search(regex5, item)
        makeNow = match.group(1)
        if (match.group(1) == ""):
            print(f"{fNameNow} 's makeNow is empty")
    elif (re.findall(regex6, item.strip())):
        qCnt += 1
        match = re.search(regex6, item)
        funcNow = match.group(1)
        if (match.group(1) == ""):
            print(f"{fNameNow} 's funcNow is empty")
    elif (re.findall(regex7, item.strip())):
        qCnt += 1
        match = re.search(regex7, item)
        usageNow = match.group(1)
        if (match.group(1) == ""):
            print(f"{fNameNow} 's usageNow is empty")
    elif (re.findall(regex8, item.strip())):
        qCnt += 1
        g = i+1
        tempStr = ""
        while "[自動調整劑量]" not in listNow[g]:
            tempStr += listNow[g].strip()
            g = g+1
        noteNow = tempStr.strip()
        if (tempStr == ""):
            print(f"{fNameNow} 's noteNow is empty")

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

#new org filter
regorgs = r"(?<!\\n\\t)--"
for i, item in enumerate(orgQ):
    if re.findall(regorgs, item.strip()):
        new_item = re.sub(regorgs, r"\\n\\t--", item)
        orgQ[i] = new_item

#new note filter
regnotes = r"(?<!\\n\\t)--"
for i, item in enumerate(noteQ):
    if re.findall(regnotes, item.strip()):
        new_item = re.sub(regnotes, r"\\n\\t--", item)
        noteQ[i] = new_item


#filter the orgs
# regorgs = r"(\s*\-\-)"
# regorgs2 = r"('\-\-)"
# regorgs3 = r"\\n'"
# regorgs4 = r"\)\s+"

# temp = []
# for i, item in enumerate(orgQ):
#     if re.findall(regorgs, item.strip()):
#         new_item = re.sub(regorgs, "\\n\\t--", item)
#         representation = repr(new_item)
#         temp.append(representation)
#     else:
#         temp.append(item)
# orgQ = temp

# for i, item in enumerate(orgQ):
#     if re.findall(regorgs2, item.strip()):
#         orgQ[i] = re.sub(regorgs2, "--", item)
# for i, item in enumerate(orgQ):       
#     if re.findall(regorgs3, item.strip()):
#         orgQ[i] = re.sub(regorgs3, "", item)
# for i, item in enumerate(orgQ):       
#     if re.findall(regorgs4, item.strip()):
#         orgQ[i] = re.sub(regorgs4, ")", item)
#     orgQ[i].strip()

#filter the notes
# regnotes = r"(\s*\-\-)"
# regnotes1 = r"(\s+)"
# regnotes2 = r"('\-\-)"
# regnotes3 = r"\\n\'"
# temp = []
# for i, item in enumerate(noteQ):

#     if re.findall(regnotes, item.strip()):
#         new_item = re.sub(regnotes, "\\n\\t--", item)
#         representation = repr(new_item)
#         temp.append(representation)
#     else:
#         temp.append(item)
# noteQ = temp
# for i, item in enumerate(noteQ):
#     if re.findall(regnotes1, item.strip()):
#         noteQ[i] = re.sub(regnotes1, "", item)
        
# for i, item in enumerate(noteQ):
#     if re.findall(regnotes2, item.strip()):
#         noteQ[i] = re.sub(regnotes2, "--", item)
# for i, item in enumerate(noteQ):       
#     if re.findall(regnotes3, item.strip()):
#         noteQ[i] = re.sub(regnotes3, "", item)
#     noteQ[i].strip()
    
    

print("orgQ after = "+str(len(orgQ)))
print("noteQ after = "+str(len(orgQ)))

new_file.write("[\n")
for i, item in enumerate(fNameQ):
    finished1 = f"\t{{\n\t\t\"instruction\": \"什麼是{fNameQ[i]}的出處?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{fNameQ[i]}是出自{sourceQ[i]}論的方劑。\"\n\t}},\n\t{{\n\t\t\"instruction\": \"什麼是{fNameQ[i]}的原文說明?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{fNameQ[i]}的原文說明如下:{orgQ[i]}\"\n\t}},\n\t{{\n\t\t\"instruction\": \"什麼是{fNameQ[i]}的組成?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{fNameQ[i]}的組成是{contentQ[i]}。\"\n\t}},\n\t{{\n\t\t\"instruction\": \"什麼是{fNameQ[i]}的功用?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{fNameQ[i]}的功用是{funcQ[i]}。\"\n\t}},\n\t{{\n\t\t\"instruction\": \"什麼是{fNameQ[i]}的適用症狀?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{fNameQ[i]}可應用在{usageQ[i]}。\"\n\t}},\n\t{{\n\t\t\"instruction\": \"什麼是{fNameQ[i]}的使用方法?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{fNameQ[i]}的使用方法是:\\n\\t{makeQ[i]}\"\n\t}},\n\t{{\n\t\t\"instruction\": \"什麼是{fNameQ[i]}的方解(方劑說明)?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{fNameQ[i]}的方解如下:{noteQ[i]}\"\n\t}}"

    finished2 = finished1.replace("。。", "。")
    finished3 = finished2.replace("。。", "。")

    



    new_file.write(finished3)

    if i != len(fNameQ) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")

new_file.close()