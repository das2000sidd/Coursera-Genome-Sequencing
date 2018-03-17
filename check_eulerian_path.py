
##This is code to check if a graph has a eulerian path meaning equal number of outgoing and incoming edges for each node.
graph_with_cycle={'2':['2','3'],'1':['2'],'3':['1']} ## 1 expected output
graph_with_no_cycle = {'1':['2','3'],'2':['3'],'3':['1']} ## 0 expected output
graph_with_cycle_2={'1':['2','4'],'2':['1','4'],'3':['2'],'4':['1','3']} ## 1 expected output
graph_with_cycle3={'1':'2','2':'3','3':'1'}## 1 expected output

def out_in_edges(graph_with_cycle):
	has_cycle=0
	graph_nodes= graph_with_cycle.keys()
	visited=set()
	node_count_dict={}
	for each_node in graph_nodes:
		node_out_degree=len(graph_with_cycle[each_node])
		node_in_degree=0
		for a_node in graph_nodes:
			if each_node in graph_with_cycle[a_node]:
				node_in_degree+=1
		node_count_dict[each_node]=[node_out_degree,node_in_degree]
	return node_count_dict
					
def check_eulerian(graph_with_cycle):
	out_in_edges_dict=out_in_edges(graph_with_cycle)
	is_eulerian=0
	for each_node in out_in_edges_dict.keys():
		degree_values=out_in_edges_dict[each_node]
		out_degree=degree_values[0]
		in_degree=degree_values[1]
		if(out_degree==in_degree):
			is_eulerian=1
		else:
			is_eulerian=0
			break
			
	return is_eulerian	
	
	
	
print('First is out degree and then in degree')
print(out_in_edges(graph_with_cycle))
print(out_in_edges(graph_with_no_cycle))
print(out_in_edges(graph_with_cycle_2))
print(out_in_edges(graph_with_cycle3))

 
print(check_eulerian(graph_with_cycle)) ## 1
print(check_eulerian(graph_with_no_cycle)) ## 0
print(check_eulerian(graph_with_cycle_2)) ## 1
print(check_eulerian(graph_with_cycle3)) ## 1

print('\n')
print('\n')