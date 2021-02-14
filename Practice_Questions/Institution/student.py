class Institution(object):
	"""docstring for Institution"""
	def __init__(self, institutionId, institutionName, noOfStudentPlaced, noOfStudentCleared, location):
		self.institutionId = institutionId
		self.institutionName = institutionName
		self.noOfStudentPlaced = noOfStudentPlaced
		self.noOfStudentCleared = noOfStudentCleared
		self.location = location
		self.grade = 0

	def set_institutionId(self, id):
		self.institutionId = id

	def get_institutionId(self):
		return self.institutionId

	def set_institutionName(self, name):
		self.institutionName = name

	def get_institutionName(self):
		return self.institutionName

	def set_noOfStudentPlaced(self, no):
		self.noOfStudentPlaced = no

	def get_noOfStudentPlaced(self):
		return self.noOfStudentPlaced

	def set_noOfStudentCleared(self, no):
		self.noOfStudentCleared = no

	def get_noOfStudentCleared(self):
		return self.noOfStudentCleared

	def set_location(self, location):
		self.location = location

	def get_location(self):
		return self.location

	def set_grade(self, grade):
		self.grade = grade

	def get_grade(self):
		return self.grade


def findNumClearancedByLoc(inst_obj, location):
	total = 0
	for institute in inst_obj:
		if institute.get_location().lower() == location.lower():
			total += institute.get_noOfStudentCleared()

	return total if total > 0 else 0



def updateInstitutionGrade(inst_obj, name):
	for institute in inst_obj:
		if institute.get_institutionName().lower() == name.lower():
			rating = (institute.get_noOfStudentPlaced() * 100) / institute.get_noOfStudentCleared()
			institute.set_grade('A' if rating >= 80 else 'B')
			return institute

	return None

		

if __name__ == '__main__':
	n = int(input())
	inst_obj = []
	for _ in range(n):
		id, name, place, clear, loc = int(input()), input(), int(input()), int(input()), input()
		inst_obj.append(Institution(id, name, place, clear, loc))

	location = input()
	name = input()

	noOfClearance = findNumClearancedByLoc(inst_obj, location)
	print(noOfClearance) if noOfClearance > 0 else print('There are no cleared students in this particular location.')

	name_grade = updateInstitutionGrade(inst_obj, name)
	print(f'{name_grade.get_institutionName()}::{name_grade.get_grade()}') if name_grade else print('No institute is available with the specified name.')
