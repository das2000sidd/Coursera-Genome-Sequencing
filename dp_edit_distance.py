##This is the dynamic programming solution to edit distance to determine minimum number of changes needed to convert one sequence to other


def editDistance(x,y):
	D=[]
	for i in range(len(x)+1):
		D.append([0]*(len(y)+1))
	for i in range(len(x)+1):
		D[i][0]=i
	for i in range(len(y)+1):
		D[0][i]=i
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			distHor = D[i][j-1] +1
			distVer = D[i-1][j]+1
			if x[i-1] == y[j-1]:
				distDiag = D[i-1][j-1] ## characters match
			else:
				distDiag = D[i-1][j-1]+1
			D[i][j] = min(distHor,distVer,distDiag)
	
	return D[len(x)][len(y)]
	

print(editDistance('AA','AAB'))	
print(editDistance('ABB','BAA'))

print(editDistance('shake spea','Shakespear'))	
print(editDistance('geek','gesek'))
