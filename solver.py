import rubik
import copy
from collections import deque
from pprint import pprint
import time
start_time = time.time()
#main()

def isEqual(t1,t2):
    if len(t1)!=len(t2):
        return False
    else:
        for i in range(len(t1)):
            if t1[i] != t2[i]:
                return False
    return True

def backtrack(d,pos):

    moves = ""
    temp = pos
    # for i in d:
        # print(i,d[i])
        # print()
    while temp != None:
        # print(temp)
        start = d[temp]
        end = temp
        if start!=None:
            for i in rubik.quarter_twists:
                check = rubik.perm_apply(i,start)
                if check == end:
                    moves += " "+rubik.quarter_twists_names[i]
                    break
        temp = d[temp]
    moves = moves.split()
    return moves[::-1]



def shortest_path(start, end):
    """
    For Question 1, using BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """

    moves = ""
    visited = dict()
    bfs = deque()
    pair = (start,0)
    bfs.append(pair)
    depth = 0
    parents = dict()
    parents[start] = None
    while depth<=14 and len(bfs)>0:
        # print("start",bfs[0])
        p = bfs[0]
        pos = p[0]
        # print(pos)
        
        depth =  p[1]

        for i in rubik.quarter_twists:
            newpos = rubik.perm_apply(i,pos)
            # tempmove = copy.deepcopy(move)
            # tempmove.append(rubik.quarter_twists_names[i])
            
            if newpos==end:
                parents[newpos] = pos
                return backtrack(parents,newpos)
            visitflag = False
            
            if newpos in visited:
                visitflag = True
            if not visitflag:
                bfs.append((newpos,depth+1))
                parents[newpos] = pos
        
        # print(len(bfs))
        visited[pos] = ""
        bfs.popleft()
        # print("end",bfs[0])

        
    return "not possible"
    raise NotImplementedError

def invert(s):
    s = list(s.split())
    # print(s)
    for i in range(len(s)):
        has_i = s[i].find('i')
        if has_i==-1:
            s[i] = s[i]+'i'
        else:
            s[i] = list(s[i])
            s[i].pop(-1)
            s[i] = "".join(s[i])
        # print(s)
    return s[::-1]

def shortest_path_optmized(start, end):
    """
    For Question 2, using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    
    move_front = ""
    move_back = ""
    depth = 0
    bfs_front = deque()
    bfs_back = deque()
    bfs_front.append((start,move_front,depth))
    bfs_back.append((end,move_back,depth))
    visited_front = dict()
    visited_back = dict()
    parents = dict()
    parents[start] = None
    while depth<=7 :
        node_front = bfs_front[0]
        pos_front = node_front[0]
        mov_front = node_front[1]
        depth = node_front[2]

        node_back = bfs_back[0]
        pos_back =  node_back[0]
        mov_back = node_back[1]
        

        for i in rubik.quarter_twists:
            newpos_front = rubik.perm_apply(i,pos_front)
            temp_mov_front = mov_front + " "+ rubik.quarter_twists_names[i]
            if newpos_front==end:
                
                return temp_mov_front.split()
            if newpos_front in visited_back:
               

                return temp_mov_front.split() + invert(visited_back[newpos_front])
            visitflag_front = False
            if newpos_front in visited_front:
                visitflag_front = True
            if visitflag_front == False:
               
                bfs_front.append((newpos_front,temp_mov_front,depth+1))
                
            
            newpos_back = rubik.perm_apply(i,pos_back)
            temp_mov_back = mov_back + " "+ rubik.quarter_twists_names[i]

            if newpos_back==newpos_front:
                
                return temp_mov_front.split() + invert(temp_mov_back)

            if newpos_back == start:
                
                return invert(temp_mov_back)
            if newpos_back in visited_front:
                
                return visited_front[newpos_back].split() + invert(temp_mov_back)
            visitflag_back = False
            if newpos_back in visited_back:
                visitflag_back = True
            if visitflag_back == False:
                
                bfs_back.append((newpos_back,temp_mov_back,depth+1))
                
        
        visited_back[pos_back] = mov_back
        visited_front[pos_front] = mov_front
        bfs_back.popleft()
        bfs_front.popleft()


    
    return "None(not possible)"
    raise NotImplementedError


# rubik.perm_apply()
# print(rubik.quarter_twists_names)
start = (6, 7, 8, 0, 1, 2, 9, 10, 11, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
end = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
start5 =(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)

start1 = (6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23)
end1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
start2 = (5,3,4,16,17,15,13,14,12,8,6,7,1,2,0,19,20,18,10,11,9,21,22,23)

start3 = (7, 8, 6, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23)
end3= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
start4 = (15, 16, 17, 20, 18, 19, 9, 10, 11, 8, 6, 7, 12, 13, 14, 3, 4, 5, 2, 0, 1, 21, 22, 23)
# print(rubik.perm_inverse(start))
# print(rubik.quarter_twists_names)
print(len(rubik.quarter_twists))
# print(rubik.perm_apply(start,rubik.quarter_twists['Fi']))
# for i in rubik.quarter_twists:
#     print(rubik.quarter_twists[i])
# print(invert("F Fi"))
print(shortest_path(start5,end))

#print(shortest_path_optmized(start3,end))
print("--- %s seconds ---" % (time.time() - start_time))