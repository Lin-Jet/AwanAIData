

def main():

    f = open("rawData_01_中醫名詞大辭典.txt", "r")

    data = f.read()
    tag = []
    ans = []

    for i in range(len(data)):
        tag_helper = []
        ans_helper = []
        if (data[i] == '【'):
            while (data[i] != '】'):
                if (data[i+1] != '】'):
                    tag_helper.append(data[i+1])
                i = i + 1
        
        if (data[i] == '】'):
            while i < len(data) and data[i] != '【' and data[i] != '■':
                if (i+1 < len(data)) and (data[i+1] != '【' and data[i+1] != '■'):
                    ans_helper.append(data[i+1])
                i = i + 1




        tag_helper = "".join(tag_helper)
        
        ans_helper = "".join(ans_helper)
        
        for j in tag_helper:
            if tag_helper not in tag:
                tag.append(tag_helper)

        for k in ans_helper:
            if ans_helper not in ans:
                ans.append(ans_helper)
            
                
    print ("len of tag ", len(tag))
    print ("len of ans ", len(ans))

    
    with open("result.txt", "w") as output_file:
        for i in range(len(tag)):
            output_file.write("[Q] 什麼是" + tag[i] + '?' + '\n' + "[TAG] " + tag[i] + '\n' + "[A] " + ans[i] +'\n')
    

    

    f.close()



if __name__ == "__main__":
    main()
    