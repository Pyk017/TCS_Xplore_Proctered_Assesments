class Phone(object):
	"""docstring for Phone"""
	def __init__(self, phoneID, os, brand, price):
		self.phoneID = phoneID
		self.os = os
		self.brand = brand
		self.price = price

	def set_phoneID(self, id):
		self.phoneID = id

	def get_phoneID(self):
		return self.phoneID

	def set_os(self, os):
		self.os = os

	def get_os(self):
		return self.os

	def set_brand(self, brand):
		self.brand = brand

	def get_brand(self):
		return self.brand

	def set_price(self, price):
		self.price = price

	def get_price(self):
		return self.price



def findPriceForGivenBrand(phoneObj, brand):
	total = 0
	for phone in phoneObj:
		if phone.get_brand().lower() == brand.lower():
			total += phone.get_price()

	return total if total > 0 else 0


def getPhoneIdBasedOnOs(phoneObj, os):
	for phone in phoneObj:
		if phone.get_os().lower() == os.lower() and phone.get_price() >= 50000:
			return phone

	return None


if __name__ == '__main__':
	n = int(input())
	phone_obj = []
	for _ in range(n):
		id, os, phone, price = int(input()), input(), input(), int(input())
		phone_obj.append(Phone(id, os, phone, price))

	brand, os = input(), input()
	total_price = findPriceForGivenBrand(phone_obj, brand)
	print(total_price) if total_price > 0 else print('The given Brand is not available.')
	phone_ = getPhoneIdBasedOnOs(phone_obj, os)
	print(phone_.get_phoneID()) if phone_ else print("No phones are available with specified os and price range.")
