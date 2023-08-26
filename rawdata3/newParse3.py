# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...

fileNow = open("rawData_03_TCM_Herb_List.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open("new_result_03.txt", "w")

herb = []
attribute = []
meridian = []
efficacy = []
usage = []
main = []
dose_warning = []

herbStr = ""
attributeStr = ""
meridianStr = ""
efficacyStr = ""
usageStr = ""
mainStr = ""
dose_warningStr = ""

# truetestcnt = 0
# nonetestcnt = 0
# noneintestcnt = 0
for i, item in enumerate(listNow):
    re_herb = r"\[herb\]\s*(.*)\s*"
    re_attribute = r"\[attribute\]\s*(.*)\s*"
    re_meridian = r"\[Meridian\]\s*(.*)\s*"
    re_efficacy = r"\[efficacy\]\s*(.*)\s*"
    re_usage = r"\[usage\]\s*(.*)\s*"
    re_main = r"\[main\]\s*(.*)\s*"
    # re_dose_warning_none = r"\[dose_warning\]\n"
    re_dose_warning_true = r"\[dose_warning\](20:)?\s*(.*)\s*"

    if '#' in item:
        pass
    elif (re.findall(re_herb, item.strip())):
        herbStr = ""
        attributeStr = ""
        meridianStr = ""
        efficacyStr = ""
        usageStr = ""
        mainStr = ""
        dose_warningStr = ""

        match = re.search(re_herb, item)
        herbStr = match.group(1)
    elif (re.findall(re_attribute, item.strip())):
        match = re.search(re_attribute, item)
        attributeStr = match.group(1)
    elif (re.findall(re_meridian, item.strip())):
        match = re.search(re_meridian, item)
        meridianStr =match.group(1)
    elif (re.findall(re_efficacy, item.strip())):
        match = re.search(re_efficacy, item)
        efficacyStr = match.group(1)
    elif (re.findall(re_usage, item.strip())):
        match = re.search(re_usage, item)
        usageStr = match.group(1)
    elif (re.findall(re_dose_warning_true, item.strip())):   
        match = re.search(re_dose_warning_true, item)
        dose_warning_text = match.group(2)
        if dose_warning_text == "":
            dose_warningStr = ""
            # noneintestcnt += 1
        else:
            dose_warningStr = re.sub(r"\+", "、", dose_warning_text)
            dose_warningStr = f"{herbStr}不適用的情況有: {dose_warningStr}"
            # truetestcnt += 1

        dose_warning.append(dose_warningStr)
    elif (re.findall(re_main, item.strip())):
        match = re.search(re_main, item)
        mainStr = match.group(1)

        herb.append(herbStr)
        attribute.append(attributeStr)
        meridian.append(meridianStr)
        efficacy.append(efficacyStr)
        usage.append(usageStr)
        main.append(mainStr)
        # print(dose_warningStr + "hi")
        
        # newQ = []
        # [newQ.append(item) for item in dose_warning if item not in newQ]
        # print(newQ)

            

# print("herb = "+str(len(herb)))
# print("attribute = "+str(len(attribute)))
# print("meridian = "+str(len(meridian)))
# print("efficacy = "+str(len(efficacy)))
# print("usage = "+str(len(usage)))
# print("main = "+str(len(main)))
# print("dose_warning = "+str(len(dose_warning)))
# print("true: ", truetestcnt)
# print("none: ", nonetestcnt)
# print("nonein: ", noneintestcnt)


new_file.write("[\n")
for i, item in enumerate(herb):

    json1 = f"\t{{\n\t\t\"instruction\": \"什麼是{herb[i]}的性味?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb[i]}的性味是{attribute[i]}。\"\n\t}},\n"
    json2 = f"\t{{\n\t\t\"instruction\": \"什麼是{herb[i]}的歸經?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb[i]}的歸經是{meridian[i]}。\"\n\t}},\n"
    json3 = f"\t{{\n\t\t\"instruction\": \"什麼是{herb[i]}的功效?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb[i]}的功效是{efficacy[i]}。\"\n\t}},\n"
    json4 = f"\t{{\n\t\t\"instruction\": \"什麼是{herb[i]}的應用?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb[i]}的應用為{usage[i]}。\"\n\t}},\n"
    json5 = f"\t{{\n\t\t\"instruction\": \"什麼是{herb[i]}的不適用、禁忌的事項?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{herb[i]}不適用的情況有: {dose_warning[i]}。\"\n\t}}"
    


    finished1 = f"{json1}{json2}{json3}{json4}{json5}"

    finished2 = finished1.replace("。。", "。")
    finished3 = finished2.replace("。。", "。")


    new_file.write(finished3)

    if i != len(herb) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")

new_file.close()