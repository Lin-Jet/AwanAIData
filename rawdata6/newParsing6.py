# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...

fileNow = open("rawData_06_classic_point.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open("new_result_06.txt", "w")

red = []
yellow = []
green = []
blue = []
pink = []
grey = []

redNow = ""
greenNow = ""
blueNow = ""

for item in listNow:

    re_red = r"\[经络\]\s*(.*)\s*"

    re_yellow = r"\[穴位\]\s*(.*)\s*"
    re_green = r"\[编码\]\s*(.*)\s*"
    re_blue = r"\[症状\]\s*(.*)\s*"
    re_pink = r"\[位置\]\s*(.*)\s*"
    re_grey = r"\[方法\]\s*(.*)\s*"

    

    if(re.findall(re_red, item.strip())):
        redNow = ""
        greenNow = ""
        blueNow = ""

        match = re.search(re_red, item)
        tempStr = match.group(1)
        if tempStr == "":
            redNow = ""
        else:
            redNow = match.group(1)
    elif(re.findall(re_yellow, item.strip())):
        match = re.search(re_yellow, item)
        yellow.append(match.group(1))
        yellow_blue_helper = match.group(1)
    elif(re.findall(re_green, item.strip())):
        greenNow = ""
        match = re.search(re_green, item)
        tempStr = match.group(1)
        if tempStr == "":
            greenNow = "。"
        else:
            greenNow = f"，其國際針灸代碼是{match.group(1)}。"
    elif(re.findall(re_blue, item.strip())):
        blueNow = ""
        match = re.search(re_blue, item)
        tempStr = match.group(1).replace('+', '、')
        if tempStr == "":
            blueNow = ""
        else:
            # blueNow = f"{yellow_blue_helper}可用來治療的症狀有: {tempStr}。"
            blueNow = tempStr + "。"
    elif(re.findall(re_pink, item.strip())):
        match = re.search(re_pink, item)
        pink.append(match.group(1))
    elif(re.findall(re_grey, item.strip())):
        match = re.search(re_grey, item)
        grey.append(match.group(1))
        red.append(redNow)
        green.append(greenNow)
        blue.append(blueNow)


print("red = "+str(len(red)))
print("yellow = "+str(len(yellow)))
print("green = "+str(len(green)))
print("blue = "+str(len(blue)))
print("pink = "+str(len(pink)))
print("grey = "+str(len(grey)))



new_file.write("[\n")
for i, item in enumerate(red):

    json1 = f"\t{{\n\t\t\"instruction\": \"{yellow[i]}這個穴位是哪一個經絡的穴位?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{yellow[i]}是{red[i]}的穴位。\"\n\t}},\n"
    json2 = f"\t{{\n\t\t\"instruction\": \"{yellow[i]}這個穴位的國際針灸代碼是什麼?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"其國際針灸代碼是{green[i]}。\"\n\t}},\n"
    json3 = f"\t{{\n\t\t\"instruction\": \"說明{yellow[i]}這個穴位可以治療的症狀\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{yellow[i]}可用來治療的症狀有:\\n\\t{blue[i]}。\"\n\t}}"
    json4 = f"\t{{\n\t\t\"instruction\": \"{yellow[i]}這個穴位的位置在哪裡?\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{yellow[i]}的位置是{pink[i]}。\"\n\t}}"
    json5 = f"\t{{\n\t\t\"instruction\": \"說明{yellow[i]}這個穴位的針刺方法、灸法\",\n\t\t\"input\": \"\",\n\t\t\"output\": \"{yellow[i]}的針刺方法為{grey[i]}。\"\n\t}}"



    finished1 = f"{json1}{json2}{json3}{json4}{json5}"

    finished2 = finished1.replace("。。", "。")
    finished3 = finished2.replace("。。", "。")
    finished4 = finished3.replace(" 。", "。")

    new_file.write(finished4)

    if i != len(red) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")

new_file.close()
