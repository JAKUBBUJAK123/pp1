import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
avg = 0
for i in range(len(temperatures)):
    avg += int(temperatures[i]) 

avg = avg/ len(temperatures)

print(avg)
print(temperatures)