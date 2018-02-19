
## Given a list of sequences find sequences with highest GC percentage
import re
def readFileOfSequences(fastaSeqFile):
	fileRead = open(fastaSeqFile,'r')
	linesRead = '\n'
	for line in fileRead:
		linesRead+=line
	fileRead.close()
	return linesRead

seqFile =  'Rosalind_Sequences.txt'	


def returnGCPercentBySeqID(fastaSeqFile):
	linesRead = readFileOfSequences(fastaSeqFile)
	linesToList = re.split('>',linesRead)
	seqDict = {}
	for i in range(1,len(linesToList)):
		eachSeq = re.split('\n',linesToList[i])
		seqId = eachSeq[0]
		seqItemsList = eachSeq[1:]
		seqItemsString = ''.join(seqItemsList)
		gcCount = (seqItemsString.count('G') + seqItemsString.count('C'))
		
		gcPercentage = gcCount*100/float(len(seqItemsString)) ## SETTING LEN AS FLOAT WAS CRUCIAL IN GETTING DECIMAL PLACE NUMBER
		seqDict[seqId] = gcPercentage
	
	return seqDict

def returnSeqWithHighestGC(fastaSeqFile):
	
	highestGCPercent = 0
	seqIdToReturn=''
	GCPercentbySeq = returnGCPercentBySeqID(fastaSeqFile)
	for SeqId,GCPercent in GCPercentbySeq.items():
		if GCPercent > highestGCPercent:
			highestGCPercent = GCPercent
			seqIdToReturn = SeqId
	return highestGCPercent,seqIdToReturn
			
	

	

print(returnSeqWithHighestGC(seqFile))