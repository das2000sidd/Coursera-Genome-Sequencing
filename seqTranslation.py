## Given a RNA sequence and codon table, generate corresponding translated sequence
import re
def readFileOfCodons(codonFile):
	codonFileRead = open(codonFile,'r')
	linesRead = '\n'
	for line in codonFileRead:
		linesRead+=line
	codonFileRead.close()
	return linesRead

def convertReadCodonFileToDict(codonFile):
	codonFileRead = readFileOfCodons(codonFile)
	linesAsList = re.split('\n',codonFileRead)
	codonDict = {}
	for i in range(1,len(linesAsList)):
		codonsAsList = re.split('\s{2,}',linesAsList[i])
		for eachCodon in codonsAsList:
			codonAndSymbol = re.split('\s',eachCodon)
			codon = codonAndSymbol[0]
			aminoAcidSymbol = codonAndSymbol[1]
			codonDict[codon] = aminoAcidSymbol
		
	return codonDict
	

print(convertReadCodonFileToDict('RNA_Codon_Table.txt'))

print(readFileOfCodons('RNASeqToTranslate.txt'))
print(len(readFileOfCodons('RNASeqToTranslate.txt')))

def convertSeqToCodonList(rnaFile):
	
	rnaSeq = readFileOfCodons(rnaFile)
	rnaSeq = rnaSeq.replace('\n','') ## so zthat new line does not append with character string
	lengthRnaSeq = len(rnaSeq)
	listOfCodons = []
	for i in range(0,(lengthRnaSeq),3):
		aCodon = rnaSeq[i:i+3]
		listOfCodons.append(aCodon)
	return listOfCodons
	
def translateRNASeqToProtein(codonFile,rnaSeqFile):
	codonDict = convertReadCodonFileToDict(codonFile)
	rnaCodonList = convertSeqToCodonList(rnaSeqFile)
	translatedSeq=''
	for eachRNACodon in rnaCodonList:
		for eachCodon,aminoAcid in codonDict.items():
			if(eachRNACodon==eachCodon):
				if(aminoAcid!='Stop'):
					translatedSeq += aminoAcid
				else:
					break
	return translatedSeq
	
	
print(translateRNASeqToProtein('RNA_Codon_Table.txt','RNASeqToTranslate.txt'))
	

			
			
	
	
	
	