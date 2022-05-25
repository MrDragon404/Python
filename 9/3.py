array = ["CSGO", "Doom", "Rocet Luga", "Whitcher"]
array[0] ="Fortnite"
array.append("DOTA")
#print(len(array), array[3], array[1:3], array[::-1])
array1 = [n for n in array if len(n) == 4]
print(array1)

cities = ("Евпатория","Симферопаль","Саки","Севастопалб")
cities1 = [n for n in cities ]
print(len(cities), cities[0], cities[-1])


products = {"хлеб", "батон", "булка", "круасан"}
products.add("батон")
print(products)

arr = [1,2,3,4,5,2]
sum_arr = sum(arr)
sum_uniq = sum(set(arr))
print(sum_arr, sum_uniq, sum_arr-sum_uniq)

str = "око"
print(str == str[::-1])





