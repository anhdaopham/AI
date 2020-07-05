# Pham Thi Anh Dao
# MSSV: 1611039
from collections import defaultdict
import math

def readFile():
    with open('input.txt', 'r') as fl:
        l = [[int(num) for num in lines.split(' ')] for lines in fl]
    n, x_start, y_start, x_end, y_end = (int(i) for i in l[0])
    fl.close()
    l.pop(0)
    return l

def readFile2():
    with open('input.txt', 'r') as fl:
        l = [[int(num) for num in lines.split(' ')] for lines in fl]
    n, x_start, y_start, x_end, y_end = (int(i) for i in l[0])
    fl.close()
    l.pop(0)
    return n, x_start, y_start, x_end, y_end

class Point:
    def __init__(self, x = 0, y = 0):
        self.abscissa = x  #hoanh do
        self.ordinate = y  #tung do

    def distancePointToPoint(self, other): # Khoang cach tu mot diem den mot diem khac
        distance = (self.abscissa - other.abscissa)**2 + (self.ordinate - other.ordinate)**2
        distance = math.sqrt(distance)
        return distance

    def duplicate(self, other): #kiem tra hai diem co trung nhau hay khong
        if(self.abscissa == other.abscissa and self.ordinate == other.ordinate):
            return True
        return False


    def __str__(self):
        s = "{0} {1}".format(self.abscissa, self.ordinate)
        return s


def lineFromPoints(A,B):
    a = B.ordinate - A.ordinate #hoanh do
    b = A.abscissa - B.abscissa #tung do
    c = a*(A.abscissa) + b*(A.ordinate)
    return a,b,c

def setOfVertex(V): #tap hop tat ca cac toa do cua cac da giac trong khong gian V
    set_of_vertex = []
    for i in range(len(V)):
        n_i = V[i][0]
        V[i].pop(0)
        temp = []
        for j in range(n_i):
            point_j = Point(V[i][j*2], V[i][j*2+1])
            temp.append(point_j)
        set_of_vertex.append(temp)
    return set_of_vertex

def remove_duplicate(arr): #loai bo cac diem bi trung trong ket qua tra ve
    final_list = []
    for num in arr:
        if num not in final_list:
            final_list.append(num)
    return final_list

def check(P,arr): #kiem tra mot diem co nam trong mot tap hop diem hay khong
    flag = False
    for i in range(len(arr)):
        if(P.duplicate(arr[i]) == True):
            flag = True
            break
    return flag

def isValid(P,V):
    set_of_vertex = setOfVertex(V)
    temp = []
    black_list = []
    valid = []
    for i in range(len(set_of_vertex)):
        for j in range(len(set_of_vertex[i])):
            if(j < len(set_of_vertex[i]) - 1):
                A = set_of_vertex[i][j]
                B = set_of_vertex[i][j+1]
                d_1_a, d_1_b, d_1_c = lineFromPoints(P,A)
                d_2_a, d_2_b, d_2_c = lineFromPoints(P, B)
                d_3_a, d_3_b, d_3_c = lineFromPoints(A,B)
            else:
                A = set_of_vertex[i][-1]
                B = set_of_vertex[i][0]
                d_1_a, d_1_b, d_1_c = lineFromPoints(P, A)
                d_2_a, d_2_b, d_2_c = lineFromPoints(P, B)
                d_3_a, d_3_b, d_3_c = lineFromPoints(A, B)
            for k in range(len(set_of_vertex)):
                for t in range(len(set_of_vertex[k])):
                    Q = set_of_vertex[k][t]
                    if((Q.duplicate(A) == False) and (Q.duplicate(B) == False)): # Q khac A va B
                        ans1 = (d_1_a * Q.abscissa + d_1_b * Q.ordinate - d_1_c) * (d_1_a * B.abscissa + d_1_b * B.ordinate - d_1_c) >= 0
                        ans2 = (d_2_a * Q.abscissa + d_2_b * Q.ordinate - d_2_c) * (d_2_a * A.abscissa + d_2_b * A.ordinate - d_2_c) >= 0
                        ans3 = (d_3_a * Q.abscissa + d_3_b * Q.ordinate - d_3_c) * (d_3_a * P.abscissa + d_3_b * P.ordinate - d_3_c) < 0
                        ans0 = not (ans1 and ans2 and ans3)
                        if(ans0 == True):
                            temp.append(Q)
                        else:
                            black_list.append(Q)
    black_list.append(P)

    for u in range(len(temp)):
        res = check(temp[u], black_list)
        if(res == False):
            valid.append(temp[u])
    valid = remove_duplicate(valid)
    return valid

def inPolygon(P):
    l_1 = readFile()
    set_of_vertex = setOfVertex(l_1)
    for i in range(len(set_of_vertex)):
        if(check(P,set_of_vertex[i]) == True):
            return i

n, x_start, y_start, x_end, y_end = readFile2()
S = Point(x_start,y_start)
G = Point(x_end, y_end)

l_0 = readFile()
temp = isValid(G,l_0)
cost = 0
arr = []
arr.append(S)
while((S.duplicate(G) == False) and (check(S,temp) == False)):
    l = readFile()
    res = isValid(S,l)
    min_fn = 10000

    for i in range(len(res)):
        g_n = S.distancePointToPoint(res[i])
        h_n = res[i].distancePointToPoint(G)
        f_n = g_n + h_n
        if (f_n < min_fn):
            min_fn = f_n
            S = res[i]
    arr.append(S)
arr.append(G)

for i in range(len(arr) - 1):
    cost = cost + arr[i].distancePointToPoint(arr[i+1])

print("Duong di tu S qua G: ")
for j in range(len(arr)):
    if(arr[j].duplicate(Point(1,3)) == True):
        print("((", end='')
        print(arr[j], end='')
        print(");S)")
    elif(arr[j].duplicate(Point(34,19)) == True):
        print("((", end='')
        print(arr[j], end='')
        print(");G)")
    else:
        print("((", end='')
        print(arr[j], end='')
        print(");", end='')
        print(inPolygon(arr[j]), end='')
        print(")")
print("Chi phi: %f" % (cost))


















