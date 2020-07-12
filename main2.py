class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y
class Size:
	def __init__(self, width, height):
		self.width = width
		self.height = height
class Box:
	def __init__(self, origin:Coordinate, box_size:Size):
		self.origin = origin
		self.size = box_size
class World:
	def __init__(self):
		self.item_list = []
	def add_item(self, item):
		self.item_list.append(item)
	def have_collided(self, item1, item2):
		if item1.location.origin.x + item1.location.size.width < item2.location.origin.x:
			return False
		if item2.location.origin.x + item2.location.size.width < item1.location.origin.x:
			return False
		if item1.location.origin.y + item1.location.size.width < item2.location.origin.y:
			return False
		if item2.location.origin.y + item2.location.size.width < item1.location.origin.y:
			return False
		return True
	def get_collisions(self):
		collisions = []
		for item1 in self.item_list:
			for item2 in self.item_list:
				if item1 != item2 and (item2,item1) not in collisions:
					if self.have_collided(item1,item2):
						collisions.append((item1,item2))
		return collisions
class Item:
	def __init__(self, name):
		self.name = name
		self.location = Box(Coordinate(0,0), Size(3,3))
	def __str__(self):
		return f"{self.name} {self.location}"
debugging = True
def log(text):
	if debugging:
		print(text)
w = World()
add_item = lambda item: w.add_item(item)
get_collisions = lambda : w.get_collisions()
# TESTS
add_item(Item("A"))
add_item(Item("B"))
c = get_collisions()
log(c)
assert( len(c) == 1 )
