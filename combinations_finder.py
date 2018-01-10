# hands
hand1digits = [14, 13, 14, 14, 13, 14, 13]
hand2digits = [6, 6, 11, 3, 7, 2, 13]
hand1suit = [2, 4, 3, 1, 1, 4, 2]
hand2suit = [4, 2, 3, 1, 1, 4, 2]
# begining
print("there are two combinations on table.")
print("first one: ")
print(hand1digits)
print(hand1suit)
print("second one: ")
print(hand2digits)
print(hand2suit)
# finding royal flush
RF = 0
h1 = ["5d", "4h", "10h", "Jh", "Qh", "Kh", "Ah"]
RFd = [10, 11, 12, 13, 14]#first condition
HRF = ["10h", "Jh", "Qh", "Kh", "Ah"]
DRF = ["10d", "Jd", "Qd", "Kd", "Ad"]
CRF = ["10c", "Jc", "Qc", "Kc", "Ac"]
SRF = ["10s", "Js", "Qs", "Ks", "As"]
r1H = len(list(set(h1) & set(HRF)))
if r1H >= 5:
    RF = 1
r1D = len(list(set(h1) & set(DRF)))
if r1D >= 5:
    RF = 1
r1C = len(list(set(h1) & set(CRF)))
if r1C >= 5:
    RF = 1
r1S = len(list(set(h1) & set(SRF)))
if r1S >= 5:
    RF = 1
# finding pairs, two pairs, triple, full house, quads
repeats = []
repeats.insert(2, hand1digits.count(2))
repeats.insert(3, hand1digits.count(3))
repeats.insert(4, hand1digits.count(4))
repeats.insert(5, hand1digits.count(5))
repeats.insert(6, hand1digits.count(6))
repeats.insert(7, hand1digits.count(7))
repeats.insert(8, hand1digits.count(8))
repeats.insert(9, hand1digits.count(9))
repeats.insert(10, hand1digits.count(10))
repeats.insert(11, hand1digits.count(11))
repeats.insert(12, hand1digits.count(12))
repeats.insert(13, hand1digits.count(13))
repeats.insert(14, hand1digits.count(14))
a = max(repeats)
b = repeats.index(max(repeats)) + 2
#print(repeats)
#for i in repeats:
    #if i == 4:
        #sQ = (repeats.index(i) + 2)*4
        #print("quads")
    #if i == 3:
        #sT = (repeats.index(i) + 2)*3
        #print("triple")

