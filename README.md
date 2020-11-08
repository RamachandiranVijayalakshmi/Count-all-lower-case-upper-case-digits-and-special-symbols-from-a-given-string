# Count-all-lower-case-upper-case-digits-and-special-symbols-from-a-given-string
- get the valide input for the user
- calculate the user input length
- count the type of length
## sample code
```
for i in string:
   if i.islower():
      low+=1
   elif i.isupper():
      upper+=1
   elif i.isdigit():
      digit+=1
   else:
      special+=11
```
## Exapmle output
```
Enter your string:welcome 2021
Length of string 12
lowercase 7
Uppercase 0
digit 4
special 1
```
