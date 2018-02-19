## Given a sequence, find starting position of motif in sequence
string = 'GATATATGCATATACTT'
subString = 'ATAT'
def findAllPosSubStringInString(string,subString):
	lengthSubString = len(subString)
	subStringLocations = []
	for pos in range(0,len(string)-1):
		if(pos+lengthSubString-1 <= len(string)-1):
					subStringExtracted = string[pos:pos+lengthSubString]
					if(subStringExtracted==subString):
						subStringLocations.append(pos)
	return subStringLocations

print(findAllPosSubStringInString(string,subString))
						
						
			
	