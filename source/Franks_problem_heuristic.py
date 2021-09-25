import simplegui
import math
import random
import codeskulptor

codeskulptor.set_timeout(10)
# Some global variables
xmax = 800 #horizontal size of window
ymax = 600 # vertical size of window
n = 30 # default number of random segments for random_map()
temp = [] # saves the current input pair of points by mouse click
route_mode = False # is True when the user draws a route in Game Mode: on
#current_route = []
opt_length = 0 # the length of the guarding route
total_length = 0 # the lenght of guarded segments
first_loop = True
second_loop = False
wolfie_pos = [780,20]
wolfie_vel = [0,0]
wolfie_size = (32,32)
factor = float(1)/90
start = False
counter = 0
score = 0
unguarded_length = 100
    
#-------------------------------------------------------------------------- 
# Helper functions
def sorting(List, n):
    # sorts a list of tuples, according to the nth entry
    idx_list = [[List[i][n],i] for i in range (len(List))]
    idx_list.sort()
    sorted_list = [List[idx_list[i][1]] for i in range (len(idx_list))]
    return sorted_list

def orientation(p1 ,p2):
    # determines if [p1,p2] is horizontal or vertical
    if p1[0] == p2[0] and p1[1] != p2[1] :
        seg_type = 'v'
    elif p1[1] == p2[1] and p1[0] != p2[0]:
        seg_type = 'h'
    else:
        seg_type = "neither" 
    return seg_type

def classify(points):
    # creates horizontal and vertical segment lists
    # segment: (p1,p2,[intersected],color,'h'/'v', idx, equiv. class, min_most, length)"""
    vertical = []
    horizontal = []
    i = j = 0
    for i in range(len(points)):
        p1 = points[i][0]
        p2 = points[i][1]
        l = length(points[i])
        segment_type = orientation(p1, p2)
        if segment_type == 'v':
            if p1[1] < p2[1]:
                vertical.append([p1, p2, [], 'white', 'v', i,p1[0], p1[1], l])
            else:
                vertical.append([p2, p1, [], 'white', 'v', i,p1[0], p2[1], l])
            i += 1
        elif segment_type == 'h':
            if p1[0] < p2[0]:
                horizontal.append([p1, p2, [], 'white', 'h', j, p1[1], p1[0], l])
            else:
                horizontal.append([p2, p1, [], 'white', 'h', j, p1[1], p2[0], l])
            j += 1
    return [horizontal, vertical]

def equivalence(List,n):
    # groups elements of a list by their nth entry
    dictionary = {}
    if len(List) > 0:
        dictionary[0] = [List[0]]
        j = 0
        for i in range(len(List)-1):
            if List[i+1][n] == dictionary[j][0][n]:
                dictionary[j].append(List[i+1])
            else:
                j +=  1
                dictionary[j]=[List[i+1]]
    return dictionary

def overlap(ab, cd):
    # evaluates if two real segments intersect
    output = False
    if ab[0] <= cd[0] <= ab[1]:
        if ab[1] <= cd[1]:
            output = True
        if cd[1] <= ab[1]:
            output = True
    if cd[0] <= ab[0] <= cd[1]:
        if ab[1] <= cd[1]:
            output = True
        if cd[1] <= ab[1]:
            output = True
    return output

def merge(x, y):
    # merges two collinear segments if they overlap
    if x[4]=='v':
        temp = sorting([x[0], x[1], y[0], y[1]],1)
        m = temp[0][1]
    elif x[4]=='h':
        temp = sorting([x[0], x[1], y[0], y[1]],0)
        m = temp[0][0]
    return [temp[0],temp[-1], [], x[3], x[4], x[5], x[6], m, length((temp[0],temp[-1]))]
    
def list_seg_merge(L):
    # merges overlapping collinear segments in a list 
    seg_merge = L[0]
    flag=0
    temp=[]
    for i in range (1,len(L)):
        if L[i][4]==seg_merge[4] and intersect(L[i],seg_merge):
            seg_merge = merge(seg_merge, L[i])
        else:
            temp.append(seg_merge)
            seg_merge = L[i]
    temp.append(seg_merge)
    return temp
    
