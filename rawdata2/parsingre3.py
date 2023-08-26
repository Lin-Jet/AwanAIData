import re

def main():

    file = open("rawData_02_formulaNote-繁體.txt", "r")
    lines = file.readlines()
    file.close()
    with open("result02.txt", "w") as output_file:
        for line in lines:
            # boundary = re.search(r"#===", line)
            # if (boundary):
            #     while line != (boundary):
            #         print (line)
            pattern = re.compile(r"^(\[(?P<q>.+)\]|\-\-)\s?(?P<a>.+)\s*")
            matches = pattern.finditer(line)

            yellowName = ""
            blueName = ""
            greyName1 = ""
            greyName2 = ""
            brownText = ""
            blueText = ""
            pinkName = ""
            tealName = ""
            greenText1 = ""
            greenText2 = ""
            unusedtext = ""


            for match in matches:
                # output_file.write("one instance: " + match.group())
                if (match.group("q") == "方名"):
                    yellowName = match.group("a")
                elif (match.group("q") == "出處"):
                    blueName = match.group("a")
                elif (match.group("q") == "原文"):
                    greyName = match.group("a")
                    # output_file.write("greyname: " + greyName + '\n')
                    greyfilter = re.finditer(r"\-\-\s+(.+)", greyName)
                    greyMatches = [m.group(1) for m in greyfilter]
                    greyName1 = greyMatches[0] if len(greyMatches) >= 1 else ""
                    greyName2 = greyMatches[1] if len(greyMatches) >= 2 else ""
                elif (match.group("q") == "原文劑量"):
                    brownText = match.group("a")
                elif (match.group("q") == "用法"):
                    blueText = match.group("a")
                elif (match.group("q") == "功用"):
                    pinkName = match.group("a")
                elif (match.group("q") == "適用症狀"):
                    tealName = match.group("a")
                elif (match.group("q") == "方解"):
                    greenText = match.group("a")
                    greenfilter = re.finditer(r"\-\-\s+(.+)", greenText)
                    greenMatches = [m.group(1) for m in greenfilter]
                    greenText1 = greenMatches[0] if len(greenMatches) >= 1 else ""
                    greenText2 = greenMatches[1] if len(greenMatches) >= 2 else ""
                else:
                    unusedtext = match.group("a")
                
                output_file.write("[Q]什麼是" + yellowName + "?\n" )
                output_file.write("[TAG] " + yellowName + '\n')
                output_file.write("[A] "+ yellowName + "是出自" + blueName + "的方劑，書中原文提到:" + '\n')
                output_file.write("「" + greyName1 +"」" + "\n" + "「" + greyName2 +"」"+ '\n')
                output_file.write( yellowName + "的組成是 " + brownText + '\n')
                output_file.write( yellowName + "的功用是 " + pinkName + "，可應用在" + tealName + "。" + blueText + '\n')
                output_file.write(greyName1 + '\n')
                output_file.write(greyName2 + "\n\n")
            
if __name__ == "__main__":
    main()