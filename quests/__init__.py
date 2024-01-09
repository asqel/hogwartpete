class Quest:
	def __init__(self, name : str, info : str = "", desc : str = "", data : dict = None, percentage = 0) -> None:
		self.name = name
		self.data = (data if data else {})
		self.info = info
		self.description = desc
		self.pourcentage = percentage 
	
	def copy(self):
		return Quest(self.name, self.info, self.description, self.data.copy)

	def json(self):
		return [self.name, self.info, self.description, self.data]


