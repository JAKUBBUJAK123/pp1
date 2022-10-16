EHours = 45
ERate = 10
pay = 0
i = 1
while  i <= EHours :
    if i <= 40:
        pay += 10
        i += 1
    else:
        pay += 15
        i += 1
else:
    print(pay)
