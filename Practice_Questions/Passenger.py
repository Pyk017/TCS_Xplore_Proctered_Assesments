class Passenger(object):
	def __init__(self, id, name, gender, miles):
		self.pass_id = id
		self.pass_name = name
		self.pass_gender = gender
		self.pass_miles = miles

	def calculate_discount(self, discount_rate):
		discount = (self.pass_miles * discount_rate) // 100
		return discount


class Organisation(object):
	def __init__(self, name, passList):
		self.org_name = name
		self.passenger_list = passList


	def calculate_discount(self, id, rate):
		for passenger in self.passenger_list:
			if passenger.pass_id == id:
				dis = passenger.calculate_discount(rate)
				return dis if dis > 0 else (-1) * dis

		return 0
					
		
if __name__ == '__main__':
	pass_list = []
	count = int(input())
	for i in range(count):
		id, name, gender, miles = input(), input(), input(), int(input())
		pass_list.append(Passenger(id, name, gender, miles))

	o = Organisation("XYZ Corp", pass_list)
	inp_id = input()
	inp_percent = int(input())
	discount = o.calculate_discount(inp_id, inp_percent)

	if discount > 0:
		print("Discount of the passenger with id ", inp_id, ' is:', discount)
	else:
		if discount < 0:
			print("Passenger with id ", inp_id, ' is not eligible for discount')
		else:
			print("Passenger with given id not found")

		