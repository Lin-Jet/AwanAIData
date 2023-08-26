import re

def main():

    file = open("rawData_02_formulaNote-繁體.txt", "r")
    lines = file.readlines()
    file.close()
    with open("result02.txt", "w") as output_file:
        for line in lines:
            # pattern = re.compile(r"""
            # \[方名\](.+)?
            # \[出處\](.+)?
            # \[原文\]
            # (\-\-(.+)?)*
            # \[原文劑量\](.+)?
            # \[現代劑量\](.+)?
            # \[用法\](.+)?
            # \[劑型\](.+)?
            # \[劑量大小\](.+)?
            # \[方性提示\](.+)?
            # \[功用\](.+)?
            # \[適用症狀\](.+)?
            # \[方解\]
            # (\-\-(.+)?)*
            # \[自動調整劑量\](.+)?
            # \[劑量提示\](.+)?
            # \[加減\](.+)?
            # \[注意事項\](.+)?
            # """)
            pattern = re.compile(r"\[方名\]\s+(.+)\[出處\]\s*(.+)\s+")
            matches = pattern.finditer(line)

            for match in matches:
                output_file.write(match.group(1) + '\n' + match.group(2) + '\n')
                
            
if __name__ == "__main__":
    main()