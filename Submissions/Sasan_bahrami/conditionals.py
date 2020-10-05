my_city = 'Tehran'
my_city_population = 8490000
my_previous_city_population = 7000000

if my_city_population > 10000000:
    print('My City is a Mega City')
elif my_city_population > 1500000:
    print('My city is a large metropolitan area')
    if my_city_population > my_previous_city_population:
        print("My city is bigger than previous ")
    else:
        print('My city is bigger than the previous')
elif my_city_population > 500000:
    print('My city is a metropolitan area')
elif my_city_population > 200000:
    print('My city is a medium metropolitan area')
else:
    print('My city is neither a MegaCity nor metropolitan area')