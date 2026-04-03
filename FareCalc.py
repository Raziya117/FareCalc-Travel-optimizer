#FareCalc Travel Optimizer
print("WELCOME TO CITYCAB FARE CALCULATOR")
def calculate_fare(dist,vehicle,hours,rates):
        base_charge=50
        
        base_fare=dist*rates[vehicle]
        total=base_charge+base_fare
        
        if 17<=hours<=20:
            extra_charge=1.5
        else:
            extra_charge=1
        final_amt=total*extra_charge
        
        if final_amt>500:
            disc=final_amt*0.1
            final_amt-=disc
        else:
            disc=0
        return base_fare,base_charge,extra_charge,total,disc,final_amt
while True:
    dist=float(input("Enter distance to travel in km:"))
    print("Select Vehicle Type\n 1.Economy(Auto/Bike) \n 2.Premium(Sedan)\n 3.SUV")
    choice=int(input("Enter your choice(1/2/3): "))

    if choice==1:
        vehicle="Economy"
    elif choice==2:
        vehicle="Premium"
    elif choice==3:
        vehicle="SUV"
    else:
        print("Invalid choice!!Please select (1/2/3):")
        continue

    hours=int(input("Enter hours(0-23):"))
    rates={
            "Economy":10,
            "Premium":18,
            "SUV":25
            }
        
    if vehicle not in rates:
        print("Service not available for the entered vehicle Type")
    else:
        base_fare,base_charge,extra_charge,total,disc,final_amt=calculate_fare(dist,vehicle,hours,rates)
        print("====================CITYCAB RECEIPT=====================")
        print("Distance: ",dist,"km")
        print("Vehicle: ",vehicle)
        print("Base charge: ",base_charge)
        print("Base Fare: ",base_fare)
        print("Total without extra charges:",total)

        if extra_charge>1:
            print("Extra charge applied (1.5x)")
        else:
            print("No extra charges applied")
        
        print("Discount: ",disc)
        print("Final amount: ",final_amt)
        print("========================================================")
    
    ch=input("If you want to calculate for another ride enter(YES/NO):")
    if ch.lower()!="yes":
        print("Thank you for using CityCab!\nHappy Riding,Have a great day!!")
        break
    
