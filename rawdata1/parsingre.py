import re

def main():

    file = open("rawData_01_中醫名詞大辭典.txt", "r")
    lines = file.readlines()
    file.close()
    with open("result_01.txt", "w") as output_file:
        for line in lines:
            pattern = re.compile(r"【(\S+)】(.+)■?")
            matches = pattern.finditer(line)

            for match in matches:
                q_temp = match.group(1)
                q = ''.join(q_temp.split())
                a_temp = match.group(2)
                a = ''.join(a_temp.split())
                output_file.write("[Q] 什麼是" + q + "\n[TAG] " + q + "\n[A] " + a + '\n\n')
            
if __name__ == "__main__":
    main()