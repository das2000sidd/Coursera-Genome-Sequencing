

## Given a collection of kmer patterns, this code generates the adjacency list of the deBruijn graph
import re
import argparse


def Main():
	
	parser = argparse.ArgumentParser(description='This script converts a k mer pattern file to adjacency list')
	parser.add_argument('--kmers_file',nargs='?')
	
	args = parser.parse_args()
	return args

def read_kmers():
	all_returned = []
	all_returned=Main()
	kmer_file=all_returned.kmers_file
	fileRead = open(kmer_file,'r')
	linesRead = ''
	for line in fileRead:
		linesRead+=line
	return linesRead



def line_to_list():
	lines_read = read_kmers()
	line_to_list = re.split('\n',lines_read)
	line_to_list_sorted = sorted(line_to_list)
	return line_to_list_sorted
	


def kmer_to_adj_list():
	kmer_list = line_to_list()
	len_kmer = len(kmer_list[0])
	dict_adj_list = {}
	
	for a_kmer in kmer_list:
		adj_kmer_1 = a_kmer[:len_kmer-1]
		adj_kmer_2 = a_kmer[-(len_kmer-1):]
		list_adj_kmer_2=[]
		
		if(adj_kmer_1 not in dict_adj_list.keys()):
			list_adj_kmer_2.append(adj_kmer_2)
			dict_adj_list[adj_kmer_1]=list_adj_kmer_2
		else:
			list_adj_kmer_2.append(adj_kmer_2) ## append new value
			list_adj_kmer_2.extend(dict_adj_list[adj_kmer_1]) ## since it is already a list
			dict_adj_list[adj_kmer_1] = list_adj_kmer_2
				
			
				
	return dict_adj_list
	
def display_the_adj_list():
	kmer_adj_dict = kmer_to_adj_list()
	for key,value in kmer_adj_dict.items():
		
		value_as_string = ','.join(value)
		print key, '->',value_as_string


				
display_the_adj_list() ## do not put print here or else none is displayed


## python kmer_to_adj_list.py --kmers_file kmers.txt
## where kmers.txt is a text file with one kmer per line

