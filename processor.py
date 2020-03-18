from sensor import generatedata

def sensor_unit():
  return 0

def processor():
  return 0
######################
def generatedata():
#   generate fake values
  heartrate = random.randint(60,100)
  bloodpressure = [random.randint(60,90),random.randint(90,140)]
  
  dict = {}
  dict['heartrate'] = heartrate
  dict['bloodpressure'] = bloodpressure
  
  return dict
##################
import AI

#test01
def alert(ProcessedData):

  #   Call for API from AI module
  standardData = AI.standarData
  if(ProcessedData > standardData):
    return true
  else:
    return false
  
#below are just draft saved since it might be easy to work when offline
######################
  def ai(impulse, blood_pressure, blood_oxygen, nn):
  # get latest nn groups of input from database
  # if nn == null or nn <= 0 or any one of input is null:
  # . throw WRONG_INPUT
  
  # make some analysis
  
  # may raise alert..
  
  # return future['impulse', 'blood_pressure', 'blood_oxygen']
  
  pass
#############################
import random

def monitor(AI_data, flag=null):
  
def show(res):
