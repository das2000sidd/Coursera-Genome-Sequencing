
## This is practice script for reading in FastQC and doing some QC such as GC content
import matplotlib.pyplot as plt
import collections


def readFastQ(filename):
	sequences=[]
	qualities=[]
	with open(filename) as fh:
		while True:
			fh.readline()
			seq=fh.readline().rstrip()
			fh.readline()
			qual = fh.readline().rstrip()
			if len(seq)==0:## end of file check
				break
			sequences.append(seq)
			qualities.append(qual)
	return sequences,qualities
	
	


seqs,quals=readFastQ('shorter.fastq')


def phred33ToQ(qual):
	return ord(qual)-33 ## ord returns for a string of length one 
	## the unicode code point of the character when argument is unicode object
	
print(phred33ToQ('#'))
print(phred33ToQ('J'))

def createHist(qualities):
	hist=[0]*50
	for qual in qualities:
		for phred in qual:
			q=phred33ToQ(phred)
			hist[q]+=1
	return hist
	
h=createHist(quals)
print(h)



def findGCByPos(reads):
	gc = [0]*36
	totals = [0]*36
	for read in reads:
		for i in range(len(read)):
			if read[i]=='C' or read[i]=='G':
				gc[i] +=1
			totals[i]+=1
	for i in range(len(gc)):
		if(totals[i] > 0):
			gc[i] /= float(totals[i])
	return gc
	
gc = findGCByPos(seqs)
print(gc)

plt.plot(range(len(gc)),gc)
plt.show()

count = collections.Counter()
for seq in seqs:
	count.update(seq)
	
print(count)