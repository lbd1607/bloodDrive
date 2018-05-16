#Laura Davis
#26 April 2016
#This program will calculate the number of pints donated during a blood drive. 
#CGP145 Ch08 Lab-4 Blood Drive

#the main function
def main():
	endProgram = 'no'
	print
	while endProgram == 'no':
		print
		# declare variables
		pints = [0] * 7
		totalPints = 0.0
		averagePints = 0.0
		highPints = 0.0
		lowPints = 0.0
    
		# function calls
		pints = getPints(pints)
		totalPints = getTotal(pints)
		averagePints = getAverage(totalPints)
		highPints = getHigh(pints)
		lowPints = getLow(pints)
		displayInfo(averagePints, highPints, lowPints)
	
		endProgram = raw_input('Do you want to end program? (Enter no or yes) --> ')
		while not(endProgram == 'yes' or endProgram == 'no'):
			print 'Please enter a yes or no'
			endProgram = raw_input('Do you want to end program? (Enter no or yes) --> ')

#the getPints function
def getPints(pints):
	counter = 0
	while counter < 7:
		pints[counter] = input('Enter pints collected: ')
		counter = counter + 1
	return pints

#the getTotal function
def getTotal(pints):
	counter = 0
	totalPints = 0
	while counter < 7:
		totalPints = totalPints + pints[counter]
		counter = counter +1
	return totalPints
	
#the getAverage function
def getAverage(totalPints):
	averagePints = totalPints / 7.0
	return averagePints
	
#the getHigh function
def getHigh(pints):
	highPints = pints[0]
	counter = 1
	while counter < 7:
		if pints[counter] > highPints:
			highPints = pints[counter]
		counter = counter + 1
	return highPints
	
#the getLow function
def getLow(pints):
	lowPints = pints[0]
	counter = 1
	while counter < 7:
		if pints[counter] < lowPints:
			lowPints = pints[counter]
		counter = counter + 1
	return lowPints
	
#the displayInfo function
def displayInfo(averagePints, highPints, lowPints):
	print "The average number of pints collected is ", averagePints
	print "The highest pints donated is ", highPints
	print "The lowest pints donated is ", lowPints
	
# calls main
main()
