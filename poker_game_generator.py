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
print ("")
print ("opponent's hand:")
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
print("summary:")
print(h1)
print(h2)
print(t)
print("")

# find combinations
# creating yours sequence
g11 = []
g1 = h1 + t
print(g1)
print("")
# creating opponent's sequence
g22 = []
g2 = h2 + t
print(g2)
print("")

#finding
a = 0
for i in g1:    
        if i == "2h" or i == "2d" or i == "2c" or i == "2s":
            a = 2
            g11.append(2)
for i in g1:    
        if i == "3h" or i == "3d" or i == "3c" or i == "3s":
            a = 2
            g11.append(3)
for i in g1:    
        if i == "4h" or i == "4d" or i == "4c" or i == "4s":
            a = 2
            g11.append(4)
for i in g1:    
        if i == "5h" or i == "5d" or i == "5c" or i == "5s":
            a = 2
            g11.append(5)        
for i in g1:    
        if i == "6h" or i == "6d" or i == "6c" or i == "6s":
            a = 2
            g11.append(6)          
for i in g1:    
        if i == "7h" or i == "7d" or i == "7c" or i == "7s":
            a = 2
            g11.append(7)
for i in g1:    
        if i == "8h" or i == "8d" or i == "8c" or i == "8s":
            a = 2
            g11.append(8)
for i in g1:    
        if i == "9h" or i == "9d" or i == "9c" or i == "9s":
            a = 2
            g11.append(9)
for i in g1:    
        if i == "10h" or i == "10d" or i == "10c" or i == "10s":
            a = 2
            g11.append(10)
for i in g1:    
        if i == "Jh" or i == "Jd" or i == "Jc" or i == "Js":
            a = 2
            g11.append(11)
for i in g1:    
        if i == "Qh" or i == "Qd" or i == "Qc" or i == "Qs":
            a = 2
            g11.append(12)
for i in g1:    
        if i == "Kh" or i == "Kd" or i == "Kc" or i == "Ks":
            a = 2
            g11.append(13)
for i in g1:    
        if i == "Ah" or i == "Ad" or i == "Ac" or i == "As":
            a = 2
            g11.append(14)



            

for i in g2:    
        if i == "2h" or i == "2d" or i == "2c" or i == "2s":
            a = 2
            g22.append(2)
for i in g2:    
        if i == "3h" or i == "3d" or i == "3c" or i == "3s":
            a = 2
            g22.append(3)
for i in g2:    
        if i == "4h" or i == "4d" or i == "4c" or i == "4s":
            a = 2
            g22.append(4)
for i in g2:    
        if i == "5h" or i == "5d" or i == "5c" or i == "5s":
            a = 2
            g22.append(5)        
for i in g2:    
        if i == "6h" or i == "6d" or i == "6c" or i == "6s":
            a = 2
            g22.append(6)          
for i in g2:    
        if i == "7h" or i == "7d" or i == "7c" or i == "7s":
            a = 2
            g22.append(7)
for i in g2:    
        if i == "8h" or i == "8d" or i == "8c" or i == "8s":
            a = 2
            g22.append(8)
for i in g2:    
        if i == "9h" or i == "9d" or i == "9c" or i == "9s":
            a = 2
            g22.append(9)
for i in g2:    
        if i == "10h" or i == "10d" or i == "10c" or i == "10s":
            a = 2
            g22.append(10)
for i in g2:    
        if i == "Jh" or i == "Jd" or i == "Jc" or i == "Js":
            a = 2
            g22.append(11)
for i in g2:    
        if i == "Qh" or i == "Qd" or i == "Qc" or i == "Qs":
            a = 2
            g22.append(12)
for i in g2:    
        if i == "Kh" or i == "Kd" or i == "Kc" or i == "Ks":
            a = 2
            g22.append(13)
for i in g2:    
        if i == "Ah" or i == "Ad" or i == "Ac" or i == "As":
            a = 2
            g22.append(14)
