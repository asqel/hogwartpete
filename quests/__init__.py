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
		return [self.name, self.info, self.description, self.data, self.pourcentage]

	def from_json(self, d: list):
		self.name = d[0]
		self.data = d[3]
		self.info = d[1]
		self.description = d[2]
		self.pourcentage = d[4]
	
	def __str__(self) -> str:
		return f"Q[{self.name} {self.pourcentage}%]"

	def __repr__(self) -> str:
		return str(self)


