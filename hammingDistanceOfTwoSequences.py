seqA = 'GAGCCTACTAACGGGAT'
seqB = 'CATCGTAATGACGGCCT'

def findHammingDist(seqA,seqB):
	hammingDist = 0
	if(len(seqA)==len(seqB)):
		for i in range(len(seqA)):
			if(seqA[i]!=seqB[i]):
				hammingDist+=1
	return hammingDist
	

	
print(findHammingDist(seqA,seqB))
				