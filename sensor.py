import random

def generatedata(n):
#   generate fake values
  heartrate = random.randint(60,100)
  bloodpressure = [random.randint(60,90),random.randint(90,140)]
  bloodoxygen = round(random.uniform(0.85,0.99),n)
  
  dict = {}
  dict['heartrate'] = heartrate
  dict['bloodpressure'] = bloodpressure
  dict['bloodoxygen'] = bloodoxygen
  
  return dict
  
if __name__ == '__main__':
	print(generatedata())

