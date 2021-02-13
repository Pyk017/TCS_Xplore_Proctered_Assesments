# Problem Statement

Create class Passenger with attributes:
passengerName of type String, passengerAge of type Number represents the age of the passenger.
distanceTravelled of type Number represents the distanceTravelled in KM.

Create the constructor (__init__method) which takes parameters in above sequence for passengerName, passengerAge and distanceTravelled.
Method will set the value passed argument to the attributes of the Passenger object created.

Define 1:
 calculateTicketFare => Function will take as arguments a list of Passenger and fare per KM and calculate the total amount to be paid for the ticket fare including the tax for all the passengers in the list.
 To calculate the fare following formula is to be used:
 
 Ticket fare with tax = (distanceTravelled * fare) + tax, where tax is calculated based on the age of the passenger as below, 
 
 For passenger of age 60 or more or age less than 12, no tax required.
 
 For passenger of the age group 21 to 59, tax is 12% of Ticket fare calculte without Tax.
 
 2. countSeniorJuniorPassenger => function will take as argument a list of Passenger objects and return the count of senior and junior passengers in the list.
 Passenger having age >= 60 are considered as Senior and passengers having age < 12 are considered as junior.
 
 These methods should be called from the main section.
 Instruction to write main section of the code :
 
 a. You would require to write the main section completely, hence please follow the below instructions for the same.
 b. You would require to write the main program inline to the "same input description section" mentioned below and to read the data in the same sequence.
 c. Create the respective objects(Passenger) with the given sequence of arguments to fulfill the __init__ method requirement defined in the respective classes referring to the below instructions:
  1. Create a list of Passenger objects which will be passed as arguments while calling the function in main. To create the list, 
    a. Read a number for the count of Passenger objects to be created and added to the list.
    b. Create a passenger object after reading the data related to it and add the object to the list to be created. The points repeat for the number of passenger objects to be created as per point c.1.a
    
  2. Read a value for the ticket fare per KM to be passed as argument to the function calculateTicketFare.
  3. Call the function calculteTicketFare by passing th passengerlist created in point c.1 and the value read in point 2.
  4. Call the function calculateSeniorJuniorPassengers by passing the passenger list created in point c.1
  5. Display the value returned by the function calculateTicketFare. 
  6. Display the value returned by the function countSeniorJuniorPassengers.
  
  
## Sample Input description:
1. The first line of input is the number of passengers objects to be added to the list of passenger objects.
2. The next set of inputs are passengerName, passengerAge and distanceTravelled for each passenger object taken on after another and is repeated for number of times the total nunber of passenger objects.
3. The last input is the value for ticket fare per KM to be passed as argument to the function calculateTicketFare.

### Sample Inputs:
 ## Testcase 1.
 ```
 Input:
 4
 Anupam
 10
 20
 Dipali
 30
 300 
 Diganta
 80
 100
 Golap
 55
 200
 100
 Output:
 68000.0
 2
```

## Testcase 2. 
```
5
Aparna
78
200
Bimal
12
80
Makani
25
110
Binita
45
300
Gajen
30
200
50
Output:
48560.0
1

```
  
