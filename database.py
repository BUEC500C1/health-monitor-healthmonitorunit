# a simple database for health monitor


class database(object):

	def __init__(self):
		self.data = list()

	def getdata(self,number):
		length = len(self.data)
		return self.data[length-number:length]

	def save(self,time,impulse,oxygen):
		self.data.append((time,impulse,oxygen))

	def delete(self,number):
		temp = self.data[length-number:length]
		self.data = temp