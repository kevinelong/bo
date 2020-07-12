class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y
class Size:
	def __init__(self, widht, height):
		self.width = width
		self.height = height
class Box:
	def __init__(self, origin:Coordinate, box_size:Size):
		self.origin = origin
		self.size = box_size
class World:
	def __init__(self, items:[]):
		self.items = items

class Item:
	def __init__(self, name):
		self.name = name
		self.location = [0,0]
	def __str__(self):
		return f"{self.name} {self.location}"
 
debugging = True

def log(text):
	if debugging:
		print(text)

item_list = []

def add_item(item):
	item_list.append(item)

def get_collisions():
	collisions = []
	for item1 in item_list:
		for item2 in item_list:
			if item1 != item2 and (item2,item1) not in collisions:
				if item1.location == item2.location:
					log(f"collision {item1} {item2}")
					collisions.append((item1,item2))
	return collisions

# TESTS
add_item(Item("A"))
add_item(Item("B"))
assert( len(get_collisions()) == 1 )
