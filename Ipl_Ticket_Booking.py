#Ipl tickets
t1=10
t2=10
while True:
    username=input("Username: ")
    print(f"Welcome {username}!")
    event=int(input("Choose the match you are interested in: 1.SRH vs MI 2.RCB vs CSK"))
    if(event==1):
        
        
        
        if(t1==0 and t2==0):
            print("We are all sold out at the present")
            continue
        elif(t2!=0 and t1==0):
            print("East wing is all sold out")
        elif(t1!=0 and t2==0):
            print("Lounge is all sold out")

        section=int(input('''Select from the available seating: 1.East wing(5000) 2.Fan lounge(8000)'''))
           
        if(section==1 and t1!=0):
            print(f"{t1}seats are available,You can only select upto 5 tickets at a time")
            n=int(input("Enter the number of tickets required:"))
            if n<=5:
                if t1>=n:
                    card=int(input("Select the payment option 1.Creditcard 2.Debitcard"))
                    if card==1 or card==2:
                        x=n*5000
                        cash=int(input(f"Please pay {x}rs"))
                        if cash==x:
                            print("Congratulations, Your seats are booked")
                            t1-=n
                        else:
                            print("Enter the correct amount")
                    else:
                        print("Select one of the given options")
                else:
                    print("Sorry, Tickets are unavailable, Please try again")
            else:
                print("You can only select upto 5 tickets at a time")
        
        elif(section==2 and t2!=0):
            print(f"{t2}seats are available,You can only select upto 5 tickets at a time")
            n=int(input("Enter the number of tickets required:"))
            if n<=5:
                if t2>=n:
                    card=int(input("Select the payment option 1.Creditcard 2.Debitcard"))
                    if card==1 or card==2:
                        x=n*8000
                        cash=int(input(f"Please pay {x}rs"))
                        if cash==x:
                            print("Congratulations, Your seats are booked")
                            t2-=n
                        else:
                            print("Please try again")
                    else:
                        print("Select one of the given options")
                else:
                    print("Sorry, Tickets are unavailable, Please try again")
            else:
                print("You can only select upto 5 tickets at a time")
        
        

    elif(event==2):
        print("Bookings will be open soon")
            
        
            
            
                
                    
                    
                

                                                    
                                                    
                                                    
                                                    



    
                
    
    



    
