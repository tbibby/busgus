import pickle, os
from inc import baseclasses

#unarchive from pickle
def readData(filename):
    return pickle.load( open(filename, "rb") )

stopPoints = readData("stopPoints.dat")
stops = readData("stops.dat")
vehicles = readData("vehicles.dat")
passages = readData("passagesStopPoints.dat")


print "We have",len(stops),"stops,",len(stopPoints),"stop points,",len(vehicles),"vehicles and",len(passages),"passages."

#this is unfinished. Get a stop and display the passage data
user_input = raw_input("Enter a stop name: ")
filtered_stops = [stopPoint.long_name for stopPoint in stopPoints if user_input.lower() in stopPoint.long_name.lower()]
if len(filtered_stops) > 0:
    loop_count = 1
    for stop in filtered_stops:
        print loop_count, stop
        loop_count += 1
    number_input = raw_input("Enter your choice: ")
    print "Chosen:", filtered_stops[int(number_input)]
else:
    print "Sorry, could not find a stop with that name. Bye."

result = [stopPoint.duid for stopPoint in stopPoints if "University" in stopPoint.long_name]
print result[0]

stop = [stopPoint.long_name for stopPoint in stopPoints if "University of Limerick" in stopPoint.long_name]
print stop[0]

print "sched actual"

davesPassageObjects = sorted([passage for passage in passages if result[0] == passage.stopPointDuid], key=lambda passage: passage.arrival_scheduled_utc)

for passageObject in davesPassageObjects:
    print passageObject.arrival_scheduled, passageObject.arrival_actual

davesPassages = [passage.arrival_actual_utc - passage.arrival_scheduled_utc for passage in passages if result[0] == passage.stopPointDuid]
print davesPassages
