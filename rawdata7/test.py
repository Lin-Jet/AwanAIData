apStr = "內關+足三里+太衝+間使+尺澤(放血)+曲澤(放血)+心俞(放血)+厥陰俞(放血)+關元+巨闕+少府+湧泉+公孫+內關+郄門+神門+厥陰俞+巨闕"
apQ = apStr.split("+")
newQ = []
[newQ.append(item) for item in apQ if item not in newQ]
print(newQ)

tempStr = ""
for i in newQ:
    tempStr += f"{i}, "



print("temp " + tempStr)