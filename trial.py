# creating card deck
l = ["2h", "2d", "2c", "2s",
     "3h", "3d", "3c", "3s",
     "4h", "4d", "4c", "4s",
     "5h", "5d", "5c", "5s",
     "6h", "6d", "6c", "6s",
     "7h", "7d", "7c", "7s",
     "8h", "8d", "8c", "8s",
     "9h", "9d", "9c", "9s",
     "10h", "10d", "10c", "10s",
     "Jh", "Jd", "Jc", "Js",
     "Qh", "Qd", "Qc", "Qs",
     "Kh", "Kd", "Kc", "Ks",
     "Ah", "Ad", "Ac", "As"]

# creating yours hand
from random import random
h1 = []
m1 = 0
m2 = 51
n = int(random() * (m2-m1+1)) + m1
print ("yours hand:")
h1.append(l[n])
l.pop(n)
m2 = 50
n = int(random() * (m2-m1+1)) + m1
h1.append(l[n])
l.pop(n)
print(h1)

# creating opponent's hand 
h2 = []
m2 = 49
n = int(random() * (m2-m1+1)) + m1
print("")
print("opponent's hand:")

h2.append(l[n])
l.pop(n)
m2 = 48
n = int(random() * (m2-m1+1)) + m1
h2.append(l[n])
l.pop(n)
print(h2)

# creating flop
print ("")
m2 = 47
n = int(random() * (m2-m1+1)) + m1
t = [] #creating table list
t.append(l[n]) #table list
l.pop(n)
m2 = 46
n = int(random() * (m2-m1+1)) + m1
t.append(l[n]) #table list
l.pop(n)
m2 = 45
n = int(random() * (m2-m1+1)) + m1
t.append(l[n]) #table list
l.pop(n)
print("flop:")
print(t)
print("")

# creating turn
m2 = 44
n = int(random() * (m2-m1+1)) + m1
t.append(l[n]) #table list
l.pop(n)
print("turn:")
print(t)
print("")

# creating river
m2 = 43
n = int(random() * (m2-m1+1)) + m1
t.append(l[n]) #table list
l.pop(n)
print("river:")
print(t)
print("")

# finaly output


# find combinations
# creating yours sequence
g1 = h1 + t
print("")

# creating opponent's sequence
g2 = h2 + t



# yours full combination (digits)
gasAA=[0,0,0,0,0,0,0]

for i in g1:    
        if i == "2h" or i == "2d" or i == "2c" or i == "2s":
            a2 = g1.index(i)
            gasAA.pop(a2)
            gasAA.insert(a2, 2)
            
for i in g1:    
        if i == "3h" or i == "3d" or i == "3c" or i == "3s":
            a3 = g1.index(i)
            gasAA.pop(a3)
            gasAA.insert(a3, 3)
            
for i in g1:    
        if i == "4h" or i == "4d" or i == "4c" or i == "4s":
            a4 = g1.index(i)
            gasAA.pop(a4)
            gasAA.insert(a4, 4)
            
for i in g1:    
        if i == "5h" or i == "5d" or i == "5c" or i == "5s":
            a5 = g1.index(i)
            gasAA.pop(a5)
            gasAA.insert(a5, 5)
                   
for i in g1:    
        if i == "6h" or i == "6d" or i == "6c" or i == "6s":
            a6 = g1.index(i)
            gasAA.pop(a6)
            gasAA.insert(a6, 6)
                     
for i in g1:    
        if i == "7h" or i == "7d" or i == "7c" or i == "7s":
            a7 = g1.index(i)
            gasAA.pop(a7)
            gasAA.insert(a7, 7)
          
for i in g1:    
        if i == "8h" or i == "8d" or i == "8c" or i == "8s":
            a8 = g1.index(i)
            gasAA.pop(a8)
            gasAA.insert(a8, 8)
            
for i in g1:    
        if i == "9h" or i == "9d" or i == "9c" or i == "9s":
            a9 = g1.index(i)
            gasAA.pop(a9)
            gasAA.insert(a9, 9)
            
for i in g1:    
        if i == "10h" or i == "10d" or i == "10c" or i == "10s":
            a10 = g1.index(i)
            gasAA.pop(a10)
            gasAA.insert(a10, 10)
            
