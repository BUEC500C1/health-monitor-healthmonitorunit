# The input of this func is processed data from func processor()
# The output is the flag to alert by true or false. True means alert, False means as usual
# The func is to compare the processed data with standard data we get from AI module, and relatively to alert or not

import AI_Analysis

def alert(input_impulse, input_pressure, input_oxygen):

  #   Call for API from AI module 
  alarm_boolean, future_impulse, future_pressure, future_oxygen = AI_Analysis.analysis()

  flagAlert = False
  
  #   Compare data from AI with input data, and decide alert or not
  
  if(input_impulse > future_impulse):
    flagAlert = True
    print("impulse is beyongd standard value !")
   
  if(input_pressure > future_pressure):
    flagAlert = True
    print("pressure is beyongd standard value !")
 
  if(input_oxygen > future_oxygen):
    flagAlert = True
    print("oxygen is beyongd standard value !")
    
  return flagAlert

