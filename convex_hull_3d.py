import rhinoscriptsyntax as rs
import random as r

def combination(list):
    comb=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            for k in range(j+1,len(list)):
                element=[list[i],list[j],list[k]]
                comb.append(element)
    return comb

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

def test_plan_equation(pt1,pt2,pt3,test_pt):
    vetA = (pt2[0]-pt1[0],pt2[1]-pt1[1],pt2[2]-pt1[2])
    vetB = (pt2[0]-pt3[0],pt2[1]-pt3[1],pt2[2]-pt3[2])
    N_vet = (vetA[1]*vetB[2]-vetA[2]*vetB[1],vetA[2]*vetB[0]-vetA[0]*vetB[2],vetA[0]*vetB[1]-vetA[1]*vetB[0])
    val = N_vet[0] *(test_pt[0] - pt2[0]) + N_vet[1] *(test_pt[1] - pt2[1]) + N_vet[2] *(test_pt[2] - pt2[2])
    return val


generate_num = 50

mk_pt=[]
for i in range(generate_num):
    pt_test = (r.randint(0,100),r.randint(0,100),r.randint(0,100))
    mk_pt.append(pt_test)

comb_pts =combination(mk_pt)

exter_srf=[]
for comb_pt in comb_pts:
    test_dummy=[]
    for test_pt in mk_pt:
        test_val = test_plan_equation(comb_pt[0],comb_pt[1],comb_pt[2],test_pt)
        if test_val > 0 and abs(test_val)>0.001:
            test_dummy.append(1)
        elif test_val<0 and abs(test_val)>0.001:
            test_dummy.append(-1)
    if list_inner_test(test_dummy) ==True:
        exter_srf.append(comb_pt)