def length(seg):
    # calculates the length of a line segment
    if seg[0][0] == seg[1][0]:
        d = seg[1][1] - seg[0][1]
    elif seg[0][1] == seg[1][1]:
        d = seg[1][0] - seg[0][0]
    return abs(d)

def intersect(x, y):
    # checks if two segments intersect
    check1 = overlap((x[0][1], x[1][1]), (y[0][1], y[1][1]))
    check2 = overlap((x[0][0], x[1][0]), (y[0][0], y[1][0]))
    return check1 and check2

def check_intersect(seg, List):
    # checks intersections between a segment and a list of segments
    seg[2] = []
    for i in range(len(List)):
            if intersect(seg, List[i]):
                seg[2].append(List[i][4]+str(i))
                
def printlist(List):
    # prints a list
    for x in range(len(List)):
        print List[x]        

def eq_class_sort(dictionary,n):
    # sorts equivalence classes, by nth entry, in dictionary
    j = 0
    for k in range(len(dictionary)):
        dictionary[k] = sorting(dictionary[k],n)
        for i in range(len(dictionary[k])):
            dictionary[k][i][5] = j 
            j += 1
    return dictionary

def extract(dictionary):
    # extracts all elements of its lists and store them in a single list
    temp = []
    for i in range(len(dictionary)):
        temp += dictionary[i]      
    return temp

