import re
def f(player1,player2):
    one = re.findall('[AKQJT]', player1)
    onen = re.findall('[2-9]' , player1)
    two = re.findall('[AKQJT]', player2)
    twon = re.findall('[2-9]', player2)
    sum1 = len(one) * 10
    sum2 = len(two) * 10
    for i in onen :
        sum1 += eval(i)
    for j in twon:
        sum2 += eval(j)

    if sum1 > sum2 :
        return True
    else:
        return False

print(f("AJ9","K8TTT"))