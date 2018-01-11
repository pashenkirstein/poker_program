#finding straight-flush-D
h1 = ["5d", "3d", "Jd", "Qs", "2d", "4d", "Ad"]
h2 = ["4d", "5d", "7d", "6d", "As", "8d", "Qd"]
SF = 0
sSF = 0
DS1 = ["2d", "3d", "4d", "5d", "6d"]
DS2 = ["3d", "4d", "5d", "6d", "7d"]
DS3 = ["4d", "5d", "6d", "7d", "8d"]
DS4 = ["5d", "6d", "7d", "8d", "9d"]
DS5 = ["6d", "7d", "8d", "9d", "10d"]
DS6 = ["7d", "8d", "9d", "10d", "Jd"]
DS7 = ["8d", "9d", "10d", "Jd", "Qd"]
DS8 = ["9d", "10d", "Jd", "Qd", "Kd"]
DS9 = ["2d", "3d", "4d", "5d", "Ad"]
def straight_flush_d(lst):
    rD = len(list(set(lst) & set(DS1)))
    if rD >= 5:
        global SF
        global sSF
        SF = 1
        sSF = 20
    rD = len(list(set(lst) & set(DS2)))
    if rD >= 5:
        SF = 1
        sSF = 25
    rD = len(list(set(lst) & set(DS3)))
    if rD >= 5:
        SF = 1
        sSF = 30
    rD = len(list(set(lst) & set(DS4)))
    if rD >= 5:
        SF = 1
        sSF = 35
    rD = len(list(set(lst) & set(DS5)))
    if rD >= 5:
        SF = 1
        sSF = 40
    rD = len(list(set(lst) & set(DS6)))
    if rD >= 5:
        SF = 1
        sSF = 45
    rD = len(list(set(lst) & set(DS7)))
    if rD >= 5:
        SF = 1
        sSF = 50
    rD = len(list(set(lst) & set(DS8)))
    if rD >= 5:
        SF = 1
        sSF = 55
    rD = len(list(set(lst) & set(DS9)))
    if rD >= 5:
        SF = 1
        sSF = 15
straight_flush_d(h1)
if SF == 1:
    print("hand-1 has streight-flush with sum: ", sSF)
SF = 0
sSF = 0
straight_flush_d(h2)
if SF == 1:
    print("hand-2 has streight-flush with sum: ", sSF)
