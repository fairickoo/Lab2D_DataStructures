from termcolor import colored
class Node:

    def __init__(self, data, Next=[], weight=[]):
        self.data = data
        self.weight = [] if weight is [] else weight
        self.Next = [] if Next is [] else Next

    def __str__(self):
        return str(self.data)

l = [1,2,3,4,5,6,7]
adjL = []
for i in l:
    adjL.append(Node(i))

# adjL[1 - 1].Next = [2,4,3]
# adjL[2 - 1].Next = [4,5]
# adjL[3 - 1].Next = [6]
# adjL[4 - 1].Next = [6,7,3]
# adjL[5 - 1].Next = [4,7]
# adjL[7 - 1].Next = [6]

# adjL[1 - 1].weight = [2,1,4]
# adjL[2 - 1].weight = [3,10]
# adjL[3 - 1].weight = [5]
# adjL[4 - 1].weight = [8,4,2]
# adjL[5 - 1].weight = [2,6]
# adjL[7 - 1].weight = [1]

adjL[1 - 1].Next = [adjL[2-1],adjL[4 - 1],adjL[3 - 1]]
adjL[2 - 1].Next = [adjL[4 - 1],adjL[5 - 1]]
adjL[3 - 1].Next = [adjL[6-1]]
adjL[4 - 1].Next = [adjL[6-1],adjL[7 - 1],adjL[3 - 1]]
adjL[5 - 1].Next = [adjL[4 - 1],adjL[7 - 1]]
adjL[7 - 1].Next = [adjL[6-1]]

adjL[1 - 1].weight = [2,1,4]
adjL[2 - 1].weight = [3,10]
adjL[3 - 1].weight = [5]
adjL[4 - 1].weight = [8,4,2]
adjL[5 - 1].weight = [2,6]
adjL[7 - 1].weight = [1]




def print_adj_list(INPUT):
    print('---- Adjacency LIST ----')
    for i in INPUT:
        print(str(i),end=' ')
        for j in i.Next:
            print('>',colored(j,'red'),end=' ')
        print()
    print()

def print_adj_matrix(INPUT):
    print('---- Adjacency MATRIX ----')
    color = ['cyan','magenta']
    in_color = 0
    print(' ',end=' ')
    for i in range(1,len(INPUT)+1):
        print(i,end=' ')
    print()
    for V in INPUT:
        print(str(V),end=' ')
        for i in range(1,len(INPUT)+1):
            
            found = False
            for j in V.Next:
                if i == j.data:
                    print(colored(V.weight[V.Next.index(j)],color[in_color]),end=' ')
                    found = True
            
            if not found:
                print(' ',end=' ')
            # if i in V.Next:
            #     print(colored(V.weight[V.Next.index(i)],color[in_color]),end=' ')
            # else:
            #     print(' ',end=' ')
        print()
        if in_color == 0:
            in_color = 1
        else:
            in_color = 0
    print()

def node(index):
    global adjL
    return adjL[index - 1] 




true_Path = []
def shortPATH(graph ,src, des): #! <----- distance = sum of weight , path = list of passed List/NODE ??????????????????????
    distance = 0
    path = []
    _shotPATH(graph ,src, des, distance, path)
    distance = []
    for i in true_Path:
        distance.append(i[0])
    beforeOUT = true_Path[distance.index(min(distance))]
    strOUT = 'The shortest path \t'+ colored('-','red')
    for i in beforeOUT[1]:
        strOUT +=  colored('-> ','red')+colored(str(i),'green') + ' '
    strOUT += '\nDistance\t\t' + colored('--> ', 'blue') + colored(str(beforeOUT[0]),'yellow')
    return strOUT



def _shotPATH(graph ,src, des, distance, path):
    global true_Path
    path.append(str(src))
    if src == des:
        # print('DISTANCE : ',distance,'\tPATH ->',path)
        true_Path.append([distance, path.copy()])
        path.pop()

    elif len(src.Next) != 0:
        for ele in src.Next:
            # path.append(str(ele))
            path = _shotPATH(graph, ele, des, distance+src.weight[src.Next.index(ele)], path) 
        if len(path) != 0:
            path.pop()
    
    # print(path)
    return path
    


print_adj_list(adjL)
print_adj_matrix(adjL)
print(shortPATH(adjL, node(1), node(6)))

