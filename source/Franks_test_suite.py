""" 
Test suite for Frank's problem helper functions 
"""

# the following module is a class, TestSuite
import TestSuite as poc_simpletest

def sorting_run_suite(sorting):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test sorting on various inputs
    inp = [(5, 1, 3, 4, 5), (4, 3, 1, 2, 2), (3, 4, 5, 3, 1), (1, 2, 2, 5, 3), (2, 5, 4, 1, 4)]
    out1 = [(1, 2, 2, 5, 3), (2, 5, 4, 1, 4), (3, 4, 5, 3, 1), (4, 3, 1, 2, 2), (5, 1, 3, 4, 5)]
    out2 = [(5, 1, 3, 4, 5), (1, 2, 2, 5, 3), (4, 3, 1, 2, 2), (3, 4, 5, 3, 1), (2, 5, 4, 1, 4)] 
    out3 = [(4, 3, 1, 2, 2), (1, 2, 2, 5, 3), (5, 1, 3, 4, 5), (2, 5, 4, 1, 4), (3, 4, 5, 3, 1)]
    out4 = [(2, 5, 4, 1, 4), (4, 3, 1, 2, 2), (3, 4, 5, 3, 1), (5, 1, 3, 4, 5), (1, 2, 2, 5, 3)] 
    out5 = [(3, 4, 5, 3, 1), (4, 3, 1, 2, 2), (1, 2, 2, 5, 3), (2, 5, 4, 1, 4), (5, 1, 3, 4, 5)]
    
    suite.run_test(sorting(list(inp), 0), out1, "Test #1:")
    suite.run_test(sorting(list(inp), 1), out2, "Test #2:")
    suite.run_test(sorting(list(inp), 2), out3, "Test #3:")
    suite.run_test(sorting(list(inp), 3), out4, "Test #4:")
    suite.run_test(sorting(list(inp), 4), out5, "Test #5:")
    
    suite.report_results()
    
def orientation_run_suite(orientation):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test orientation on various inputs
    suite.run_test(orientation((2, 3), (7, 6)), 'neither', "Test #1:")
    suite.run_test(orientation((2, 5), (2, -4)), 'v', "Test #2:")
    suite.run_test(orientation((0, -1), (1, 1)), 'neither', "Test #3:")
    suite.run_test(orientation((9, 9), (9, 9)), 'neither', "Test #4:")
    suite.run_test(orientation((3, 5), (-2, 5)), 'h', "Test #5:")
    suite.run_test(orientation((-2, -4), (-2, 6)), 'v', "Test #6:")
    suite.run_test(orientation((9, -6), (4, -6)), 'h', "Test #7:")
    suite.run_test(orientation((2, 3), (5, 7)), 'neither', "Test #8:")
    suite.run_test(orientation((3, 0), (-18, 0)), 'h', "Test #9:")
    suite.run_test(orientation((0, 2), (0, 5)), 'v', "Test #10:")
    
    suite.report_results()
    