for i in g1:    
        if i == "Jh" or i == "Jd" or i == "Jc" or i == "Js":
            a11 = g1.index(i)
            gasAA.pop(a11)
            gasAA.insert(a11, 11)
           
for i in g1:    
        if i == "Qh" or i == "Qd" or i == "Qc" or i == "Qs":
            a12 = g1.index(i)
            gasAA.pop(a12)
            gasAA.insert(a12, 12)
            
for i in g1:    
        if i == "Kh" or i == "Kd" or i == "Kc" or i == "Ks":
            a13 = g1.index(i)
            gasAA.pop(a13)
            gasAA.insert(a13, 13)
            
for i in g1:    
        if i == "Ah" or i == "Ad" or i == "Ac" or i == "As":
            a14 = g1.index(i)
            gasAA.pop(a14)
            gasAA.insert(a14, 14)






# yours full combination (suit)

gasSA=[0,0,0,0,0,0,0]

for r in g1:
        if r == "2h" or r == "3h" or r == "4h" or r == "5h" or r == "6h" or r == "7h" or r == "8h" or r == "9h" or r == "10h" or r == "Jh" or r == "Qh" or r == "Kh" or r == "Ah" :
                
                sh = g1.index(r)
                gasSA.pop(sh)
                gasSA.insert(sh, 1)
for r in g1:
        if r == "2d" or r == "3d" or r == "4d" or r == "5d" or r == "6d" or r == "7d" or r == "8d" or r == "9d" or r == "10d" or r == "Jd" or r == "Qd" or r == "Kd" or r == "Ad" :
                
                sd = g1.index(r)
                gasSA.pop(sd)
                gasSA.insert(sd, 2)
for r in g1:
        if r == "2c" or r == "3c" or r == "4c" or r == "5c" or r == "6c" or r == "7c" or r == "8c" or r == "9c" or r == "10c" or r == "Jc" or r == "Qc" or r == "Kc" or r == "Ac" :
                
                sc = g1.index(r)
                gasSA.pop(sc)
                gasSA.insert(sc, 3)
for r in g1:
        if r == "2s" or r == "3s" or r == "4s" or r == "5s" or r == "6s" or r == "7s" or r == "8s" or r == "9s" or r == "10s" or r == "Js" or r == "Qs" or r == "Ks" or r == "As" :
                
                ss = g1.index(r)
                gasSA.pop(ss)
                gasSA.insert(ss, 4)


#opponent's full combination (digits)      

gasBB=[0,0,0,0,0,0,0]

for j in g2:    
        if j == "2h" or j == "2d" or j == "2c" or j == "2s":
            b2 = g2.index(j)
            gasBB.pop(b2)
            gasBB.insert(b2, 2)
for j in g2:    
        if j == "3h" or j == "3d" or j == "3c" or j == "3s":
            b3 = g2.index(j)
            gasBB.pop(b3)
            gasBB.insert(b3, 3)
for j in g2:    
        if j == "4h" or j == "4d" or j == "4c" or j == "4s":
            b4 = g2.index(j)
            gasBB.pop(b4)
            gasBB.insert(b4, 4) 
for j in g2:    
        if j == "5h" or j == "5d" or j == "5c" or j == "5s":
            b5 = g2.index(j)
            gasBB.pop(b5)
            gasBB.insert(b5, 5) 
for j in g2:    
        if j == "6h" or j == "6d" or j == "6c" or j == "6s":
            b6 = g2.index(j)
            gasBB.pop(b6)
            gasBB.insert(b6, 6) 
for j in g2:    
        if j == "7h" or j == "7d" or j == "7c" or j == "7s":
            b7 = g2.index(j)
            gasBB.pop(b7)
            gasBB.insert(b7, 7) 
for j in g2:    
        if j == "8h" or j == "8d" or j == "8c" or j == "8s":
            b8 = g2.index(j)
            gasBB.pop(b8)
            gasBB.insert(b8, 8) 
for j in g2:    
        if j == "9h" or j == "9d" or j == "9c" or j == "9s":
            b9 = g2.index(j)
            gasBB.pop(b9)
            gasBB.insert(b9, 9)
