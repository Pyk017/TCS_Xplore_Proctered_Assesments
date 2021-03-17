class Items(object):
	def __init__(self, name, type, price):
		self.itemName = name
		self.itemType = type
		self.unitPrice = price


class Store(object):
	def __init__(self):
		self.itemInventory = dict()

	def buyItem(self, name, quantity):
		for i, j in self.itemInventory.items():
			if name.lower() == i.itemName.lower() and j == 0:
				return None

			if name.lower() == i.itemName.lower() and quantity > j:
				bill = i.unitPrice * j
				self.itemInventory[i] = 0
				return bill

			elif name.lower() == i.itemName.lower() and quantity <= j:
				bill = i.unitPrice * quantity
				self.itemInventory[i] = j - quantity
				return bill

		return None


if __name__ == '__main__':
	n = int(input())
	store = Store()
	temp_dict = {}
	for _ in range(n):
		name, type, uprice, stock = input(), input(), int(input()), int(input())
		store.itemInventory[Items(name, type, uprice)] = stock

	m = int(input())
	order = {}
	for _ in range(m):
		name, quantity = input(), int(input())
		order[name] = quantity

	for itemName, itemQuant in order.items():
		bill = store.buyItem(itemName, itemQuant)
		if not bill:
			print(f'{itemName} is not available')
		else:
			print(f'Bill of the item {itemName} = {bill}')

	print("Stock in Hand:")
	for item, stock in store.itemInventory.items():
		print(f'{item.itemName} {stock}')


