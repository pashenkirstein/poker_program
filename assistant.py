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
print("input yours flop cards:")
fp = input()
sp = input()
l.remove(fp)
l.remove(sp)
hand = [fp,sp]
print("yours hand: ", hand)
print("input flop cards: ")
f1 = input()
f2 = input()
f3 = input()
l.remove(f1)
l.remove(f2)
l.remove(f3)
flop = [f1,f2,f3]
print("flop is: ", flop)
length = len(l)-2
print("number of cards: ", length)
strflop = flop[0] + flop[1] + flop[2] 
print(strflop)
ll =  ''.join(l)
print(ll)
sc = ll.count("4")
ss = ll.count("h")
print(sc)
print(ss)




