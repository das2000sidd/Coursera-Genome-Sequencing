
## this is dynamic programming approach to longest common subsequence
def longest_common_subseq_len(string1,string2):
	DP_matrix=[]
	for i in range(0,len(string1)+1):
		a_List = [0]*(len(string2)+1)
		DP_matrix.append(a_List)
	
	for i in range(1,len(string1)+1):
		for j in range(1,len(string2)+1):
			if(string1[i-1]==string2[j-1]): ## THIS WAS CRUCIAL IN THAT INDEX OF STRING IS ONE LESS THAN CELL TO FILL
				DP_matrix[i][j] = 1+DP_matrix[i-1][j-1]
			else:
				nums_to_compare=[DP_matrix[i-1][j],DP_matrix[i][j-1]]
				DP_matrix[i][j] = max(nums_to_compare)
				nums_to_compare=[]
	return DP_matrix[len(string1)][len(string2)]
	
print(longest_common_subseq_len('ABACE','ADBAVCEB'))
			