def equivalence_run_suite(equivalence):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test equivalence on various inputs
    inp = [(2, 'x', 0.3, 1), (2, 'x', 0.3, 1), (3, 'x', 0.3, 1), (3, 'x', -0.2, 1), (4, 'x', -0.2, 1), 
           (4, 'y', -0.2, 1), (4, 'y', 0.1, 1), (5, 'y', 0.1, 1), (5, 'y', 0.1, 1)]
    out1 = {0:[(2, 'x', 0.3, 1), (2, 'x', 0.3, 1)],
            1:[(3, 'x', 0.3, 1), (3, 'x', -0.2, 1)],
            2:[(4, 'x', -0.2, 1), (4, 'y', -0.2, 1), (4, 'y', 0.1, 1)], 
            3:[(5, 'y', 0.1, 1), (5, 'y', 0.1, 1)]}
    out2 = {0:[(2, 'x', 0.3, 1), (2, 'x', 0.3, 1), (3, 'x', 0.3, 1), (3, 'x', -0.2, 1), (4, 'x', -0.2, 1)], 
            1:[(4, 'y', -0.2, 1), (4, 'y', 0.1, 1), (5, 'y', 0.1, 1), (5, 'y', 0.1, 1)]}
    out3 = {0:[(2, 'x', 0.3, 1), (2, 'x', 0.3, 1), (3, 'x', 0.3, 1)], 
            1:[(3, 'x', -0.2, 1), (4, 'x', -0.2, 1), (4, 'y', -0.2, 1)], 
            2:[(4, 'y', 0.1, 1), (5, 'y', 0.1, 1), (5, 'y', 0.1, 1)]}
    out4 = {0:[(2, 'x', 0.3, 1), (2, 'x', 0.3, 1), (3, 'x', 0.3, 1), (3, 'x', -0.2, 1), (4, 'x', -0.2, 1), 
           (4, 'y', -0.2, 1), (4, 'y', 0.1, 1), (5, 'y', 0.1, 1), (5, 'y', 0.1, 1)]}
    inp5 = [('x', 1), (2.3, 1), ('yx', 1), (4/3, 1), (-5, 1), (0.2, 1)]
    out5 = {0:[('x', 1)], 1:[(2.3, 1)], 2:[('yx', 1)], 3:[(4/3, 1)], 4:[(-5, 1)], 5:[(0.2, 1)]}
    
    suite.run_test(equivalence(inp, 0), out1, "Test #1:")
    suite.run_test(equivalence(inp, 1), out2, "Test #2:")
    suite.run_test(equivalence(inp, 2), out3, "Test #3:")
    suite.run_test(equivalence(inp, 3), out4, "Test #4:")
    suite.run_test(equivalence(inp5, 0), out5, "Test #5:")
    
    suite.report_results()
    
def classify_run_suite(classify):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test classify on various inputs
    inp = [[(80, 20), (20, 20)], [(60, 40), (20, 40)], [(20, 60), (40, 60)],
           [(20, 80), (20, 20)], [(40, 60), (40, 20)], [(60, 40), (60, 20)], 
           [(0,0), (1,1)], [(-1, 2), (2, 3)], [(1, 1), (1, 1)]]
    out = [{'h0': [(20, 20), (80, 20), 20, 20, 60, 'white', []], 
            'h1': [(20, 40), (60, 40), 40, 20, 40, 'white', []], 
            'h2': [(20, 60), (40, 60), 60, 20, 20, 'white', []]},
           {'v0': [(20, 20), (20, 80), 20, 20, 60, 'white', []],
            'v1': [(40, 20), (40, 60), 40, 20, 40, 'white', []], 
            'v2': [(60, 20), (60, 40), 60, 20, 20, 'white', []]}]
    
    suite.run_test(classify(inp), out, "Test #1:")
    
    suite.report_results()
    
def overlap_run_suite(overlap):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test overlap on various inputs
    suite.run_test(overlap((0, 0), (1, 2)), False, "Test #1:")
    suite.run_test(overlap((-3, 5), (-7, 0)), True, "Test #2:")
    suite.run_test(overlap((2, 2), (2, 2)), True, "Test #3:")
    suite.run_test(overlap((-1, 2), (5, 7)), False, "Test #4:")
    suite.run_test(overlap((-5, -3), (-2, -1)), False, "Test #5:")
    suite.run_test(overlap((3.4, 5.2), (-1.7, 3.4)), True, "Test #6:")
    suite.run_test(overlap((6.7, 9.89), (9.9, 10)), False, "Test #7:")
    suite.run_test(overlap((-0.25, -0.15), (-0.15, -0.15)), True, "Test #8:")
    suite.run_test(overlap((0.3, 0.7), (-0.2, -0.1)), False, "Test #9:")
    suite.run_test(overlap((0.15, 0.56), (0.12, 0.155)), True, "Test #10:")
    
    suite.report_results()
    
