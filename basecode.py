import array
page="naveen"
print(page)
enter=input("enter the above line \n")
incorrect_char=[]
correct_char=[]
for i in range(len(enter)):
    
        if enter[i]==page[i]:
            correct_char.append(enter[i])      
        else:
              incorrect_char.append(enter[i])
if len(correct_char)>0:
     print("following is the correctly typed letters")
     print(correct_char)
     for char in correct_char:
      
        print(char,end="")
        
if len(incorrect_char)>0:
      print("")
      print("following is the incorrectly typed letters")
      for char in incorrect_char:
            
            print(char,end="")                 
        
          
          
