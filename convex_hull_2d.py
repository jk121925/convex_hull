import rhinoscriptsyntax as rs
import random as r

def combination(list):
    comb=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            element=[list[i],list[j]]
            comb.append(element)
    return(comb)

def mk_ln(comb_list):
    lns=[]
    for i in range(len(comb_list)):
        ln =rs.AddLine(comb_list[i][0],comb_list[i][1])
        lns.append(ln)
    return(lns)

def list_inner_test(arr):
    test = list(set(arr))
    if len(test) ==1:
        val = True
    else :
        val = False
    return val

def test_line_equation(pt1,pt2,test_pt):
    if (pt1[0]-pt2[0]) == 0 :
        val = test_pt[0]-pt1[0]
    elif (pt1[0]-pt2[0]) != 0 :
        m = (pt1[1]-pt2[1])/(pt1[0]-pt2[0])
        val = -m*(test_pt[0]-pt1[0])+(test_pt[1]-pt1[1])
    return val


generate_num = 100

mk_pt=[]
for i in range(generate_num):
    pt_test = (r.randint(0,100),r.randint(0,100),0)
    mk_pt.append(pt_test)

comb_pts  =combination(mk_pt)

convex_hull_2d=[]
for comb_pt in comb_pts:
    test_dummy=[]
    for test_pt in mk_pt:
        test_val = test_line_equation(comb_pt[0],comb_pt[1],test_pt)
        if  test_val > 0 and abs(test_val) >0.0000001 :
            test_dummy.append(1)
        elif test_val <0 and abs(test_val) >0.0000001:
            test_dummy.append(-1)
        #print(test_dummy)
    if  list_inner_test(test_dummy) ==True :
        convex_hull_2d.append(comb_pt)
