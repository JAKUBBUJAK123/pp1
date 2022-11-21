arr = ["spiderman", "superman", "Batman", "Aquaman", "Joker"]


file = open('films.txt' , 'w')

for i in range(len(arr)):
    file.write(arr[i])
    file.write("\n")

file.close()