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
    '''
    >>> avoids('abcd','a')
    False
    
    >>> avoids('long','on')
    False
    
    >>> avoids('doctest','am')
    True
    '''
    for i in range(0,len(string)):
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
    '''
    >>> uses_only('missisipi','misp')
    True
    
    >>> uses_only('evaluate','evalut')
    True
    
    >>> uses_only('longhorn','avecy')
    False
    >>> uses_only('longhorn','yaveh')
    False
    
    >>> uses_only('aabe','ab')
    False
    '''
    correct = 0
    for i in range(len(word)):
        if correct == 3:
            break
        if word[i] in string:
            correct = 1
        if word[i] not in string:
            correct = 3
    if correct == 1:
        return True
    if correct == 3:
        return False
    
def words_with_only(string):
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,string):
                    print(word)
                    
def uses_all(word,string):
    '''
    >>> uses_all('school','olhcs')
    False
    >>> uses_all('flower','rewolf')
    True
    '''
    correct = 0
    for i in range(len(word)):
        if string[i] in word:
            correct += 1
        if string[i] not in word:
            correct = 0
            break
    if  correct != len(string):
        return False
    if correct == len(string):
        return True
    

     
    
                    
            
                    
                
        




if __name__ == "__main__":
    import doctest
    doctest.testmod()
        