def merge_run_suite(merge):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test merge on various inputs
    suite.run_test(merge([(60, 40), (120, 40), 40], [(100, 40), (140, 40), 40]),
                   [(60, 40),(140, 40)], "Test #1 :") 
    suite.run_test(merge([(40, 80), (80, 80), 80], [(40, 80), (80, 80), 80]),
                   [(40, 80), (80, 80)], "Test #2 :") 
    suite.run_test(merge([(60, 100), (100, 100), 100], [(100, 100), (140, 100), 100]),
                   [(60, 100), (140, 100)], "Test #3 :") 
    suite.run_test(merge([(60, 140), (120, 140), 140], [(100, 140), (160, 140), 140]),
                   [(60, 140), (160, 140)], "Test #4 :") 
    suite.run_test(merge([(120, 180), (100, 180), 180], [(120, 180), (140, 180), 180]),
                   [(100, 180), (140, 180)], "Test #5 :") 
    suite.run_test(merge([(60, 200), (60, 240), 60], [(60, 180), (60, 260), 60]),
                   [(60, 180), (60, 260)], "Test #6 :") 
    suite.run_test(merge([(60, 280), (60, 320), 60], [(60, 300), (60, 340), 60]),
                   [(60, 280), (60, 340)], "Test #7 :") 
    suite.run_test(merge([(100, 280), (100, 320), 100], [(100, 240), (100, 300), 100]),
                   [(100, 240), (100, 320)], "Test #8 :") 
    suite.run_test(merge([(140, 260), (140, 300), 140], [(140, 280), (140, 300), 140]), 
                   [(140, 260), (140, 300)], "Test #9 :") 
    suite.run_test(merge([(160, 220), (160, 260), 160], [(160, 220), (160, 260), 160]),
                   [(160, 220), (160, 260)], "Test #10 :") 
    suite.run_test(merge([(140, 80), (220, 80), 80], [(200, 80), (160, 80), 80]),
                   [(140, 80), (220, 80)], "Test #11 :") 
    suite.run_test(merge([(140, 320), (140, 420), 140], [(140, 340), (140, 440), 140]),
                   [(140, 320), (140, 440)], "Test #12 :") 
      
    suite.report_results()
    
def intersect_run_suite(intersect):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
   
    # test intersect on various inputs
    suite.run_test(intersect([(60, 40), (120, 40), 40], [(100, 40), (140, 40), 40]), True, "Test #1:")
    suite.run_test(intersect([(40, 80), (80, 80), 80], [(40, 80), (80, 80), 80]), True, "Test #2:")
    suite.run_test(intersect([(60, 100), (100, 100), 100], [(100, 100), (140, 100), 100]), True, "Test #3:")
    suite.run_test(intersect([(60, 140), (120, 140), 140], [(100, 140), (160, 140), 140]), True, "Test #4:")
    suite.run_test(intersect([(120, 180), (100, 180), 180], [(120, 180), (140, 180), 180]), True, "Test #5 :")
    suite.run_test(intersect([(60, 200), (60, 240), 60], [(60, 180), (60, 260), 60]), True, "Test #6:")
    suite.run_test(intersect([(60, 280), (60, 320), 60], [(60, 300), (60, 340), 60]), True, "Test #7:")
    suite.run_test(intersect([(100, 280), (100, 320), 100], [(100, 240), (100, 300), 100]), True, "Test #8:")
    suite.run_test(intersect([(140, 260), (140, 300), 140], [(140, 280), (140, 300), 140]), True, "Test #9:")
    suite.run_test(intersect([(160, 220), (160, 260), 160], [(160, 220), (160, 260), 160]), True, "Test #10 :")
    suite.run_test(intersect([(160, 60), (160, 120)], [(180, 100), (180, 160)]), False, "Test #11:")
    suite.run_test(intersect([(200, 60), (260, 60)], [(240, 40), (300, 40)]), False, "Test #12:")
    suite.run_test(intersect([(240, 100), (240, 140)], [(240, 160), (240, 200)]), False, "Test #13:")
    suite.run_test(intersect([(120, 60), (80, 60)], [(60, 60), (20, 60)]), False, "Test #14:")
    suite.run_test(intersect([(100, 100), (100, 160)], [(60, 180), (140, 180)]), False, "Test #15:")
    suite.run_test(intersect([(120, 220), (120, 260)], [(140, 260), (200, 260)]), False, "Test #16:")
    suite.run_test(intersect([(140, 140), (220, 140)], [(180, 140), (180, 220)]), True, "Test #17:")
    suite.run_test(intersect([(300, 120), (340, 120)], [(340, 120), (340, 80)]), True, "Test #18:")
    suite.run_test(intersect([(300, 160), (300, 220)], [(300, 200), (260, 200)]), True, "Test #19:")
    suite.run_test(intersect([(120, 300), (180, 300)], [(140, 240), (140, 360)]), True, "Test #20:")
    
    suite.report_results()
    
