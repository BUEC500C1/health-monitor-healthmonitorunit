from sensor import generatedata
from database import database
from Alert import alert, firstAlert, laterWarning 
from Monitor import Monitor
from AI_Analysis import AI_Analysis
import time
from termcolor import colored
def pulseSimulation():
	time.sleep(1)
	return generatedata(2)

def Processing(patientRecord):
	AAA = firstAlert()
	BBB = laterWarning()
	AAA.check(patientRecord.getdata(1)[0])
	BBB.check(patientRecord.getdata(1)[0])
	if AAA.message == "":
		if BBB.message != "":
			print(colored(BBB, 'yellow'))
		print(colored("Patient Heart Currently Runs Normally😊",'green')) 
	else:
		print(colored(AAA, 'red'))
	return patientRecord.getdata(1)[0]


def AI(patientRecord, n):
	if len(patientRecord.data) < n:
		return patientRecord.getdata(1)[0]
	historicalSample = patientRecord.getdata(n)
	obj = AI_Analysis()
	tip = []
	tbp = []
	tbo = []
	for samp in historicalSample:
		tip.append(samp[1])
		tbp.append(samp[2])
		tbo.append(samp[3])
	out = obj.analysis(tip, tbp, tbo, n)
	return out



if __name__ == '__main__':
	measurementTime = 100
	currentTime = 0
	patientRecord = database()
	#processedRecord = database()
	#AIRecord = database()
	while (currentTime < measurementTime):
		dictRecord = pulseSimulation()
		impulse = dictRecord['heartrate']
		bPressure = dictRecord['bloodpressure']
		bOxygen = dictRecord['bloodoxygen']
		patientRecord.save(currentTime, impulse, bPressure,bOxygen)
		Mo = Monitor(Processing(patientRecord),AI(patientRecord,4))
		if (currentTime % 4 == 0):
			Mo.show()
		currentTime += 1
