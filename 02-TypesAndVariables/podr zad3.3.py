score = input("write a score between 0.0 and 1.0 : ")
try:
    s = float(score)
except :
    print("write a score between 0.0 and 1.0 : ")
    score = input("write a score between 0.0 and 1.0 : ")
    
if s < 0.6 :
    print("F")
elif s >= 0.6 and s <= 0.7:
    print("D")
elif s >= 0.7 and s <= 0.8:
    print("C")
elif s >= 0.8 and s <= 0.9:
    print("B")
elif s >= 0.9 and s <=1.0:
    print("A") 