class Product(object):
	def __init__(self, name, type, price, qty):
		self.productName = name
		self.productType = type
		self.unitPrice = price
		self.qtyOnHand = qty


class Store(object):
	def __init__(self, productObjects):
		self.bill = 0
		self.productList = productObjects

	def purchaseProduct(self, name, qty):
		for i in self.productList:
			if i.productName.lower() == name.lower():
				if i.qtyOnHand == 0:
					return None

				if qty > i.qtyOnHand:
					self.bill = i.unitPrice * i.qtyOnHand
					i.qtyOnHand -= 1

				elif qty <= i.qtyOnHand:
					self.bill = i.unitPrice * qty
					i.qtyOnHand -= 1

		return None



if __name__ == "__main__":
	n = int(input())
	productList = []
	for _ in range(n):
		name, type, price, qty = input(), input(), int(input()), int(input())
		productList.append(Product(name, type, price, qty))

	store = Store(productList)
	name = input()
	qtry = int(input())

	product = store.purchaseProduct(name, qtry)
	if not product:
		print("Product not available")
	else:
		print(store.bill)
	
	for product in store.productList:
		print(f"{product.productName} {product.qtyOnHand}")


