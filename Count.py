def functionname(string):
    low,upper,digit,special=0,0,0,0
    for i in string:
        if i.islower():
            low+=1
        elif i.isupper():
            upper+=1
        elif i.isdigit():
            digit+=1
        else:
            special+=1
    print('Length of string',len(string))
    print('lowercase',low)    
    print('Uppercase',upper)    
    print('digit',digit)
    print('special',special)
b=input('Enter your string:')    
functionname(b)    
