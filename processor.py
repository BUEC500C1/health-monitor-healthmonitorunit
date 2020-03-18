from sensor import generatedata

def sensor_unit():
  return 0

def processor():
  return 0

import AI

#test01
def alert(ProcessedData):

  #   Call for API from AI module
  standardData = AI.standarData
  if(ProcessedData > standardData):
    return true
  else:
    return false
