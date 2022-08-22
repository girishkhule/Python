from expand import expand
import queue as Que

class Entry(object):
    def __init__(self, Loc, path, h, g):
        self.Loc = Loc
        self.path = []
        self.path = path
        self.h = h
        self.g = g
        self.f = h + g
        
def a_star_search ( diss_map, time_map, start, end):
    path = []
    # call the imported function expand to get the next list of nodes
    Locs =  diss_map.keys()  # Checks if the Locs passed in are in the map
    if start not in Locs or end not in Locs:
        return []
    currentPath = []
    closed = []
    currentPath.append(start)
    q = Que.PriorityQueue()
    currentLoc = start
    currentDist = 0
    found = 0
    # used to track number of opened nodes
    while currentLoc != end and found == 0:
        if currentLoc not in closed:
            next = expand(currentLoc, time_map)
            closed.append(currentLoc)
            # open += 1
            if next:  # if not dead end
                for i in next:  # For each next Loc
                    try:
                        h =  diss_map[i][end]
                        g = currentDist + time_map[currentLoc][i]
                        f = int(h + g)
                        new_Entry = Entry(i, currentPath + [i], h, g)
                        q.put((f, i, new_Entry))
                    except KeyError:
                        print('location in Time Map & Distance Map are incompatible.')
        if not q.empty():  # next queue path 
            nextQueue= q.get()[2]
            currentLoc = nextQueue.Loc
            currentDist = nextQueue.g
            currentPath = nextQueue.path
        else:
            currentPath=[]
            found = 1
    path = currentPath
    return path


def depth_first_search(time_map, start, end):
	        
        nodes = list(time_map.keys())  # intiallize node
        graph = {}
        for i in nodes:  # loop over each nodes
                edge = expand(i, time_map) # calling expand function
                if i in graph:  
                    graph[i].append(edge) # append in graph
                else:
                    graph[i] = edge
    
        stack = [(start, [start])]
        visited = set()  # Set to keep track of visited nodes of graph.
        while stack:  # child traverse
                (vertex, path) = stack.pop() 
                if vertex not in visited:
                    if vertex == end:
                        return path
                    visited.add(vertex)
                    for neighbor in graph[vertex]:
                        stack.append((neighbor, path + [neighbor]))


def breadth_first_search(time_map, start, end):
    import queue  
    src=start  # Start node 
    q1=queue.Queue()  # add the 0th node in our queue as that is our starting point
    visited=[]  # dont want to revisit the same index
    level={}    # depth of search  (traverse)
    parent={}   # branch
    bfs=[]
    # let's add every possible value that has the same value as the current one to our list to visit
    for node in time_map.keys():  
        parent[node]=None
        level[node]=-1
    q1.put(start)
    level[src]=0
    while not q1.empty():
        v=q1.get()
        visited.append(v)
        bfs.append(v)
        # If not visited, mark it as visited, and enqueue it
        for key in time_map[v]:
        	if (time_map[v][key]!=None) and key not in visited : 
                    visited.append(key)
                    parent[key]=v
                    level[key]=level[v]+1
                    q1.put(key)

    v=end
    path=[]
    while v is not None: #Getting the final path and reverse it
        path.append(v)  
        v=parent[v]
    path.reverse()

    return path
	
