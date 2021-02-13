class Passenger(object):
	def __init__(self, id, name, gender, miles):
		self.pass_id = id
		self.pass_name = name
		self.pass_gender = gender
		self.pass_miles = miles

	def calculate_discount(self, discount_rate):
		discount = (self.pass_miles * discount_rate) / 100
		return discount


class Organisation:
	def __init__(self, name, p_list):
		self.org_name = name
		self.pass_list = p_list

	def calculate_discount_(self, id, discount_rate):
		dis = 0
		for i in self.pass_list:
			if i.pass_id == id:
				dis = i.calculate_discount(discount_rate)
				return dis if dis > 0 else -1

		return 0


if __name__ == '__main__':
	n = int(input())
	pass_list = []
	disc_rate = int(input())
	for i in range(n):
		id, name, age, miles = int(input()), input(), int(input()), int(input())
		pass_list.append(Passenger(id, name, age, miles))


	org = Organisation("TCS", pass_list)
	id = input()
	rate = int(input())
	result = org.calculate_discount_(id, rate)
	if res != 0:
		if res > 0:
			print(f"The discount rate for {id} is {res}")
		else:
			print(f'The discount rate will not there for {id}')


	else:
		print(f"No passenger is there!")

		