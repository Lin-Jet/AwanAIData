import re


string = """1. hello
2. hi
3. haro
3.haro"""


re_filter = r"(\d.\s*)(.*)"

matches = re.sub(re_filter, f"\n{matches.group(1)}", string)

for match in matches:
    print(match)