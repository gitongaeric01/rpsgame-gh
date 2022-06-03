"""
rock beat sciccors
sciccors beat paper
paper beats rock
"""

while True:
        import random
        options=["R","P","S"]
        user_pick=input( "select 'R', 'P' or 'S': ")
        cpu_pick=random.choice(options)
        while True:
            
            if user_pick not in options:
                print ("Invalid choice, Try to choose again")
                #user_pick=input( "select 'R', 'P' or 'S': ")   
                break
           
            if user_pick=="R" and cpu_pick =="R":
                print("Player(Rock):CPU(Rock)")
                print("its a tie")
                

            if user_pick=="P" and cpu_pick =="P":
                print("Player(Paper):CPU(Paper)")
                print("its a tie")
            
                
            if user_pick=="S" and cpu_pick =="S":
                print("Player(Scissors):CPU(Scissors)")
                print("its a tie")
            
            
            
            if  user_pick=="R" and cpu_pick=="S":
                    print("Player(Rock):CPU(Sciccors)")
                    print("player has won")
                    

            if  user_pick=="S" and cpu_pick=="P":
                    print("Player(Scissors):CPU(Paper)")
                    print("player has won")
                    
            if  user_pick=="P" and cpu_pick=="R":
                    print("Player(Paper):CPU(Rock)")
                    print("Player has won") 
                
            if  user_pick=="S" and cpu_pick=="R":
                    print("Player(Scissors):CPU(Rock)")
                    print("CPU has won")
            if  user_pick=="P" and cpu_pick=="S":
                    print("Player(Paper):CPU(Scissors)")
                    print("CPU has won")
            if  user_pick=="R" and cpu_pick=="P":
                    print("Player(Rock):CPU(Paper)")
                    print("CPU has won")       
            break
            
        play_again= input("would you like to play again.Select 'Y' or 'N': ")
        if play_again== "Y":
                 continue
        if play_again =="N":
                 break

