# a simple database for health monitor


class database(object):

	def __init__(self):
		self.data = list()
		return self;
	def __str__(self):
		return "database has" str(len(self.data)) + "pieces data"

	def getdata(self,number):
		length = len(self.data)
		if length<number:
			print("do not have enough data for input number")
			raise NumberError
		else:
			return self.data[length-number:length]
		
	def getdatabytime(self,time):
		for d in self.data:
			if d[0] == time:
				return d
		return None

	def save(self,time,impulse,oxygen):
		self.data.append((time,impulse,oxygen))

	def deletenew(self,number):
		length = len(self.data)
		if length<number:
			print("do not have enough data to delete")
			raise NumberError
		else:
			temp = self.data[0:length-number]
			self.data = temp
	def deleteold(self,number):
		length = len(self.data)
		if length<number:
			print("do not have enough data to delete")
			raise NumberError
		else:
			temp = self.data[number:length]
			self.data = temp