def list_merge_run_suite(list_merge):
    # create a TestSuite object
    suit = poc_simpletest.TestSuite()
    
    # test list_merge on various inputs
    inp1 = [[(100, 180), (120, 180)], [(120, 180), (140, 180)], [(140, 180), (160, 180)],
            [(160, 180), (180, 180)], [(180, 180), (200, 180)], [(200, 180), (220, 180)]]
    inp2 = [[(100, 240), (160, 240)], [(120, 240), (320, 240)], [(140, 240), (180, 240)],
            [(200, 240), (240, 240)], [(260, 240), (280, 240)], [(280, 240), (340, 240)]]
    inp3 = [[(100, 300), (140, 300)], [(120, 300), (160, 300)], [(180, 300), (220, 300)],
            [(220, 300), (240, 300)], [(260, 300), (320, 300)], [(280, 300), (300, 300)]]
    inp4 = [[(100, 340), (140, 340)], [(160, 340), (200, 340)], [(180, 340), (220, 340)],
            [(240, 340), (280, 340)], [(280, 340), (300, 340)], [(320, 340), (340, 340)]]
    inp5 = [[(420, 120), (420, 180)], [(420, 140), (420, 180)], [(420, 160), (420, 200)],
            [(420, 200), (420, 240)], [(420, 220), (420, 260)], [(420, 240), (420, 280)]]
    inp6 = [[(440, 120), (440, 160)], [(440, 160), (440, 180)], [(440, 180), (440, 200)],
            [(440, 200), (440, 240)], [(440, 220), (440, 260)], [(440, 260), (440, 280)]]
    inp7 = [[(480, 120), (480, 140)], [(480, 160), (480, 180)], [(480, 180), (480, 200)],
            [(480, 220), (480, 260)], [(480, 240), (480, 260)], [(480, 260), (480, 280)]]
    inp8 = [[(520, 120), (520, 160)], [(520, 200), (520, 260)], [(520, 220), (520, 280)],
            [(520, 300), (520, 340)], [(520, 340), (520, 360)], [(520, 360), (520, 380)]]
    
    out1 = [[(100, 180),(220, 180)]]
    out2 = [[(100, 240),(340, 240)]]
    out3 = [[(100, 300),(160, 300)], [(180, 300),(240, 300)], [(260, 300),(320, 300)]]
    out4 = [[(100, 340),(140, 340)], [(160, 340),(220, 340)], [(240, 340),(300, 340)], 
            [(320, 340),(340, 340)]]
    out5 = [[(420, 120),(420, 280)]]
    out6 = [[(440, 120),(440, 280)]]
    out7 = [[(480, 120),(480, 140)], [(480, 160),(480, 200)], [(480, 220),(480, 280)]]
    out8 = [[(520, 120),(520, 160)], [(520, 200),(520, 280)], [(520, 300),(520, 380)]]

    suit.run_test(list_merge(inp1), out1, "Test#1:")
    suit.run_test(list_merge(inp2), out2, "Test#2:")
    suit.run_test(list_merge(inp3), out3, "Test#3:")
    suit.run_test(list_merge(inp4), out4, "Test#4:")
    suit.run_test(list_merge(inp5), out5, "Test#5:")
    suit.run_test(list_merge(inp6), out6, "Test#6:")
    suit.run_test(list_merge(inp7), out7, "Test#7:")
    suit.run_test(list_merge(inp8), out8, "Test#8:")
    
    suit.report_results()
    
