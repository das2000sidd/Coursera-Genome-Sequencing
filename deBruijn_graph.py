## This is a practice solution to the deBruijn graph problem of breaking sequence into overlapping reads of equal size 
## and then using those reads to reconstruct the sequence

import argparse

def Main():
	
	parser = argparse.ArgumentParser(description='This script converts a dna sequence to overlapping reads and reconstructs sequence from those reads')
	parser.add_argument('--seqReads',nargs='?')
	parser.add_argument('--seqFile',nargs='?')
	parser.add_argument('--kmerSize',nargs='?')
	args = parser.parse_args()
	return args

def read_in_seq_command_line():
	all_returned = []
	all_returned=Main()
	seq_file = all_returned.seqFile
	seq_read = open(seq_file,'r')
	seq_to_return=''
	for line in seq_read:
		seq_to_return+=line
	return seq_to_return

##print(read_in_seq_command_line())

def construct_kmer():
	all_returned = []
	all_returned=Main()
	seq = read_in_seq_command_line()
	kmer_size = all_returned.kmerSize
	kmer_size = int(kmer_size)
	seq_length = len(seq)
	kmers_to_return=[]
	if(kmer_size <= seq_length):
		for index in range(0,seq_length):
			start_index = index
			end_index = index+kmer_size
			if(end_index <= len(seq)):
				one_kmer = seq[start_index:end_index]
			##print(start_index)
			##print(end_index)
				kmers_to_return.append(one_kmer)
			else:
				if(end_index > len(seq)):
					break
				
	else:
			return(-1)
		
	return kmers_to_return
	
	
print(construct_kmer())



def merge_any_two_kmer(kmer1,kmer2,size_of_kmer):
	
	stringReturned=''
	
	if(kmer1[-(size_of_kmer-1):]==kmer2[0:size_of_kmer-1]):
		stringReturned = kmer1[0:]+kmer2[size_of_kmer-1]
	return stringReturned

def create_genome_path():
	all_returned = []
	all_returned=Main()
	kmer_size = all_returned.kmerSize
	kmer_size = int(kmer_size)
	kmer_list = construct_kmer()
	
	if(kmer_list!=-1):
		string_to_return = ''
		for i in range(1,len(kmer_list)):
		
			new_merged_kmer = merge_any_two_kmer(kmer_list[0],kmer_list[i],kmer_size)
		
			kmer_list[0]=new_merged_kmer
		return kmer_list[0]
	else:
		return('Kmer size greater than seq size')

		
print(create_genome_path())



if __name__=='__main__':
	Main()
	
## Ran using the following command: python deBruijn_graph.py --seqFile seq_sample.txt --kmerSize 7

## Working on setting argument for building sequence if only reads supplied by user arguments 
