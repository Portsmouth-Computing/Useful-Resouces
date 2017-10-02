"""Write a function travelStatistics which asks the user to input the average speed
(in km/hour) and duration (in hours) of a car journey. The function should then
output the overall distance travelled (in km), and the amount of fuel used (in litres) assuming a fuel efficiency of 5 km/litre."""


def travelStatistics():
    average_speed = input("Average speed in km/hour")
    duration = input("Duration of journey in hours")
    distance_travelled = average_speed * duration
    fuel_used = 5 / duration
    print("Distance traveled is {}km and the fuel used is {}".format(distance_travelled, fuel_used))
