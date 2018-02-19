seq1='AAAACCCGGT'

def reverseASeq(seq):
	reverse_seq=''
	for i in range(len(seq)-1,-1,-1):
		reverse_seq = reverse_seq+seq[i]
	return reverse_seq




def getReverseComplement(seq):
	reversedSeq = reverseASeq(seq)
	dictOfComplement = {'A':'T','G':'C','T':'A','C':'G'}
	reverseComplement=''
	for i in range(0,len(reversedSeq)):
		for base1,complement in dictOfComplement.items():
			if  reversedSeq[i]==base1:
				reverseComplement = reverseComplement+complement
	return reverseComplement


print('This is the sequence')
print(seq1)
print('This is the reverse complement')	
print(getReverseComplement(seq1))