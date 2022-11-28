import json

file = open('favourite.json' , 'w' )
films = {
    'film name ' : 'Avengers end game',
    "heroes" : ["spiderMan" , "Iron Man" , "black panther"],
    "villians" : "thanos",
    "film lenght (minutes)" : 150,
    "rating" : "9.5/10"
}

json.dump(films, file, indent= 1)

file.close()
