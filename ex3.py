cars = 100
passengers = 60
drivers = 90
spac_in_a_car = 4.0
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * spac_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are",cars,"cars avaiable."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven ,"empty cars today."
print "We can transport",carpool_capacity, "people today."
print "WE have",passengers, "to carpool today"
print "We need to put about",average_passengers_per_car, "in each car."
