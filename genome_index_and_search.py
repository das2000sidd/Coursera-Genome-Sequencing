## This is protoyping of genome indexing using kmer sequences of genome of specific size
## and retrieving start and end of seq in genome for exact matches
genome = 'CGTGCGTGCTT'

def index_genome(genome,size_genome_index):
	size_genome = len(genome)
	offset = 0
	genome_index_dict={}
	while(offset + size_genome_index <= size_genome):
		end_seq = offset + size_genome_index
		actual_seq = genome[offset:end_seq]
		offset_list=[]
		if(actual_seq in genome_index_dict.keys()):
			offset_list.append(genome_index_dict[actual_seq])
			offset_list.append(offset)
			genome_index_dict[actual_seq] = offset_list
		else:
			offset_list.append(actual_seq)
			genome_index_dict[actual_seq]=offset
		offset+=1
	return genome_index_dict

print(index_genome(genome,5))
		
def return_start_end_of_any_kmer(query_seq,genome,size_index):
	genome_indexes = index_genome(genome,size_index)
	aseq_size_as_index = query_seq[0:size_index]
	
	for seq,seq_start in genome_indexes.items():
		if(seq==aseq_size_as_index):
			start_of_genome_match = seq_start
			end_of_genome_match = seq_start+len(query_seq)-1
			
			
			
	return start_of_genome_match,end_of_genome_match
	
print(return_start_end_of_any_kmer('TGCGTG',genome,5))
print(return_start_end_of_any_kmer('GTGCTT',genome,5))

	
		