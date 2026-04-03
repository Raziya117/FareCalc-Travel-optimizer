# 🚘FareCalc Travel optimizer
### Project Description
FareCalc is a python based application developed for a ride-sharing startup,CityCab.It caluculates the ride fare dynamically based on distance,vehicle type and time.The system also applies extra charges during peak hours and provides discounts for higher fares.

### Features
- Calculates fare based on distance(per km rate)
- Supports multiple vechicle types(Economy,Premium,SUV)
- Applies extra charge during peak hours(5PM-8PM)
- Provides discount for fares above certain amount
- Allows multiple ride calculations using loop
- Displays a clean and formatted receipt
- 
### Key Concepts used 
- Technology: Python
- Basic Programming Concepts(Functions,Loops,Conditions,Dictionary)
     - Function for modular code
     - Dictionary for rate mapping
     - Conditional statements for Pricing logic
     - Loop for repeated execution
  
### Fare Calculation logic
- Base charge:₹50 (fixed for every ride)
- Distance Fare:Based on selected vechicle type
     - Economy:₹10/km
     - Premium:₹18/km
     - SUV:₹25/km
- Extra charge:1.5x applied during peak hours(17-20)
- Discpunt 10% is applied if total fare exceeds ₹500

### Execution steps
1. Open the Python file
2. Run the code
3. Enter:
     -  Distance in km
     -  Vechile type(1/2/3)
     -  Hours(0-23)
4. View the generated receipt
5. Choose to caluculate another ride or exit

### Sample output
```
WELCOME TO CITYCAB FARE CALCULATOR
Enter distance to travel in km:20
Select Vehicle Type
 1.Economy(Auto/Bike) 
 2.Premium(Sedan)
 3.SUV
Enter your choice(1/2/3): 1
Enter hours(0-23):20
====================CITYCAB RECEIPT=====================
Distance:  20.0 km
Vehicle:  Economy
Base charge:  50
Base Fare:  200.0
Total without extra charges: 250.0
Extra charge applied (1.5x)
Discount:  0
Final amount:  375.0
========================================================
If you want to calculate for another ride enter(YES/NO):no
Thank you for using CityCab!
Happy Riding,Have a great day!!
```
### Conclusion
This project demonstrates a real-world fare calculation system using Python. It focuses on clean code structure, user-friendly interaction, and practical business logic implementation.

### 👤 Author
Raziya Mohammad
