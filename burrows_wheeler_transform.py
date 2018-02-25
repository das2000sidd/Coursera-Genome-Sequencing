##This is a python script where given a sequence file, it can generate the burrows wheeler transform
import re
import argparse

def Main():
	
	parser = argparse.ArgumentParser(description='This script converts a sequence to its burrows wheeler transform')
	parser.add_argument('--seq_file',nargs='?')
	
	args = parser.parse_args()
	return args

def read_seq():
	all_returned = []
	all_returned=Main()
	seq_file=all_returned.seq_file
	fileRead = open(seq_file,'r')
	linesRead = ''
	for line in fileRead:
		linesRead+=line
	return linesRead

def line_to_list():
	lines_read = read_seq()
	return lines_read

def append_dollar_return_chars():
	a_string = line_to_list()
	a_string = a_string+"$"
	list_of_char=[]
	for i in range(0,len(a_string)):
		list_of_char.append(a_string[i])
	return list_of_char
	
print(append_dollar_return_chars())

def create_single_rotation_of_string(list_of_char): 
	
	rotated_list_of_char = [0]*(len(list_of_char))
	
	len_list_char = len(list_of_char)
	for i in range(0,len_list_char):
		if(i==len_list_char-1):
			rotated_list_of_char[0]=list_of_char[len(list_of_char)-1]
			
		else:
			rotated_list_of_char[i+1] = list_of_char[i]
	return rotated_list_of_char 		
				
			 
def create_complete_rotation_of_string():
	list_of_char = append_dollar_return_chars()
	
	all_rotations = []
	for i in range(0,len(list_of_char)):
		rotated_list_of_char = create_single_rotation_of_string(list_of_char)
		a_string=''.join(rotated_list_of_char)
		
		all_rotations.append(a_string)
		list_of_char=rotated_list_of_char
	return sorted(all_rotations)

def get_the_burrows_wheeler_transform():
	all_sorted_string_list = create_complete_rotation_of_string()
	burrows_wheeler_transformed_string=""
	for i in range(0,len(all_sorted_string_list)):
		
		burrows_wheeler_transformed_string+=all_sorted_string_list[i][len(all_sorted_string_list[i])-1]
	return 	burrows_wheeler_transformed_string

print('These are all the rotations of the strings')	
print(create_complete_rotation_of_string())
print('This is the burrows wheeler transform')
print(get_the_burrows_wheeler_transform())

## ran using: python burrows_wheeler_transform.py --seq_file seq_sample.txt
