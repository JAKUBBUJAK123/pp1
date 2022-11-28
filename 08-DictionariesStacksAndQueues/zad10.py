arr = [{'country': "Poland", "Population":'40 mln'}, {'country':'German','population': '83 mln'}
 , {'country':"Spain",'population':'47 mln' }, {'country':"Italy",'population':"59 mln" }, {'country':"Russia", 'population': "143 mln"}]


for i in arr :
    for x in i.values():
            print(f'{x}' , end=" ")
    print(" ")