for j in g2:    
        if j == "10h" or j == "10d" or j == "10c" or j == "10s":
            b10 = g2.index(j)
            gasBB.pop(b10)
            gasBB.insert(b10, 10) 
for j in g2:    
        if j == "Jh" or j == "Jd" or j == "Jc" or j == "Js":
            b11 = g2.index(j)
            gasBB.pop(b11)
            gasBB.insert(b11, 11) 
for j in g2:    
        if j == "Qh" or j == "Qd" or j == "Qc" or j == "Qs":
            b12 = g2.index(j)
            gasBB.pop(b12)
            gasBB.insert(b12, 12) 
for j in g2:    
        if j == "Kh" or j == "Kd" or j == "Kc" or j == "Ks":
            b13 = g2.index(j)
            gasBB.pop(b13)
            gasBB.insert(b13, 13) 
for j in g2:    
        if j == "Ah" or j == "Ad" or j == "Ac" or j == "As":
            b14 = g2.index(j)
            gasBB.pop(b14)
            gasBB.insert(b14, 14)

# opponent's full combination (suit)

gasSB=[0,0,0,0,0,0,0]

for t in g2:
        if t == "2h" or t == "3h" or t == "4h" or t == "5h" or t == "6h" or t == "7h" or t == "8h" or t == "9h" or t == "10h" or t == "Jh" or t == "Qh" or t == "Kh" or t == "Ah" :
                bh = g2.index(t)
                gasSB.pop(bh)
                gasSB.insert(bh, 1)
for t in g2:
        if t == "2d" or t == "3d" or t == "4d" or t == "5d" or t == "6d" or t == "7d" or t == "8d" or t == "9d" or t == "10d" or t == "Jd" or t == "Qd" or t == "Kd" or t == "Ad" :
                bd = g2.index(t)
                gasSB.pop(bd)
                gasSB.insert(bd, 2)
for t in g2:
        if t == "2c" or t == "3c" or t == "4c" or t == "5c" or t == "6c" or t == "7c" or t == "8c" or t == "9c" or t == "10c" or t == "Jc" or t == "Qc" or t == "Kc" or t == "Ac" :
                bc = g2.index(t)
                gasSB.pop(bc)
                gasSB.insert(bc, 3)
for t in g2:
        if t == "2s" or t == "3s" or t == "4s" or t == "5s" or t == "6s" or t == "7s" or t == "8s" or t == "9s" or t == "10s" or t == "Js" or t == "Qs" or t == "Ks" or t == "As" :
                bs = g2.index(t)
                gasSB.pop(bs)
                gasSB.insert(bs, 4)
print("hand1 full combination: ")           
print(g1)
print(gasAA)
print(gasSA)
print("")
print("hand2 full combination: ")  
print(g2)
print(gasBB)
print(gasSB)
print("")

# finding royal flush HAND1
RF1 = 0
i9 = ["5d", "4h", "10h", "Jh", "Qh", "Kh", "As"]

HRF = ["10h", "Jh", "Qh", "Kh", "Ah"]
DRF = ["10d", "Jd", "Qd", "Kd", "Ad"]
CRF = ["10c", "Jc", "Qc", "Kc", "Ac"]
SRF = ["10s", "Js", "Qs", "Ks", "As"]
r1H = len(list(set(g1) & set(HRF)))
if r1H >= 5:
    RF1 = 1
r1D = len(list(set(g1) & set(DRF)))
if r1D >= 5:
    RF1 = 1
r1C = len(list(set(g1) & set(CRF)))
if r1C >= 5:
    RF1 = 1
r1S = len(list(set(g1) & set(SRF)))
if r1S >= 5:
    RF1 = 1

# finding royal flush HAND2
RF2 = 0
i9 = ["5d", "4h", "10h", "Jh", "Qh", "Kh", "As"]
r2H = len(list(set(g2) & set(HRF)))
if r1H >= 5:
    RF2 = 1
r2D = len(list(set(g2) & set(DRF)))
if r2D >= 5:
    RF2 = 1
r2C = len(list(set(g2) & set(CRF)))
if r2C >= 5:
    RF2 = 1
r2S = len(list(set(g2) & set(SRF)))
if r2S >= 5:
    RF2 = 1
