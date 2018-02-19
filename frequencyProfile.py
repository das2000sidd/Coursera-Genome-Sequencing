import re
def readSeqFile (seqFile):
	seqFileRead = open(seqFile,'r')
	linesRead = '\n'
	for line in seqFileRead:
		linesRead+=line
	seqFileRead.close()
	return linesRead
	


def convertSeqFileToDict(seqFile):
	fileRead = readSeqFile(seqFile)
	linesToList = re.split('\n',fileRead)
	linesToList = linesToList[1:]
	return linesToList
	
def makeSeqDictById(seqFile):
	linesToList = convertSeqFileToDict(seqFile)
	seqIdDict={}
	for i in range(0,len(linesToList)-1,2):
		seqIdDict[linesToList[i]] = linesToList[i+1]
	return seqIdDict	

def getListOfSequences(seqFile):
	seqByIdDict = makeSeqDictById(seqFile)
	seqList = []
	
	for key,value in seqByIdDict.items():
		value = re.findall('\w',value)
		seqList.append(value)
	return seqList

def countOfABaseForAllPos(anyBase,seqFile):
	baseListPerSeq = getListOfSequences(seqFile)
	
	dictOfBaseCount={}
	countsForABase = []
	## looping over per position 
	for i in range(0,len(baseListPerSeq[0])):
		countOfBasePerColumn=0
		## looping over per sequence
		for j in range(0,len(baseListPerSeq[0])-1):
			if(baseListPerSeq[j][i]==anyBase):
				countOfBasePerColumn +=1
		countsForABase.append(countOfBasePerColumn)
		dictOfBaseCount[anyBase] = countsForABase			
		
	return dictOfBaseCount
		
		
def countOfAllBaseForPerPosForAllSeq(allBaseList,seqFile):
		listForAllBases = []
		for aBase in allBaseList:
			dictOfBaseCountPerBase = countOfABaseForAllPos(aBase,seqFile)
			listForAllBases.append(dictOfBaseCountPerBase)
		return listForAllBases
	


	
print(countOfAllBaseForPerPosForAllSeq(['A','C','G','T'],'buildFrequencyProfileOfSequences.txt'))	