def random_segment(seg):
    # constructs a random segment based in (p1,p2) 
    p1 = seg[0]
    p2 = seg[1]
    flag = random.randint(0,1)
    x2 = 20*(random.randint(20, xmax-20)//20)
    y2 = 20*(random.randint(20, ymax-20)//20)
    if orientation(p1, p2) != 'h':
        [p1, p2] = sorting([p1, p2], 1)
        y1 = 20*(random.randint(p1[1], p2[1])//20)
        q1 = (p1[0], y1)
        if flag == 0:            
            q2 = (x2, y1)
        else:
            q2 = (p1[0], y2)
    elif orientation(p1, p2) != 'v':
        [p1, p2] = sorting([p1, p2], 0)
        x1 = 20*(random.randint(p1[0], p2[0])//20)
        q1 = (x1, p1[1])
        if flag == 0:
            q2 = (x2, p1[1])
        else:
            q2 = (x1, y2)
    ran_seg = [q1, q2]       
    if flag == 1:
        ran_seg = sorting(ran_seg, 1)
    else:
        ran_seg = sorting(ran_seg, 0)
    return ran_seg

def set_random_seg(seg, n):
    # constructs incrementally a set of n random segs from (p1, p2)
    temp = [seg]
    for i in range(n):
        current_seg = random_segment(temp[i])
        temp.append(current_seg)
    return temp

def split(seg, H, V):
    # creates the chopped version of a segment by its intersections (incidents)
    seg_chopped = []
    if seg[4]=='v':
        check_intersect(seg, H)
        z=seg[0][1]
        for x in seg[2]:
            incident = H[int(x[1])]
            if incident[0][1] != z and incident[0][1] != seg[1][1]:
                seg_chopped.append([(seg[0][0], z), (seg[0][0], incident[0][1])])
                z = incident[0][1]
        seg_chopped.append([(seg[0][0], z), seg[1]])
    if seg[4]=='h':
        check_intersect(seg, V)
        z=seg[0][0]
        for x in seg[2]:
            incident = V[int(x[1])]
            if incident[0][0] != z and incident[0][0] != seg[1][0]:
                seg_chopped.append([(z, seg[0][1]), (incident[0][0], seg[0][1])])
                z = incident[0][0]
        seg_chopped.append([(z, seg[0][1]), seg[1]])
    return seg_chopped

def color_cce(List, cce, avoid_color, desired_color):
        # colors cce with desired_color, except for the avoid_color segments
        for seg in List:
            if seg[9] == cce and seg[3] != avoid_color:
                seg[3] = desired_color 
        return List
               
def cce_label(List):
    # sets labels according to cce for coloring purposes
    j=0
    List[j].append('cce'+List[j][4]+str(j))
    for i in range(len(List)-1):
        if List[i+1][4] == List[i][4] and intersect(List[i+1], List[i]):
            List[i+1].append(List[i][9])
        else:
            j += 1
            List[i+1].append('cce'+List[i+1][4]+str(j))
    return List

def cce_graph(List):
    # retrieves a list the cce and its cardinality to construct graph
    temp = List[0][9]
    temp_list = {}
    k = 1
    for i in range(len(List)-1):
        if List[i+1][9] == temp:
            k += 1
        else:
            temp_list[temp] = k
            k = 1
            temp = List[i+1][9]
    temp_list[temp] = k
        
    return temp_list

def make_dictionary(List):
    # creates a dictionary of the list of segments
    seg_dictionary={}
    cce = cce_graph(List)
    antecesor = []
    sucesor = []
    for i in range(len(List)):
        if i > 0 and List[i-1][9] == List[i][9]:
            List[i][2].append(List[i-1][4]+str(List[i-1][5]))
        if i < len(List)-1 and List[i+1][9] == List[i][9]:
            List[i][2].append(List[i+1][4]+str(List[i+1][5]))
        weight = List[i][8] # the length of the segment 
        List[i].append(float(weight)/cce[List[i][9]]) # assigning weights to segments
        seg_dictionary[List[i][4]+str(List[i][5])] = List[i]
    return seg_dictionary

def feasible_neighbor(seg, dictionary):
    # checks if seg has unguarded neighbors (white)
    for x in seg[2]:
        if dictionary[x][3] == 'white':
            return True
            
def tail_test(seg, dictionary):
    # checks that a segment is not a tail in Map
    temp = set()
    for x in seg[2]:
        if dictionary[x][9] != seg[9]:
            temp.add(dictionary[x][9])
    if len(temp) == 2:
        return True
    else:
        return False
    
def next_route_seg(seg, dictionary):
    # tests seg to check if it can be added to the route
    if feasible_neighbor(seg, dictionary) and seg[3]!='lime':
            if tail_test(seg, dictionary):
                return True
            else:
                return False
    else:
        return False
    
def wolfie_bot(seg):
    # displays wolfie bot on screen!
    global wolfie_pos, wolfie_vel 
    wolfie_pos = [seg[0][0], seg[0][1]]
    wolfie_vel = [seg[1][0]-seg[0][0], seg[1][1]-seg[0][1]]
    wolfie_vel = [factor*wolfie_vel[0], factor*wolfie_vel[1]]
    
#--------------------------------------------------------------------------
# Map class. Is a list of segments: vertical and horizontal, storing 
# information of connectivity, length, etc. 
# CCE = Connected Class of Equivalence
class Map:
    def __init__(self, points=[]):
        # initializes Map object
        self.points = points
        self.horizontal = {} # a dictionary for horizontal CCE's
        self.vertical = {} # a dictionary for vertical CCE's
        self.H = [] # list of horizontal segments in lexicographical order
        self.V = [] # list of vertical segments in lexicographical order
        self.color = 'white' # default color of Map
        self.split_mode = False
                            
    def __class_of_equivalence(self):
        # static method that creates the CCE's for H and V
        temp = classify(self.points)
        self.horizontal = equivalence(sorting(temp[0], 6),6)
        self.vertical = equivalence(sorting(temp[1], 6),6)
        self.__lexicographic()
        self.__merge()
        self.H = extract(self.horizontal)
        self.V = extract(self.vertical)
            
    def __lexicographic(self):
        # static method that sorts lexicographically both dictionaries
        self.horizontal = eq_class_sort(self.horizontal,7)
        self.vertical = eq_class_sort(self.vertical,7)
        
    def __merge(self):
        # static method, merges overlapping segments within each CCE
        if not self.split_mode:
            for i in range(len(self.horizontal)):
                self.horizontal[i]=list_seg_merge(list(self.horizontal[i]))
            for i in range(len(self.vertical)):
                self.vertical[i]=list_seg_merge(list(self.vertical[i]))
        self.__lexicographic()
        
    def __intersections(self):
        # static method, updates the intersections of Map's segments
        for i in range(len(self.points)) :
            if self.points[i][4] == 'h':
                check_intersect(self.points[i], self.V)
            elif self.points[i][4] == 'v':
                check_intersect(self.points[i], self.H)
        
    def split(self):
        # chops segments by its intersection points, updates points
        self.split_mode = True
        temp_list = []
        for i in range(len(self.points)):
            temp_list += split(self.points[i], self.H, self.V)
        self.points = temp_list
        self.__class_of_equivalence()
        self.points = self.H + self.V
        self.__intersections()
        self.points = cce_label(self.points)
        self.split_mode = False
                                 
    def draw(self,canvas):
        # draws segments by their color, default color is white
        for i in range(len(self.points)):
            if len(self.points[i]) == 2:
                canvas.draw_line(self.points[i][0], self.points[i][1], 2.5, self.color)
            else:
                canvas.draw_line(self.points[i][0], self.points[i][1], 2.5, self.points[i][3])
        
    def paint(self, seg, color):
        # paints a segment of the Map
        if orientation(seg[0], seg[1]) == 'h':
            segment = sorting(seg, 0)
        elif orientation(seg[0], seg[1]) == 'v':
            segment = sorting(seg, 1)
        for i in range(len(self.points)):
            if [self.points[i][0],self.points[i][1]]==segment:
                self.points[i][3]= color # color the guarding segment
                self.__guarded_segments(self.points[i], 'blue') # color the guarded segments
        
    def get_length(self, color):
        # calculates the lenght of all segments of a given color in Map
        total_length = 0
        for i in range(len(self.points)):
            if self.points[i][3] == color:
                total_length += self.points[i][8]  
        return total_length/20
        
    def add_segment(self, segment):
        # adds a segment to Map
        self.points.append(segment)
                
    def undo(self):
        # deletes the last segment added to Map
        if len(self.points) > 0:
            self.points.pop()
                    
    def update(self): 
        # updates Map, sorting lexicographically and merging CCE's
        self.__class_of_equivalence()
        self.points = self.H + self.V
        self.__intersections()
                       
    def get_map(self):
        # returns points
        return list(self.points)
    
    def __guarded_segments(self, segment, color_desired):
        # all segments guarded by segment are set to color_desired
        for idx in segment[2]:
            for seg in self.points:
                if seg[4]+str(seg[5]) == idx:
                    #print seg
                    cce = seg[9]
                    color_cce(self.points, cce, segment[3], color_desired)
            color_cce(self.points, segment[9], segment[3], color_desired)
        
#------------------------------------------------------------------------
# Graph class. Bernd Klein, http://www.python-course.eu/graphs_python.php
class Graph:
    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.graph = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graph.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        (vertex1, vertex2, weigth) = tuple(edge)
        if vertex1 in self.graph:
            self.graph[vertex1].append((vertex2, weigth))
        else:
            self.graph[vertex1] = [(vertex2, weigth)]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if (neighbour[0], vertex) not in edges:
                    edges.append((vertex, neighbour[0], neighbour[1]))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graph:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
#--------------------------------------------------------------------------------------
# Union-Find. Carl Kingsford, http://www.cs.cmu.edu/~ckingsf/class/02713-s13/src/mst.py
class ArrayUnionFind:
    """Holds the three "arrays" for union find"""
    def __init__(self, S):
        self.group = dict((s,s) for s in S) # group[s] = id of its set
        self.size = dict((s,1) for s in S) # size[s] = size of set s
        self.items = dict((s,[s]) for s in S) # item[s] = list of items in set s
        
def make_union_find(S):
    """Create a union-find data structure"""
    return ArrayUnionFind(S)
    
def find(UF, s):
    """Return the id for the group containing s"""
    return UF.group[s]

def union(UF, a,b):
    """Union the two sets a and b"""
    assert a in UF.items and b in UF.items
    # make a be the smaller set
    if UF.size[a] > UF.size[b]:
        a,b = b,a
    # put the items in a into the larger set b
    for s in UF.items[a]:
        UF.group[s] = b
        UF.items[b].append(s)
    # the new size of b is increased by the size of a
    UF.size[b] += UF.size[a]
    # remove the set a (to save memory)
    del UF.size[a]
    del UF.items[a]
#---------------------------------------------------------------------------------------
# Kruskal MST. Carl Kingsford, http://www.cs.cmu.edu/~ckingsf/class/02713-s13/src/mst.py
def kruskal_mst(G):
    """Return a minimum spanning tree using kruskal's algorithm"""
    # sort the list of edges in G by their length
    # A small adaptation was done by Caleb for the sorting
    Edges = sorting(G.edges(),2)
    UF = make_union_find(G.vertices())  # union-find data structure

    # for edges in increasing weight
    mst = [] # list of edges in the mst
    for u,v,d in Edges:
        setu = find(UF, u)
        setv = find(UF, v)
        # if u,v are in different components
        if setu != setv:
            mst.append((u,v))
            union(UF, setu, setv)
    return mst
#------------------------------------------------------------------------    
# DEFINE EVENT HANDLERS
def click(pos):
    # defines a segment with a pair of points
    global temp, opt_length
    pos = (int(20*round(float(pos[0])/20)), int(20*round(float(pos[1])/20)))
    temp.append(pos)
    if len(temp) == 2:
        if not route_mode and orientation(temp[0],temp[1])!='neither':
            current_map.add_segment(temp)
        elif route_mode and orientation(temp[0],temp[1])!='neither':
            current_map.paint(temp, 'lime')
        temp = []
    if route_mode:
        objective_value()
            
def draw(canvas):
    global wolfie_pos, wolfie_vel, wolfie_size, start_next, counter 
    global unguarded_length, second_loop
    global score, opt_length
    """ draws the background, by uploading image file from web"""
    canvas.draw_image(image, (600, 400), (1200, 800), (600, 400), (1200, 800))
    
     # draws maps
    current_map.draw(canvas)
    
    # draws text
    canvas.draw_text('OPT length: '+str(opt_length), (180,16), 18, 'white')
    canvas.draw_text('Total length: '+str(total_length), (320,16), 18, 'white')
    canvas.draw_text('Your score: '+str(score), (480,16), 18, 'yellow')
    if route_mode:        
        canvas.draw_text('Game Mode: ON', (20,16), 18, 'yellow')
    else:
        canvas.draw_text('Game Mode: OFF', (20,16), 18, 'white')
    
    if second_loop:
        canvas.draw_text('is OPT connected?', (600,16), 18, 'yellow')
    
    # draws wolfie_bot
    canvas.draw_image(wolfie, (100, 105), (200, 210), (wolfie_pos[0], wolfie_pos[1]), wolfie_size)
    # update wolfie_bot position
    wolfie_pos[0] += wolfie_vel[0]
    wolfie_pos[1] += wolfie_vel[1]
    counter+=1
    if counter%90 == 0:
        counter=0
        
        if start:            
            guarding_route()
            wolfie_size = (32,32)
        else:
            wolfie_vel = [0,0]
            if unguarded_length == 0 and route_mode:
                if score > opt_length and counter%180==0:
                    wolfie_thanks.play()
                    
def undo():
    # undoes the last segment added to the current Map
    if not route_mode and not start:
        current_map.undo()        
            
def reset():
    # resets everything to start over
    global temp, current_map, current_route, route_mode, wolfie_pos, score, wolfie_vel
    global wolfie_size, start, second_loop, opt_length, total_length, first_loop
    route_mode = False    
    first_loop = True
    second_loop = False
    wolfie_pos = [780,20]
    wolfie_size = (32,32)
    wolfie_vel = [0,0]
    start = False
    opt_length = 0 
    total_length = 0
    score = 0
    temp = []
                    
def objective_value():
    # updates the objective value
    global opt_length, total_length, start, score, unguarded_length
    opt_length = current_map.get_length('lime')
    guarded_length = current_map.get_length('blue')
    unguarded_length = current_map.get_length('white')
    total_length = opt_length + guarded_length + unguarded_length
    
    if route_mode and not start:
        score = opt_length
    if unguarded_length == 0:
        if route_mode and start:
            if score > opt_length:
                wolfie_can.play()
            else:
                wolfie_cannot.play()
        start = False
        
def guarding_route():
    # performs Frank's heuristic
    global route_mode, temp, cce_dict, seg_dict, min_seg, neighbor_bag
    global first_loop, start, second_loop
    game_flag = False
    if first_loop:
        if not second_loop:
            if route_mode:
                game_flag = True
            update_map()
            if game_flag:
                route_mode = True
        temp = current_map.get_map()				
        cce_dict = cce_graph(temp) 					
        seg_dict = make_dictionary(temp) 			
        temp = sorting(temp,10) 					
        for i in range(len(temp)):
            if next_route_seg(temp[i], seg_dict):
                min_seg = temp[i][4]+str(temp[i][5]) 	
                break
        neighbor_bag = []
        first_loop = False
        start = True
    segment = [seg_dict[min_seg][0],seg_dict[min_seg][1]]
    current_map.paint(segment,'lime')
    wolfie_bot(segment)
    for x in seg_dict[min_seg][2]:
        if next_route_seg(seg_dict[x], seg_dict):
            neighbor_bag.append(seg_dict[x])
    neighbor_bag = sorting(neighbor_bag,10)
    flag = True
    while len(neighbor_bag) > 0 and flag:
        if next_route_seg(neighbor_bag[0], seg_dict):
            min_seg = neighbor_bag[0][4] + str(neighbor_bag[0][5])
            flag = False
        else:
            neighbor_bag.pop(0)
    if len(neighbor_bag) == 0:
        first_loop = True
        second_loop = True
        
    objective_value()
    
def game_mode():
    global route_mode, start
    current_map.update()
    current_map.split()
    if route_mode:
        reset()
        update_map()
    else:
        reset()
        route_mode = True
        start = False
    
def random_map():
    global current_map, start
    # generates a random map with at most n equivalence clases
    reset()
    seg = [(int(xmax/2),int(ymax/2)),(int(xmax/2),int(ymax/2))]
    random_map = set_random_seg(seg, n)
    current_map = Map(random_map)
    update_map()
    objective_value()
        
def update_map():
    global route_mode, current_route, first_loop, second_loop, start
    route_mode = False
    current_map.update()
    current_map.split()
    first_loop = True
    second_loop = False
    start = False
        
def random_seed(seed):
    global n
    n = int(seed)
    
def print_map():
    global start
    print "\nCurrent map: "
    printlist(current_map.get_map())
    start = False
    
def meet_wolfie():
    # short introduction of wolfie bot.
    global wolfie_pos, wolfie_size, wolfie_vel, start
    wolfie_pos = [xmax/2,ymax/2]
    wolfie_size = (200,210)
    wolfie_vel
    wolfie_hi.play()
    start = False
    
def clean():
    # cleans everything
    global current_map
    current_map = Map([])
    reset()
    
            
#------------------------------------------------------------------------    
# CREATE FRAME, BACKGROUND IMAGE & SOUNDS
frame = simplegui.create_frame("Frank's problem heuristic", xmax, ymax)
image = simplegui.load_image('http://s2.postimg.org/toznr3wh5/fondo.jpg')
wolfie_hi = simplegui.load_sound("http://s1.vocaroo.com/media/download_temp/Vocaroo_s1Pb9iEqzqGH.mp3")
wolfie_thanks = simplegui.load_sound("http://s0.vocaroo.com/media/download_temp/Vocaroo_s0CuRdPY9h6D.mp3")
wolfie_can = simplegui.load_sound("http://s1.vocaroo.com/media/download_temp/Vocaroo_s1XHNIL6FpAq.mp3")
wolfie_cannot = simplegui.load_sound("http://s1.vocaroo.com/media/download_temp/Vocaroo_s1Y8aW5hXntA.mp3")
wolfie = simplegui.load_image('http://s7.postimg.org/gl1jh6ofv/wolfie_bot.png')
wolfie_hi.set_volume(0.5)
wolfie_thanks.set_volume(0.5)
wolfie_can.set_volume(0.5)
wolfie_cannot.set_volume(0.5)

#----------------------------------------------------------------------------------------------
# REGISTER EVENT HANDLERS
#timer = simplegui.create_timer(1000, tick)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_input("Random segments? (n):", random_seed, 100)
frame.add_button("GENERATE Random Map", random_map, 130)
frame.add_button("My DRAWING is complete!", update_map, 130)
frame.add_button("GAME MODE (on/off)", game_mode, 130)
frame.add_button("CHALLENGE Wolfie-bot!", guarding_route, 130)
frame.add_button("UNDO", undo, 130)
frame.add_button("RESET", clean, 130)
frame.add_button("PRINT MAP", print_map, 130)
frame.add_button("Meet Wolfie-bot!", meet_wolfie, 130)

#----------------------------------------------------------------------------------------------
# START FRAME

frame.start()
current_map = Map([])




