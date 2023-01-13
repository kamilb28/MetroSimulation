class Station:
    def __init__(self, name, density="low", coordinates=(0, 0)):
        self.density = density
        self.name = name
        self.coordinates = coordinates

    def get_name(self):
        return self.name

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def set_density(self, density):
        self.density = density

    def get_density(self):
        return self.density

    def get_departure_time(self):
        if self.density == "low":
            return 40  # 20s
        elif self.density == "medium":
            return 60  # 30s
        elif self.density == "high":
            return 80  # 40s
        elif self.density == "very_high":
            return 100  # 50s
        else:
            return 60


class MiddleStation(Station):
    station1 = None
    station2 = None
    distance1 = 0
    distance2 = 0

    def add_neighbours_stations(self, station1, distance1, station2, distance2):
        self.station1 = station1
        self.station2 = station2
        self.distance1 = distance1
        self.distance2 = distance2

    def get_next_station(self, line_num):
        return self.station2

    def get_next_station_distance(self, line_num):
        return self.distance2

    def get_previous_station(self, line_num):
        return self.station1

    def get_previous_station_distance(self, line_num):
        return self.distance1


class LastStation(Station):
    station1 = None
    station2 = None
    distance = 0

    def add_neighbours_stations(self, station, distance, start_station):
        if start_station:
            self.station2 = station
        else:
            self.station1 = station
        self.distance = distance

    def get_next_station(self, line_num):
        return self.station2

    def get_previous_station(self, line_num):
        return self.station1

    def get_next_station_distance(self, line_num):
        return self.distance

    def get_previous_station_distance(self, line_num):
        return self.distance


class CrossingStation(Station):
    station1_line1 = None
    station2_line1 = None
    station1_line2 = None
    station2_line2 = None

    distance1_line1 = 0
    distance2_line1 = 0
    distance1_line2 = 0
    distance2_line2 = 0

    def add_neighbours_stations_on_line1(self, station1_l1, dis_1, station2_l1, dis_2):
        self.station1_line1 = station1_l1
        self.station2_line1 = station2_l1
        self.distance1_line1 = dis_1
        self.distance2_line1 = dis_2

    def add_neighbours_stations_on_line2(self, station1_l2, dis_1, station2_l2, dis_2):
        self.station1_line2 = station1_l2
        self.station2_line2 = station2_l2
        self.distance1_line2 = dis_1
        self.distance2_line2 = dis_2

    def get_next_station(self, line_num):
        if line_num == 1:
            return self.station2_line1
        elif line_num == 2:
            return self.station2_line2

    def get_previous_station(self, line_num):
        if line_num == 1:
            return self.station1_line1
        elif line_num == 2:
            return self.station1_line2

    def get_next_station_distance(self, line_num):
        if line_num == 1:
            return self.distance2_line1
        elif line_num == 2:
            return self.distance2_line2

    def get_previous_station_distance(self, line_num):
        if line_num == 1:
            return self.distance1_line1
        elif line_num == 2:
            return self.distance1_line2
