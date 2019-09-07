import random;

print("\t\t****Welcome to Guessing The Number Game!!****")
userName = input("\n\t\tEnter your Name : ")
        
print("\n\t\t**********Hello ",userName,"**********")
print("\t****************************************************************")
startGame = int(input("\n    In this Game You Can Only Guess Five Times. Press 1 to Start the Game : "))
   
rand1 = random.randint(0,21)

if(startGame == 1):
    guessNumber = int(input("\n\t\tPlease Input a Number between 0 and 20 : "))
    for i in range(5,0,-1):
        if (guessNumber > rand1):
            
            print("\n\t\tGuess Again!! ","\n\t\tRemaining Guess(es) : ",i,"\n\t\tTry Smaller number than that...")
            guessNumber = int(input("\n\t\tEnter the number : "))
                
        elif(guessNumber < rand1):
            print("\n\t\tGuess Again!! ","\n\t\tRemaining Guess(es) : ",i,"\n\t\tTry Bigger number than that...")
            guessNumber = int(input("\n\t\tEnter the number : "))
                    
        else:
            print("\t****************************************************************")
            print("\n\t\t    ***********Correct Guess!!***********")
            break
                
            
    if (guessNumber == rand1):
        
        print("\n\t    ****",userName,"is the Winner of our Guess The Number Game!!****")
        print("\n\t****************************************************************")
        n = int(input("\n\tPress O Key to exit...."))
        exit(n)
        
    else:
        
        print("\t****************************************************************")
        print("\n\t   **** Wrong Guess!!",userName,"lost our Guess The Number Game ****")
        print("\n\t****************************************************************")
        n = int(input("\n\tPress O Key to exit...."))
        exit(n)

        
else:
    print("\n\t\t\tGame Didn't Start...GoodBye!!")

n = int(input("\tPress Any Key to exit...."))
exit(n)