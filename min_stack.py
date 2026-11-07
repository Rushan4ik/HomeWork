class Stack:
	def __init__(self):
		self.items: list[int] = []
		self.minimum: list[int] = []
	
	def push(self, num: int) -> None:
		self.items.append(num)
		if not self.minimum:
			self.minimum.append(num)
		else:
			self.minimum.append(num if num<self.minimum[-1] else self.minimum[-1])
	def pop(self):
		if not len(self.items):
			raise IndexError("Stack empty")
		self.minimum.pop()
		return self.items.pop()
	def top(self):
		return self.items[-1]
	def get_min(self):
		if not self.minimum:
			raise IndexError("stack empty")
		return self.minimum[-1]
