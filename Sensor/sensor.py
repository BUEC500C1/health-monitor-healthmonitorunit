import random

def generatedata():
#   generate fake values
  heartrate = random.randint(60,100)
  bloodpressure = [random.randint(60,90),random.randint(90,140)]
  
  dict = {}
  dict['heartrate'] = heartrate
  dict['bloodpressure'] = bloodpressure
  
  return dict
  
