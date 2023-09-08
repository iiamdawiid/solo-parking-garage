class ParkingGarage():


    def __init__(self):
        self.tickets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.parkingSpaces = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.currentTicket = {}


    def takeTicket(self):
        """This should decrease the amount of tickets available by 1
           This should decrease the amount of parkingSpaces available by 1"""
        del self.tickets[-1]
        del self.parkingSpaces[-1]
        self.currentTicket["paid"] = False
        

    def payForParking(self):
        """Display an input that waits for an amount from the user and store it in a variable.
           If the payment variable is not empty then (meaning the ticket has been paid) ->  display 
           a message to the user that their ticket has been paid and they have 15mins to leave
           This should update the "currentTicket" dictionary key "paid" to True"""
        ticketCost = 50
        if self.currentTicket["paid"] == False:
            while True:
                payment = input("Enter payment amount: ")
                if payment:
                    while payment.isalpha():
                        payment = input("Enter valid payment (50): ")
                    while payment.startswith('$'):
                        payment = payment[1:]
                    if int(payment) == ticketCost:
                        print("\nTicket PAID. You have 15 min to leave the garage.\nThank you!")
                        self.currentTicket["paid"] = True
                    else:
                        while int(payment) != ticketCost:
                            print(f"\nCorrect Payment Amount: ${ticketCost}")
                            payment = input("Enter payment amount: ")
                            while payment.isalpha():
                                payment = input("Enter valid payment (50): ")
                            while payment.startswith('$'):
                                payment = payment[1:]
                            if int(payment) == ticketCost:
                                print("\nTicket PAID. You have 15 min to leave the garage.\nThank you!")
                                self.currentTicket["paid"] = True
                    break     
                else:
                    print("\nTicket not paid; Please pay the required amount!")
        else:
            print("Ticket has been paid!")


    def leaveGarage(self):
        """If the ticket has been paid, display a message of "Thank You, have a nice day"
           If the ticket has not been paid, display an input prompt for payment
           Once paid, display message "Thank you, have a nice day!"
           Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
           Update tickets list to increase by 1 (meaning add to the tickets list)"""
        if self.currentTicket["paid"] == True:
            print("Have a nice day!")
            self.parkingSpaces.append(1)
            self.tickets.append(1)
        else:
            self.payForParking()



# main
parking = ParkingGarage()

print("PARKING GARAGE".center(50, '-'))
print(f"AVAILABLE SPOTS: {len(parking.parkingSpaces)}")
user_input = input("Would you like to park? (Y/N): ")

while user_input.upper() not in ['Y', 'N']:
    print("\nPlease enter Y to park or N to cancel...")
    user_input = input("Would you like to park? (Y/N): ")

if user_input.upper() == 'Y':
    parking.takeTicket()
    print(f"\nAVAILABLE SPOTS: {len(parking.parkingSpaces)}")
    print("Thank you for parking with us!")
    leave_garage = input("\nEnter 'Y' when ready to leave: ")
    
    while leave_garage.upper() != 'Y':
        leave_garage = input("Please enter 'Y' if you are ready to leave: ")
    
    if leave_garage.upper() == 'Y':
        print("\nPlease pay parking fee: $50")
        parking.payForParking()
        parking.leaveGarage()

else:
    print("\nWe hope to see you again!")
