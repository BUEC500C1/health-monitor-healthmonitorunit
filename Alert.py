# The input of this func is processed data from func processor()
# The output is the flag to alert by true or false. True means alert, False means as usual
# The func is to compare the processed data with standard data we get from AI module, and relatively to alert or not

import AI

#test01
def alert(ProcessedData):

  #   Call for API from AI module
  standardData = AI.standarData
  if(ProcessedData > standardData):
    return true
  else:
    return false
 
