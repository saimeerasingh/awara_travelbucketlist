
from models.country import Country
from models.city import City
from models.destination import Destination

import repositories.country_repository as country_repository 
import repositories.city_repository as city_repository
import repositories.destination_repository as destination_repository

country_repository.delete_all()
city_repository.delete_all()
destination_repository.delete_all()

country1 = Country('India','Asia',True)
country_repository.save(country1)

country2 = Country('France','Europe',True)
country_repository.save(country2)

country3 = Country('Australia','Australia',False)
country_repository.save(country3)

country4 = Country('California','North America',False)
country_repository.save(country4)

country5 = Country('Brazil','South America',False)
country_repository.save(country5)

country6 = Country('Spain','Europe',False)
country_repository.save(country6)

country7 = Country('Kenya','Africa',False)
country_repository.save(country7)

country8 = Country('Turkey','Asia',False)
country_repository.save(country8)

city1 = City('Mumbai',True,country1)
city_repository.save(city1)

city2 = City('Delhi',True,country1)
city_repository.save(city2)

city3 = City('Jaipur',False,country1)
city_repository.save(city3)

city4 = City('Paris',True,country2)
city_repository.save(city4)

city5 = City('Marseille',False,country2)
city_repository.save(city5)

city6 = City('Sydney',False,country3)
city_repository.save(city6)

city7 = City('Los Angeles',False,country4)
city_repository.save(city7)

city8 = City('Sao Paulo',False,country5)
city_repository.save(city8)

city9 = City('Barcelona',False,country6)
city_repository.save(city9)

city10 = City('Nairobi',False,country7)
city_repository.save(city10)

city11 = City('Istanbul',False,country8)
city_repository.save(city11)

destination1 = Destination('Gateway of India', True,city1,country1)
destination_repository.save(destination1)

destination2 = Destination('India Gate', False, city2,country1)
destination_repository.save(destination2)

destination3 = Destination('Hawa Mahal', False, city3,country1)
destination_repository.save(destination3)

destination4 = Destination('Eiffel Tower', True, city4,country2)
destination_repository.save(destination4)

destination5 = Destination('Opera House', False, city6,country3)
destination_repository.save(destination5)

