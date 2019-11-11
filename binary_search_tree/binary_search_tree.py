class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if self.value:
			if value < self.value:
				if self.left is None:
					self.left = BinarySearchTree(value)
				else:
					self.left.insert(value)
			elif value > self.value:
				if self.right is None:
					self.right = BinarySearchTree(value)
				else:
					self.right.insert(value)
		else:
			self.value = value

	def contains(self, target):
		if self.value == target:
			return True
		elif self.value < target:
			if self.right is None:
				return False
			else:
				return self.right.contains(target)
		elif self.value > target:
			if self.left is None:
				return False
			else:
				return self.left.contains(target)

	def get_max(self):
	# 	find largest node
	# keep going right to endpoint
		max = self.value
	# 	loop through list, update max value if going right, until end of tree
	#  max value at end of tree
		while max.right:
			max = max.right
		return max.value

	def for_each(self, cb):
		res = []
		if cb:
			res.append(cb.value)
			res = res + self.for_each(cb.left)
			res = res + self.for_each(cb.right)
		return res