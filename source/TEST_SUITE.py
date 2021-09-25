""" This module implements helper functions to use in Frank's
problem heuristic. Each function has a test suite """

# import the Test suite
import Franks_test_suite as poc

def sorting(List, n):
    """ sorts a list of tuples, according to the nth entry """
    idx_list = [[List[i][n],i] for i in range (len(List))]
    idx_list.sort()
    sorted_list = [List[idx_list[i][1]] for i in range (len(idx_list))]
    return sorted_list

def orientation(p1 ,p2):
    """ determines if [p1,p2] is horizontal or vertical """
    if p1[0] == p2[0] and p1[1] != p2[1] :
        seg_type = 'v'
    elif p1[1] == p2[1] and p1[0] != p2[0]:
        seg_type = 'h'
    else:
        seg_type = 'neither' 
    return seg_type

def equivalence(List,n):
    """ groups elements of a list by their nth entry. Assume pre-processed
    data, that is, List sorted by nth entry """
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

def classify(segments):
    """ creates horizontal and vertical line segments dictionaries,
    segment: (p1, p2, equiv. class, min_value, color, length, [neighbors]) """
    hor = {}
    ver = {}
    i = j = 0
    for k in range(len(segments)):
        seg_type = orientation(segments[k][0], segments[k][1])
        if seg_type == 'h':
            [p1, p2] = sorting(segments[k], 0)
            hor['h' + str(j)] = [p1, p2, p1[1], p1[0], p2[0]-p1[0], 'white', []]
            j += 1
        elif seg_type == 'v':
            [p1, p2] = sorting(segments[k], 1)
            ver['v' + str(i)] = [p1, p2, p1[0], p1[1], p2[1]-p1[1], 'white', []]
            i += 1
    print [hor, ver]
    return [hor, ver]

def overlap(ab, cd):
    """ evaluates if two intervals intersect """
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

def merge(seg1, seg2):
    """ merges two collinear overlapping segments """
    if orientation(seg1[0], seg1[1]) == 'h':
        var = 0
    elif orientation(seg1[0], seg1[1]) == 'v':
        var =  1
    temp = sorting([seg1[0], seg1[1], seg2[0], seg2[1]],var)
    return [temp[0], temp[-1]]

def intersect(seg1, seg2):
    """ checks if two segments intersect, assume well ordered coordinates """
    check_x = overlap((seg1[0][0], seg1[1][0]), (seg2[0][0], seg2[1][0]))
    check_y = overlap((seg1[0][1], seg1[1][1]), (seg2[0][1], seg2[1][1]))
    return check_x and check_y

def list_merge(List):
    """ merges overlapping collinear segments in a list. 
    Assumes collinearity and list sorted by min_val """ 
    seg_merge = List[0]
    flag=0
    temp=[]
    for i in range (1,len(List)):
        if intersect(List[i], seg_merge):
            seg_merge = merge(seg_merge, List[i])
        else:
            temp.append(seg_merge)
            seg_merge = List[i]
    temp.append(seg_merge)
    List = temp
    #print List
    return List

def check_intersect(seg, dictionary):
    """ checks intersections between a segment and a dictionary of segments """
    seg[6] = []
    for idx in dictionary.keys():
            if intersect(seg, dictionary[idx]):
                seg[6].append(idx)
    return seg

# Run tests
print "\nTesting: sorting"
poc.sorting_run_suite(sorting)

print "\nTesting: orientation"
poc.orientation_run_suite(orientation)

print "\nTesting: equivalence"
poc.equivalence_run_suite(equivalence)

print "\nTesting: classify"
poc.classify_run_suite(classify)

print "\nTesting: overlap"
poc.overlap_run_suite(overlap)

print "\nTesting: merge"
poc.merge_run_suite(merge)

print "\nTesting: intersect"
poc.intersect_run_suite(intersect)

print "\nTesting: list_merge"
poc.list_merge_run_suite(list_merge)

print "\nTesting: check_intersect"
poc.check_intersect_run_suite(check_intersect)



