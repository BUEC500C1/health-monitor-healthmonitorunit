from AI_Analysis import AI_Analysis
# Original file author: Ganghao Li (lighao@bu.edu). The original file does not have enough connection with other module, therefore I created two python class
# from line 5 to 55 for alert and warning noticement

class firstAlert(object):
  def __init__(self):
    self.message = ""
    self.dangerousProblem = ["tachycardia ","bradycardia ","hypertension ","hypotension ","hypoxemia "]
    self.threshold = [40, 100,[60, 90],[90, 140],0.9]
    self.time = 0

  def __str__(self):
    return "Alert at "+ str(self.time)+"s : "+self.message

  def check(self, sample):
    limit=self.threshold
    prob=self.dangerousProblem
    currentImpulse = sample[1]
    currentBP = sample[2]
    currentBO = sample[3]
    currentTime = sample[0]

    if currentImpulse <= limit[0]: self.message += prob[1]
    if currentImpulse >= limit[1]: self.message += prob[0]
    if currentBO < limit[4]: self.message += prob[4]
    if currentBP[0]<limit[2][0] and currentBP[1]<limit[2][1]: self.message += prob[3]
    if currentBP[0]>limit[3][0] and currentBP[1]>limit[3][1]: self.message += prob[2]

    if len(self.message) != 0: self.time = currentTime

class laterWarning(object):
  def __init__(self):
    self.message = ""
    self.potentialProblem = ["High HR ","Low HR ","High Blood Pressure ","Low Blood Pressure ","low O2 "]
    self.threshold = [60, 90,[65, 95],[85, 130],0.95]
    self.time = 0

  def __str__(self):
    return "Warning at "+ str(self.time)+"s : "+self.message

  def check(self, sample):
    limit=self.threshold
    prob=self.potentialProblem
    currentImpulse = sample[1]
    currentBP = sample[2]
    currentBO = sample[3]
    currentTime = sample[0]

    if currentImpulse <= limit[0]: self.message += prob[1]
    if currentImpulse >= limit[1]: self.message += prob[0]
    if currentBO < limit[4]: self.message += prob[4]
    if currentBP[0]<limit[2][0] and currentBP[1]<limit[2][1]: self.message += prob[3]
    if currentBP[0]>limit[3][0] and currentBP[1]>limit[3][1]: self.message += prob[2]

    if len(self.message) != 0: self.time = currentTime

def alert(input_impulse, input_pressure, input_oxygen):
  tai = AI_Analysis()
  tip = [66, 77, 88, 99]
  tbp = [[70, 110],
         [75, 130],
         [80, 115],
        [75, 125]]
  tbo = [0.77, 0.62, 0.55, 0.49]
  out = tai.analysis(tip, tbp, tbo, 4)
  future_impulse = out[1]
  future_pressure = out[2][1]
  future_oxygen = out[3]
  #   Call for API from AI module 
  #alarm_boolean, future_impulse, future_pressure, future_oxygen = AI_Analysis.analysis()
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

if __name__ == '__main__':
  alert(213, 134, 0.6)
