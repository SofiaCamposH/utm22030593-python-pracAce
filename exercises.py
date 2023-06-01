#A list with 5 items, add a new element and print it using a for loop.
Countrylist = ["Mexico", "United States", "Korea", "Brazil", "France"]
Countrylist.append ("Canada")
for item in Countrylist: 
    print(item) 
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#A tuple with 7 items and print it using a while loop.
animals=("Cat","Dog","Cow","Rabbit","Duck","Butterfly","Cricket")
i=0 
while i < len(animals):
    print(animals[i])
    i += 1

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#A dictionary with 3 properAes, modify any of those and print it.

footballTeams={'FCB':'Barcelona','MCI':'Manchester City FC','PSG':'Paris Saint-Germain FC'}	
footballTeams["FCB"] = 'FC Barcelona'
print(footballTeams)

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#A function named operation, that receives 3 params.
def operation(operand,fnumber,snumber):
    operand = str(operand)
    fnumber = int(fnumber)
    snumber = int(snumber)
    result = 0
    
    if operand == '+':
        result=fnumber + snumber

    if operand == '-':
        result=fnumber - snumber
     
    if operand == '*':
        result=fnumber * snumber
      
    if operand == '/':
        if snumber== 0:
            print("Invalid")
            result = "error"
        else:
            result=fnumber / snumber
    return result
    
print(operation('+', 5, 7)) 
print(operation('-', 79, 43)) 
print(operation('*', 4, 6)) 
print(operation('/', 7, 4)) 
print(operation('/', 7, 0)) 





         

            
            
         

    
