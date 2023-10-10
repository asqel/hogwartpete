class Quest:
	def __init__(self, name : str, info : str = "", desc : str = "", data : dict = None) -> None:
		self.name = name
		self.data = (data if data else {})
		self.info = info
		self.description = desc
	
	def copy(self):
		return Quest(self.name, self.info, self.description, self.data.copy)

	def json(self):
		return [self.name, self.info, self.description, self.data]


