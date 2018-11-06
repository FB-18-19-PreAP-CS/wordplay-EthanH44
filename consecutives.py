def consecutives():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                for i in range(len(word)-5):
                    if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                        print(word)
                
                
def odemeter():
    for i in range(1000000):
        num = str(i)
        if len(num) == 6:
            if num[2:] == num[5:1:-1]:
                num = str(a)
                a += 1
                a = str(num)
                if a[1:] == a[5:0:-1]:
                    num = str(a)
                    a += 1
                    a = str(num)
                    if a[2:4] == a[5:1:-1]:
                        num = str(a)
                        a += 1
                        a = str(num)
                        if a[::-1] == a:
                            print(a)
                
           
def main():
    odemeter()
           
if __name__ == "__main__":
    main()