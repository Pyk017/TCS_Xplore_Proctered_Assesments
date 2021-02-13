class AutonomousCar(object):
	"""docstring for AutonomousCar"""
	def __init__(self, carId, brand, noOfTestConduct, noOfTestPassed, environ):
		self.carId = carId
		self.brand = brand
		self.noOfTestConducted = noOfTestConduct
		self.noOfTestPassed = noOfTestPassed
		self.environment = environ
		self.grade = 0

	def set_carId(self, id):
		self.carId = id

	def get_carId(self):
		return self.carId

	def set_brand(self, brand):
		self.brand = brand

	def get_brand(self):
		return self.brand

	def set_noOfTestConducted(self, no):
		self.noOfTestConducted = no

	def get_noOfTestConducted(self):
		return self.noOfTestConducted

	def set_noOfTestPassed(self, no):
		self.noOfTestPassed = no

	def get_noOfTestPassed(self):
		return self.noOfTestPassed

	def set_environment(self, environ):
		self.environment = environ

	def get_environment(self):
		return self.environment	

	def set_grade(self, grade):
		self.grade = grade

	def get_grade(self):
		return self.grade


def findTestPassedByEnv(autocar_obj, env):
	temp = 0
	for car in autocar_obj:
		if car.get_environment() == env:
			temp += car.get_noOfTestPassed()

	return 0 if not temp else temp 


def updateCarGrade(autocar_obj, brand):
	rating = 0
	for car in autocar_obj:
		if car.get_brand() == brand:
			rating = (car.get_noOfTestPassed() * 100) / car.get_noOfTestConducted()
			return f"{car.get_brand()}::A1" if rating >= 80 else f"{car.get_brand()}::B2"

	return None



if __name__ == '__main__':
	n = int(input())
	car_list = []
	for _ in range(n):
		carId, brand, testConduct, testPassed, env = int(input()), input(), int(input()), int(input()), input()
		car_list.append(AutonomousCar(carId, brand, testConduct, testPassed, env))

	environ = input()
	brand = input()

	totalTestPassed = findTestPassedByEnv(car_list, environ)
	print(totalTestPassed) if totalTestPassed > 0 else print("There are no test passed in this particular environment")

	brandGrade = updateCarGrade(car_list, brand)
	print(brandGrade) if brandGrade else print('No Car is available with the specified brand.')
