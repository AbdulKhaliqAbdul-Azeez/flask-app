import random
global house_choice
global car_choice
global career_choice 
global city_choice
house_choice = ""
car_choice =""
career_choice =""
city_choice = ""
def mash(house, car, career, city):
    global house_choice
    global car_choice
    global career_choice 
    global city_choice
    
    houses = ["Mansion","Apartment","Condo","Lake House"]
    if house == "":
        houses.append(house)
    rand_choice = random.randrange(0,len(houses))
    house_choice = houses[rand_choice]

    
    cars = ["Ford","Jeep","Lexus","Subaru","Tesla"]
    if car == "":
        cars.append(car)
    rand_choice = random.randrange(0,len(cars))
    car_choice = cars[rand_choice]

    
    careers = ["Actor","Piolt","Softwar Dev","Nurse","Doctor"]
    if career == "":
        careers.append(career)
    rand_choice = random.randrange(0,len(careers))
    career_choice = careers[rand_choice]

    
    cities = ["NYC","Jersey City","Dallas","Orlando","LA"]
    if city == "":
        cities.append(city)
    rand_choice = random.randrange(0,len(cities))
    city_choice = cities[rand_choice]

    return "You will live in a "+ house_choice +" you'll drive a "+ car_choice+ " you will work as a "+career_choice+" and you will live in "+city_choice
