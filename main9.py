import time
class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y
class Size:
	def __init__(self, width, height):
		self.width = width
		self.height = height
class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
class Box:
	def __init__(self, origin:Coordinate, box_size:Size):
		self.origin = origin
		self.size = box_size
class Item:
	def __init__(self, name:str, location:Box, direction:Vector):
		self.name = name
		self.location = location if location is not None else Box(Coordinate(0,0), Size(3,3))
		self.direction= direction if direction is not None else Vector(0,0)
	def __str__(self):
		return f"{self.name} {self.location}"
class World:
	def __init__(self):
		self.item_list = []
		self.bounds = Box(Coordinate(-10,-10), Size(35,20))
	def value_at(self,x,y):
		pixel = Item("",Box(Coordinate(x,y),Size(1,1)),Vector(0,0))
		for item in self.item_list:
			if self.have_collided(pixel,item):
				return item.name
		return "."
			
	def __str__(self):
		rows = []
		origin = self.bounds.origin
		for r in range(0,self.bounds.size.height):	
			row = []	
			for c in range(0,self.bounds.size.width):
				row.append(self.value_at(c + origin.x, r + origin.y))
			rows.append(" ".join(row))	
		return "\n".join(rows)
	def add_item(self, item):
		self.item_list.append(item)
	def have_collided(self, item1, item2):
		if item1.location.origin.x + item1.location.size.width <= item2.location.origin.x:
			return False
		if item2.location.origin.x + item2.location.size.width <= item1.location.origin.x:
			return False
		if item1.location.origin.y + item1.location.size.height<= item2.location.origin.y:
			return False
		if item2.location.origin.y + item2.location.size.height <= item1.location.origin.y:
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
	def ellapsed(self, moments):
		collisions = self.get_collisions()
		for c in collisions:
			item = c[1]
			other = c[0]
			if item.name == "O":
				if other.name == "-":
					item.direction.y *= -1
					item.location.origin.y += item.direction.y
				if other.name == "|":
					item.direction.x *= -1
					item.location.origin.x += item.direction.x
		for item in self.item_list:
			if item.direction is not stationary:
				item.location.origin.x += item.direction.x
				item.location.origin.y += item.direction.y
# TESTS
stationary = Vector(0,0)
w = World()
add_item = lambda item: w.add_item(item)
get_collisions = lambda : w.get_collisions()
wbo = w.bounds.origin
wbs = w.bounds.size
add_item(Item("-",Box(Coordinate(wbo.x+1,wbo.y), Size(wbs.width-2,1)),stationary))
add_item(Item("|",Box(Coordinate(wbo.x, wbo.y+1), Size(1,wbs.height-2)),stationary))
add_item(Item("|",Box(Coordinate(wbo.x+wbs.width-1,wbo.y+1), Size(1,wbs.height-2)),stationary))
add_item(Item("-",Box(Coordinate(wbo.x+1, wbo.y+wbs.height-1), Size(wbs.width-2,1)),stationary))
add_item(Item("O",Box(Coordinate(-3,-3), Size(2,2)),Vector(1,-1)))
def clear():
	for i in range(100):
		print("")
clear()
print(w)
for i in range(0,999):
	time.sleep(0.1)
	clear()
	print(w)
	w.ellapsed(1)
