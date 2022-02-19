print("welcome to bank of asia")

restart =("Y")
chances=3
ballance=65
while chances>=0:
    pin=int(input("Please inter your four digit pin:"))
    if pin==(1234):
        print("you intered your pin \n")
        while restart not in ("n","No","no","N"):
            print("please press 1 for your ballance\n" )
            print("please press 2 for make a withdrawl \n")
            print("please press 3 for cash in \n")
            print("please press 4 for return card \n")
            option=int(input("what would you like to chose:"))
            if option == 1:
                print("your ballance is now $",ballance ,'\n')
                restart=input("would you like to go back?")
                if restart in("n","No","no","N"):
                    print("thank you")
                    break
            elif option==2:
                option2=("y")
                withdrawl =float (input("how much would you like to withdrawl?\n $10 /$20/$40/$60/$80"))
                if withdrawl in [10,20,40,60,80]:
                    ballance=ballance-withdrawl
                    print("\n your carrent ballance is:",ballance)
                    restart =input("would you like to go back?")
                    if restart in ("n", "No", "no", "N"):
                            print("thank you")
                            break
                    elif withdrawl !=[100,200,300,400,500]:
                            print("invalaid amount please re-try \n")
                            restart=("y")
                    elif withdrawl==1:
                            withdrawl=float(input("please enter desired amount:"))
            elif option== 3:
                cash_in=float(input("how much would you like to cash in?"))
                ballance=ballance +cash_in
                print ("your ballance is now :",ballance)
                restart=("would you like to go back ?")
                if restart in ("n", "No", "no", "N"):
                    print("thank you")
                    break
            elif option== 4:
                print("please wait whilst your card is returned...\n")
                print("thank you for you service")
                break
    elif pin!=("1234"):
        print ("incorrect password")
        chances=chances-1
        if chances==0:
            print("\n No more tries")
            break