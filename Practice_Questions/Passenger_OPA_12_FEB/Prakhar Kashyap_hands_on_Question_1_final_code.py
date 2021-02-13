class Passenger(object): 
	def __init__(self, name, age, dist): 
		self.passengerName = name 
		self.passengerAge = age 
		self.distanceTravelled = dist 


def calculateTicketFare(passengers, fare): 
	total = 0 
	for i in passengers: 
		if i.passengerAge >= 60 or i.passengerAge < 12: 
			total += (i.distanceTravelled * fare) 
		elif i.passengerAge > 20 and i.passengerAge < 60: 
			total += (i.distanceTravelled * fare) + ((i.distanceTravelled * fare) * 0.12) 
		elif i.passengerAge >= 12 and i.passengerAge < 21: 
			total += (i.distanceTravelled * fare) + ((i.distanceTravelled * fare) * 0.10) 

	return total 


def countSeniorJuniorPassengers(passengers): 
	count = 0 
	for i in passengers: 
		if i.passengerAge >= 60 or i.passengerAge < 12: 
			count += 1 

	return count 


n = int(input()) 
pass_obj = [] 
for _ in range(n): 
	name, age, dist = input(), int(input()), int(input()) 
	pass_obj.append(Passenger(name, age, dist)) 

fare = int(input()) 
temp = calculateTicketFare(pass_obj, fare) 
print(temp) 
count = countSeniorJuniorPassengers(pass_obj) 
print(count)