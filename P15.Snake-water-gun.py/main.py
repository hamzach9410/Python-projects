computer=-1
youstr=input("Enter your Choice: ")
youDict ={"s":1, "w":-1, "g":0}
reverseDisk={1:"snake",-1:"Water",0:"Gun"}
you=youDict[youstr]



print("computer choose")
if("computer chose {reverseDict[computer]}"):
   print("its draw")

if(computer ==-1 and you ==1): 
   print("You Win")
   
elif(computer ==-1 and you ==0):
   print("You Lose!")
   
if(computer ==1 and you ==-1):
   print("You Lose")

elif(computer ==1 and you ==0):
   print("You Win")
   
if(computer ==0 and you ==-1):
   print("You Lose") 
     
elif(computer ==0 and you ==1):
   print("You Win")
   
else:
    print("something went wrong ")