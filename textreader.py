def read_file():
    
    with open("words.txt") as file:
        count_the = 0
        for line in file:
            for word in line.strip().split():
                count_the += 1
                    
            
        print(count_the)
        
def at_least():
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)

def has_no_e(word):
    if 'e' in word:
        return True

def no_e():
    count = 0
    count_the = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                count_the += 1
                if has_no_e(word):
                    count += 1
    perc = ((count/count_the)*100)//1
    a = int(perc)
    print('{:2}'.format(a)+'%')


    
                
            
def avoids(tword,string):
    for i in range(0,len(tword)):
        if string[i] in tword:
            return False
        else:
            return True
        
def count_avoids():
    count = 0
    forbidden = input('Enter a string of 5 forbidden letters: ')
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(word, forbidden):
                    count += 1
                    
    print(count)
    
def uses_only(word,string):
    correct = 0
    for i in range(len(string)):
        if correct == 3:
            break
        if string[i] in word:
            correct = 1
        if string[i] not in word:
            correct = 3
    if correct == 1:
        return True
    
def words_with_only(string):
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,string):
                    print(word)
    

     
    
                    
            
                    
                
        




if __name__ == "__main__":
    count_avoids()
    