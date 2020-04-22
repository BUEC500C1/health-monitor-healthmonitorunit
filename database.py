# a simple database for health monitor


class database(object):

	def __init__(self):
		self.data = list()
		return self;

	def getdata(self,number):
		length = len(self.data)
		if length<number:
			print("do not have enough data for input number")
			raise NumberErro
		else:
			return self.data[length-number:length]

	def save(self,time,impulse,oxygen):
		self.data.append((time,impulse,oxygen))

	def delete(self,number):
		length = len(self.data)
		if length<number:
			print("do not have enough data to delete")
			raise NumberErro
		else:
			temp = self.data[length-number:length]
			self.data = temp