def check_intersect_run_suite(check_intersect):
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test check intersect with various inputs
    hor = {'h0': [(20, 20), (80, 20), 20, 20, 60, 'white', []], 
           'h1': [(20, 40), (60, 40), 40, 20, 40, 'white', []], 
           'h2': [(20, 60), (40, 60), 60, 20, 20, 'white', []]}
    ver = {'v0': [(20, 20), (20, 80), 20, 20, 60, 'white', []], 
           'v1': [(40, 20), (40, 60), 40, 20, 40, 'white', []], 
           'v2': [(60, 20), (60, 40), 60, 20, 20, 'white', []]}
    
    inp1 = [(0, 20), (60, 20), 20, 0, 60, 'white', []]
    inp2 = [(0, 40), (40, 40), 40, 0, 40, 'white', []]
    inp3 = [(0, 60), (20, 60), 60, 0, 20, 'white', []]
    inp4 = [(20, 0), (20, 60), 20, 0, 60, 'white', []]
    inp5 = [(40, 0), (40, 40), 40, 0, 40, 'white', []]
    inp6 = [(60, 0), (60, 20), 60, 0, 20, 'white', []] 
    
    out1 = [(0, 20), (60, 20), 20, 0, 60, 'white', ['h0']]
    out2 = [(0, 20), (60, 20), 20, 0, 60, 'white', ['v0', 'v1', 'v2']]
    out3 = [(0, 40), (40, 40), 40, 0, 40, 'white', ['h1']]
    out4 = [(0, 40), (40, 40), 40, 0, 40, 'white', ['v0', 'v1']]
    out5 = [(0, 60), (20, 60), 60, 0, 20, 'white', ['h2']]
    out6 = [(0, 60), (20, 60), 60, 0, 20, 'white', ['v0']]
    out7 = [(20, 0), (20, 60), 20, 0, 60, 'white', ['v0']]
    out8 = [(20, 0), (20, 60), 20, 0, 60, 'white', ['h0', 'h1', 'h2']]
    out9 = [(40, 0), (40, 40), 40, 0, 40, 'white', ['v1']]
    out10 = [(40, 0), (40, 40), 40, 0, 40, 'white', ['h0', 'h1']]
    out11 = [(60, 0), (60, 20), 60, 0, 20, 'white', ['v2']]
    out12 = [(60, 0), (60, 20), 60, 0, 20, 'white', ['h0']]
        
    suite.run_test(check_intersect(list(inp1), hor), out1, "Test #1:")
    suite.run_test(check_intersect(list(inp1), ver), out2, "Test #2:")
    suite.run_test(check_intersect(list(inp2), hor), out3, "Test #3:")
    suite.run_test(check_intersect(list(inp2), ver), out4, "Test #4:")
    suite.run_test(check_intersect(list(inp3), hor), out5, "Test #5:")
    suite.run_test(check_intersect(list(inp3), ver), out6, "Test #6:")
    suite.run_test(check_intersect(list(inp4), ver), out7, "Test #7:")
    suite.run_test(check_intersect(list(inp4), hor), out8, "Test #8:")
    suite.run_test(check_intersect(list(inp5), ver), out9, "Test #9:")
    suite.run_test(check_intersect(list(inp5), hor), out10, "Test #10:")
    suite.run_test(check_intersect(list(inp6), ver), out11, "Test #11:")
    suite.run_test(check_intersect(list(inp6), hor), out12, "Test #12:")
    
    suite.report_results()
    

    
    


   
    
    
    


    
    
    
    
                   
                   
                   
                   
    
