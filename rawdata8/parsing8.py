# -*- coding:utf-8 -*-
#<!-- 1. 乾為天 乾.元.亨.利.貞. -->


#!/usr/bin/python

import sys
import os
import pickle
import re

#import TCM_allDBinOne
#=== Input File handling area ...

fileNow = open("rawData_08_FamousDr.txt", 'r')
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...

new_file = open("result_08.txt", "w")

yellow = []
blue = []
green = []
grey = []

yellowStr = ""
blueStr = ""
greenStr = ""
greyStr = ""

qCnt = 0
for i, item in enumerate(listNow):

    re_yellow = r"\[name\]\s*(.*)\s*"
    re_green = r"\[dynasty\]\s*(.*)\s*"
    re_blue = r"\[publications\]\s*(.*)\s*"
    re_grey = r"\[note\]\s*(.*)\s*"

    if "龔信《古今醫鑒》是在龔廷賢協助下并加以補充而成的" in item:
        break
    elif(re.findall(re_yellow, item.strip())):
        yellowStr = ""
        blueStr = ""
        greenStr = ""
        greyStr = ""
        
        qCnt += 1
        match = re.search(re_yellow, item)
        yellowStr = match.group(1)
    elif(re.findall(re_blue, item.strip())):
        qCnt += 1
        match = re.search(re_blue, item)
        blueStr = match.group(1)
        
    elif(re.findall(re_grey, item.strip())):
        qCnt += 1
        match = re.search(re_grey, item)
        greyStr = match.group(1)
    elif(re.findall(re_green, item.strip())):
        match = re.search(re_green, item)
        greenStr = match.group(1)
        qCnt += 1

        g = i+1
        pubcount = 0
        notecount = 0
        while g < len(listNow) and "★" not in listNow[g]:
            
            if "[publications]" in listNow[g]:
                match = re.search(re_blue, listNow[g])
                blueStr = "\\n著作: \\n" + match.group(1)
                pubcount += 1
            if "[note]" in listNow[g]:
                match = re.search(re_grey, listNow[g])
                greyStr = "\\n\\n" + match.group(1) + "\\n\\n"
                notecount += 1
            
            g = g+1
        if pubcount == 0:
                print(f"[ERROR]: {yellowStr} missing publications")
        if notecount == 0:
            print(f"[ERROR]: {yellowStr} missing note")
    



        # if qCnt != 4:
        #     print ("[ERROR]: " + yellowStr)

        yellow.append(yellowStr)
        green.append(greenStr)
        blue.append(blueStr)
        grey.append(greyStr)


print("yellow = "+str(len(yellow)))
print("green = "+str(len(green)))
print("blue = "+str(len(blue)))
print("grey = "+str(len(grey)))

# for i in blue:
#     print(i)

new_file.write("[\n")
for i, item in enumerate(yellow):
    tempoutput = f"他所在的時代是{green[i]}{blue[i]}{grey[i]}"
    tempoutput2 = ''.join(tempoutput.split())
    tempoutput3 = tempoutput2.replace("$(\"#db-navi-bar\").append('其它相關項目')", "")
    output = tempoutput3.replace('\"', '\\"')

    new_file.write(f"\t{{\n\t\t\"tag\": \"{yellow[i]}\",\n\t\t\"instruction\": \"請回答問題\",\n\t\t\"input\": \"請介紹一下醫學家{yellow[i]}\",\n\t\t\"output\": \"{output}\"\n\t}}")
    if i != len(yellow) - 1:
        new_file.write(",")
    new_file.write("\n")

new_file.write("]")
    
new_file.close()