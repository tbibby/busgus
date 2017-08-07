import json, urllib, time, pickle, os
from inc import baseclasses

# retrieve json from url
def dictFromUrl(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

# return value for key, with default value
def checkDictValue(dict, keyString, default):
    if keyString in dict:
        return dict[keyString]
    else:
        return default

# return value for doubly-nested key, with default value
def checkSecondLevelDictValue(dict, firstKeyString, secondKeyString, default):
    if firstKeyString in dict:
        if secondKeyString in dict[firstKeyString]:
            return dict[firstKeyString][secondKeyString]
    return default

#ok this is getting ridiculous
def checkThirdLevelDictValue(dict, firstKeyString, secondKeyString, thirdKeyString, default):
    if firstKeyString in dict:
        if secondKeyString in dict[firstKeyString]:
            if thirdKeyString in dict[firstKeyString][secondKeyString]:
                return dict[firstKeyString][secondKeyString][thirdKeyString]
    return default

# download a bunch of stuff from the server, and archive it
def downloadData():
    stopsFileName = "stops.dat"
    stopPointsFileName = "stopPoints.dat"
    vehiclesFileName = "vehicles.dat"
    passagesFileName = "passagesStopPoints.dat"
    
    ## Get stops
    stopData = dictFromUrl("http://www.buseireann.ie/inc/proto/stopTdi.php?latitude_north=189863582&latitude_south=189391544&longitude_east=-30765864&longitude_west=-31468225&_=1502041710608")
    #stopUrl = "http://www.buseireann.ie/inc/proto/stopTdi.php?latitude_north=189863582&latitude_south=189391544&longitude_east=-30765864&longitude_west=-31468225&_=1502041710608"
    #stopResponse = urllib.urlopen(stopUrl)
    #stopData = json.loads(stopResponse.read())
    # there's an inner dict, each key is bus_stop_x, apart from the last key, which is foo
    innerDict = stopData["stopTdi"]
    stops = []
    for key, dict in innerDict.iteritems():
        if key != "foo":
            stopObject = baseclasses.Stop(dict["duid"],dict["last_modification_timestamp"],dict["is_deleted"],dict["foo"],dict["number"],dict["short_name"],dict["long_name"],dict["latitude"],dict["longitude"],dict["altitude"])
            stops.append(stopObject)
    print "Added", len(stops), "stops"
    # save this to pickle
    with open(stopsFileName, 'wb') as f:
        pickle.dump(stops, f)
    

    ## Get vehicles
    vehicleData = dictFromUrl("http://www.buseireann.ie/inc/proto/vehicleTdi.php?latitude_north=189863582&latitude_south=189391544&longitude_east=-30765864&longitude_west=-31468225&_=1502041710608")
    vehicleInnerDict = vehicleData["vehicleTdi"]
    vehicles = []
    for key, dict in vehicleInnerDict.iteritems():
        #print dict
        if key != "foo":
            # doesn't always have a trip or a pattern
            patternDuid = checkSecondLevelDictValue(dict, "pattern_duid", "duid", 0)
            tripDuid = checkSecondLevelDictValue(dict, "trip_duid", "duid", 0)
            vehicleObject = baseclasses.Bus(dict["duid"],dict["last_modification_timestamp"],dict["is_deleted"],dict["foo"],dict["category"],dict["geo_position_status"],dict["reference_time"],dict["latitude"],dict["longitude"],dict["bearing"],dict["is_accessible"],dict["has_bike_rack"],dict["vehicle_number"],dict["operational_number"],patternDuid,tripDuid)
            vehicles.append(vehicleObject)
    print "Added", len(vehicles), "vehicles"
    with open(vehiclesFileName, 'wb') as f:
        pickle.dump(vehicles, f)

    ## Get stop points
    stopPointData = dictFromUrl("http://www.buseireann.ie/inc/proto/stopPointTdi.php?latitude_north=189863582&latitude_south=189391544&longitude_east=-30765864&longitude_west=-31468225&_=1502041710608")
    stopPointInnerDict = stopPointData["stopPointTdi"]
    stopPoints = []
    for key, dict in stopPointInnerDict.iteritems():
        if key != "foo":
            stopPointObject = baseclasses.StopPoint(dict["duid"],dict["last_modification_timestamp"],dict["is_deleted"],dict["foo"],dict["type"],dict["number"],dict["long_name"],dict["latitude"],dict["longitude"],dict["bearing"],dict["code"],dict["stop_duid"]["duid"])
            stopPoints.append(stopPointObject)
    print "Added", len(stopPoints), "stop points"
    with open(stopPointsFileName, 'wb') as f:
        pickle.dump(stopPoints, f)

    # Get passage data for each stop point
# "passage" in this case is a series of data points when a bus arrives at a particular stop
    allPassages = []
    for stopPoint in stopPoints:
        url = "http://buseireann.ie/inc/proto/stopPassageTdi.php?stop_point=" + str(stopPoint.duid)
        #print "Getting", url
        passageData = dictFromUrl(url)
        passageInnerDict = passageData["stopPassageTdi"]
        stopPassages = []
        for key, dict in passageInnerDict.iteritems():
            if key != "foo":
                congestionlevel = checkDictValue(dict, "congestion_level", 0)
                isaccessible = checkDictValue(dict, "is_accessible", 0)
                hasbikerack = checkDictValue(dict, "has_bike_rack", 0)
                category = checkDictValue(dict, "category", 0)
                vehicleDuid = checkSecondLevelDictValue(dict, "vehicle_duid", "duid", 0)
                arrivalScheduledUtc = checkSecondLevelDictValue(dict, "arrival_data", "scheduled_passage_time_utc", 0)
                arrivalScheduled = checkSecondLevelDictValue(dict, "arrival_data", "scheduled_passage_time", "03:00")
                arrivalActualUtc = checkSecondLevelDictValue(dict, "arrival_data", "actual_passage_time_utc", 0)
                arrivalActual = checkSecondLevelDictValue(dict, "arrival_data", "actual_passage_time", "03:00")
                arrivalServiceMode = checkSecondLevelDictValue(dict, "arrival_data", "service_mode", 1)
                arrivalDirectionText = checkThirdLevelDictValue(dict, "arrival_data", "multilingual_direction_text", "defaultValue","")
                arrivalType = checkSecondLevelDictValue(dict, "arrival_data", "type", 0)
                departureScheduledUtc = checkSecondLevelDictValue(dict, "departure_data", "scheduled_passage_time_utc", 0)
                departureScheduled = checkSecondLevelDictValue(dict, "departure_data", "scheduled_passage_time", "03:00")
                departureActualUtc = checkSecondLevelDictValue(dict, "departure_data", "actual_passage_time_utc", 0)
                departureActual = checkSecondLevelDictValue(dict, "departure_data", "actual_passage_time", "03:00")
                departureServiceMode = checkSecondLevelDictValue(dict, "departure_data", "service_mode", 1)
                departureDirectionText = checkThirdLevelDictValue(dict, "departure_data", "multilingual_direction_text", "defaultValue","")
                departureType = checkSecondLevelDictValue(dict, "departure_data", "type", 0)
                #print dict
                passageObject = baseclasses.Passage(dict["duid"],dict["last_modification_timestamp"],dict["is_deleted"],dict["foo"],dict["direction"],congestionlevel,dict["accuracy_level"],dict["status"],isaccessible,dict["latitude"],dict["longitude"],dict["bearing"], hasbikerack, category, arrivalScheduledUtc, arrivalScheduled, arrivalActualUtc, arrivalActual, arrivalServiceMode, arrivalDirectionText, arrivalType, departureScheduledUtc, departureScheduled, departureActualUtc, departureActual, departureServiceMode, departureDirectionText, departureType, dict["pattern_duid"]["duid"], dict["route_duid"]["duid"], dict["trip_duid"]["duid"], dict["stop_point_duid"]["duid"], vehicleDuid)
                stopPassages.append(passageObject)
        time.sleep(1)
        allPassages += stopPassages
#  print "=========="
    print "Added", len(allPassages), "passages"
    with open(passagesFileName, 'wb') as f:
        pickle.dump(allPassages, f)

# actually download the data
downloadData()




