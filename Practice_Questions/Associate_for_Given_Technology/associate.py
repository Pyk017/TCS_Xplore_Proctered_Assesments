class Associate(object):
	"""docstring for Associate"""
	def __init__(self):
		self.id = 0
		self.name = 0
		self.technology = 0
		self.experience = 0

	def set_id(self, id):
		self.id = id

	def get_id(self):
		return self.id

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def get_experience(self):
		return self.experience

	def set_technology(self, tech):
		self.technology = tech

	def get_technology(self):
		return self.technology

	def set_experience(self, exp):
		self.experience = exp

	def get_experience(self):
		return self.experience


	
def associateForGivenTechnology(ass_obj, tech):
	assc_obj = []
	for i in ass_obj:
		if i.get_technology().lower() == tech.lower() and i.get_experience() % 5 == 0:
			assc_obj.append(i)

	return  assc_obj



if __name__ == '__main__':
	n = int(input())
	ass_obj = []
	for _ in range(n):
		id, name, tech, exp = int(input()), input(), input(), int(input())
		temp_obj = Associate()
		temp_obj.set_id(id)
		temp_obj.set_name(name)
		temp_obj.set_technology(tech)
		temp_obj.set_experience(exp)
		ass_obj.append(temp_obj)

	techno = input()
	result = associateForGivenTechnology(ass_obj, techno)
	for i in result:
		print(i.id)
