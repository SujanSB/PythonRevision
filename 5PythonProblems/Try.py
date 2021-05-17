# 5 python Programs to revise the Basics of PYthon

# Q1) Make a simple Dictionary Such that user can get it's meaning after entering the input .
# Solution:
# Dictionary={
#     "Skeptical":"Attitude of Doubt",
#     "Mediocrity":"Quality of being Average",
#     "Jaded":"Lack of Enthusiasm",
#     "Dreaded":"Causing terror",
#     "Pathetic":"Esecially through Sadness",
#     "Bowed":"To bend"
# }
# print("Enter the word ,of which meaning you want to search")
# yourInput = input()
# print("the meaning of the word "+ yourInput + " is ",Dictionary.get(yourInput))


# Q2) Make any list having at least 10 elements.Generate a Random number and thus make any correct answer(A element of that list).Take input from the user to guess whether 		it is correct answer or not .GIve output as "Correct"/"Wrong" answer. 
# Solution:
# import random
# dict1=["one","two","three","four","five",'six',"seven",'eight',"nine","ten"]
# val =random.choice(dict1)
# print(val)
# userInput= input("Enter your Guess \n")
# if userInput==val:
#     print("Correct")
# else:
#     print("Wrong")



# Q3) Password Generator Program 
# 	Create a Python program that generates a random password for the user. Make sure your program takes a few inputs from the user:
# 	    How long should the password be?
# 	    How many characters should there be?
# 	    Should it have both uppercase and lowercase letters?
# 	    Should it include numbers and special symbols, too?

# Solution:
# simple

# import random
# totalCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&;*"
# leng = int(input("Enter Password length"))
# password = ""
# for i in range(leng):
#     password += random.choice(totalCharacters)
# print(password)



# Complex 
# import random
# Lowcharacters = "abcdefghijklmnopqrstuvwxyz"
# Upcharacters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# characters= Lowcharacters+Upcharacters
# num="1234567890"
# symbol="!@#$%&;*"
# password = ""
# while True:
#     length = int(input("Enter Password length\n"))
#     input1=int(input("How many Character should be there?  \n"))
#     pwCharacters=""
#     for i in range(input1):
#         pwCharacters += random.choice(characters)
#     print(pwCharacters)
#     input2 =input("Should it contain Both Uppercase and lowercase,Press 'Y' or 'y' \n")
#     if input2=="Y" or input2=="y":
#         pwCharacters=pwCharacters
#     else :
#         pwCharacters=pwCharacters.lower()

#     print(pwCharacters)

#     ramainingLen=(length-input1)

#     RemainingSN=""
#     input3 =input("Should it contain numbers and special symbols, too \n")
#     if input3=="Y" or input3=="y":
#         RemainingSN=num+symbol
#     else :
#         password=pwCharacters
#         print(password)
#         break

#     for i in range(ramainingLen):
#         password += random.choice(RemainingSN)
#     print(length)

#     print(password+pwCharacters)
#     break




# Q4) "Sakkisakyo ta !!" Game:
# 	Let any number between 1 to 100 s a correct number .(no need to be random number).
# 	Your player needs to be able to input their guesses.
# 	You need to set a maximum limit for guesses.
# 	The player needs to be notified about the remaining number of guesses.
# 	If Player have no remaining guesses then print "Sakkisakyo ta " .
# 	Twist :( if player has no remaining guesses ,give the options of entering the Secret code to increase their guesses "

# Solution:

# print("enter your Name")
# Name = input()
# print("Are you ready to play the game ",Name.upper(),"??")
# print("Press 'Y' and Enter to continue !!!")
# Yes = input()
# if Yes == "Y" or Yes =="y":
#     print("Guess the number")
#     Guess = 5
#     while True:
#         print("enter your guess value")
#         value = int(input())      
#         if value == 45:
#             Guess= Guess -1
#             if Guess==0:
#                 print("Congratulations !!!",Name.split(),"you guess the correct answer in your last chance !!! ")
#             else:
#                 print("Congratulations !!!",Name.split(),"you guess the correct answer with",Guess,"Guesses left")
#             break
#         else:
#             if value>= 45:
#                 print("Your guess  is greater than Correct value")
#             else:
#                 print("Your guess  is Less than Correct value")
#             Guess= Guess -1
#             print("you have ",Guess,"Guess Left")
#             if Guess == 1:
#                 print("Do you want a hint ? press 'Y' if so")
#                 hint= input()
#                 if hint == "Y" or hint =="y":
#                     print("Different between your last guess and the correct value is",abs(value-45))
#                 else:
#                     print("Okey ,Do the last try")

#             if Guess == 0:
#                 print("Sakkisako ta !!!...Sorry <<",Name,">> You are out of Guess")
#                 print("You need to have 'access Code' for extra guesses !!! Do you have ?")
#                 print("If you have type 'Y' otherwise press any key ")
#                 InputAG =input()
#                 if InputAG == "Y" or InputAG =="y":
#                     print("Enter the code .... ")
#                     code = input()
#                     if code=="SUZ":
#                         Guess=Guess+3
#                         continue
#                     else:
#                         print("Access denied !!! Bye Bye",Name)
#                         break
#                 else:
#                     break
              
#             continue
            

# #5
# import random
# file=open("result.txt","w") 
# listValue =["Scissors","Paper","Rock"]
# bot= random.choice(listValue)
# i =5
# userWin=0   
# userLoss=0
# Draw=0
# while True:
#     print("Enter your Choice")
#     print("0 for 'Scissors'")
#     print("1 for 'Paper'")
#     print("2 for 'Rock'")
#     userChoice= int(input())
#     user= listValue[userChoice]
    
#     if user=="Scissors" and bot=="Paper": 
#         userWin =userWin+1
#         print("Congrats you won")
#     elif user =="Paper" and bot=="Rock":
#         userWin =userWin+1
#         print("Congrats you won")
#     elif  user=="Rock" and bot=="Scissors":
#         userWin =userWin+1
#         print("Congrats you won")
#     elif bot=="Scissors" and user=="Paper": 
#         userLoss =userLoss+1
#         print("Sorry you lose")
#     elif bot =="Paper" and user=="Rock":
#         userLoss =userLoss+1
#         print("Sorry you lose")
#     elif  bot=="Rock" and user=="Scissors":
#         userLoss =userLoss+1
#         print("Sorry you lose")
#     else:
#         Draw +=1
#         print("its draw")

#     i=i-1
#     if i==1:
#         if userWin==0:
#             print(" Bad Luck")

#     if i== 0:
#         file.write(f"user have win {userWin}times \n")
#         # file.write("user have win", userWin,"times \n")
#         file.write(f"user have loss {userLoss}times \n")
#         file.write(f"it is drawn {Draw} times\n\n")
#         print("User have won",userWin,"times")
#         break
 
#     continue

# file.close()


