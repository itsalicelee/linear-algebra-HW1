import sys
from graph_gen import *
from p1 import p1_has_cycle
import networkx as nx
import time
start_time = time.time()

def main():
    
    p1_list = list()
    if len(sys.argv) <= 1:
        p1_list = get_p1('r07')
    else:
        p1_list = get_p1(sys.argv[1])
        
    p1_list_converted = convert_p1(p1_list)
    for i in range(len(p1_list)):
        graph = nx.DiGraph(p1_list[i])
        has_cycle = True
        try:
            res = nx.find_cycle(graph)
        except:
            has_cycle = False

        #print("result is:", p1_has_cycle(p1_list_converted[i]))
        #print("the answer is", has_cycle)

        if p1_has_cycle(p1_list_converted[i]) != has_cycle:
            print('Bug in the {}th graph. P1.'.format(i))
    
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
