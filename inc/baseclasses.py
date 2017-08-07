
# stopTdi
class Stop(object):
    def __init__(self, duid, last_modification_timestamp, is_deleted, foo, number, short_name, long_name, latitude, longitude, altitude):
        #super(Base, self).__init__(duid, last_modification_timestamp, is_deleted, foo)
        self.duid = duid # 6350927368470660862
        self.last_modification_timestamp = last_modification_timestamp # 1501839625957
        self.is_deleted = is_deleted # false
        self.foo = foo # 0
        self.number = number # 33206
        self.short_name = short_name # ARDNCR
        self.long_name = long_name # Ardnacrusha (ESB Station Car Park)
        self.latitude = latitude # 189745020
        self.longitude = longitude # -31027320
        self.altitude = altitude # 2147483646
# Base.__init__(duid, last_modification_timestamp, is_deleted, foo)

#links to Trip and Pattern
# vehicleTdi
class Bus(object):
    def __init__(self, duid, last_modification_timestamp, is_deleted, foo, category, geo_position_status, reference_time, latitude, longitude, bearing, is_accessible, has_bike_rack, vehicle_number, operational_number, tripDuid, patternDuid):
        #Base.__init__(duid, last_modification_timestamp, is_deleted, foo)
        self.duid = duid # 6350927368470660862
        self.last_modification_timestamp = last_modification_timestamp # 1501839625957
        self.is_deleted = is_deleted # false
        self.foo = foo # 0
        self.category = category # 5,
        self.geo_position_status = geo_position_status # 1,
        self.reference_time = reference_time  # 1502041712,
        self.latitude = latitude # 189649591,
        self.longitude = longitude # -31002712,
        self.bearing = bearing # 211,
        self.is_accessible = is_accessible # 0,
        self.has_bike_rack = has_bike_rack # 0,
        self.vehicle_number = vehicle_number # 672,
        self.operational_number = operational_number # 672,
        self.tripDuid = tripDuid # class TripRef
        self.patternDuid = patternDuid # class PatternRef

# stopPointTdi
class StopPoint(object):
    def __init__(self, duid, last_modification_timestamp, is_deleted, foo, type, number, long_name, latitude, longitude, bearing, code, stopDuid):
        self.duid = duid # 6350927368470660862
        self.last_modification_timestamp = last_modification_timestamp # 1501839625957
        self.is_deleted = is_deleted # false
        self.foo = foo # 0
        self.type = type # 1
        self.number = number # 1
        self.long_name = long_name # Ennis Rd (Radisson Hotel),
        self.latitude = latitude # 189657388,
        self.longitude = longitude # -31363751,
        self.bearing = bearing # 100,
        self.code = code # 337841,
        self.stopDuid = stopDuid

# stopPassageTdi
class Passage(object):
    def __init__(self, duid, last_modification_timestamp, is_deleted, foo, direction, congestion_level, accuracy_level, status, is_accessible, latitude, longitude, bearing, has_bike_rack, category, arrival_scheduled_utc, arrival_scheduled, arrival_actual_utc, arrival_actual, arrival_service_mode, arrival_direction_text, arrival_type, departure_scheduled_utc, departure_scheduled, departure_actual_utc, departure_actual, departure_service_mode, departure_direction_text, departure_type, patternDuid, routeDuid, tripDuid, stopPointDuid, vehicleDuid):
        self.duid = duid # 6350927368470660862
        self.last_modification_timestamp = last_modification_timestamp # 1501839625957
        self.is_deleted = is_deleted # false
        self.foo = foo # 0
        self.direction = direction # 2,
        self.congestion_level = congestion_level # 1,
        self.accuracy_level = accuracy_level # 3,
        self.status = status # 4,
        self.is_accessible = is_accessible # 0,
        self.latitude = latitude # 189607756,
        self.longitude = longitude # -31034357,
        self.bearing = bearing # 245,
        self.has_bike_rack = has_bike_rack # 0,
        self.category = category # 5,
        self.arrival_scheduled_utc = arrival_scheduled_utc
        self.arrival_scheduled = arrival_scheduled
        self.arrival_actual_utc = arrival_actual_utc
        self.arrival_actual = arrival_actual
        self.arrival_service_mode = arrival_service_mode
        self.arrival_direction_text = arrival_direction_text
        self.arrival_type = arrival_type
        self.departure_scheduled_utc = departure_scheduled_utc
        self.departure_scheduled = departure_scheduled
        self.departure_actual_utc = departure_actual_utc
        self.departure_actual = departure_actual
        self.departure_service_mode = departure_service_mode
        self.departure_direction_text = departure_direction_text
        self.departure_type = departure_type
        self.patternDuid = patternDuid
        self.routeDuid = routeDuid
        self.tripDuid = tripDuid
        self.stopPointDuid = stopPointDuid
        self.vehicleDuid = vehicleDuid
