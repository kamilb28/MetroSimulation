class Train:
    moving = False
    time_state = -1
    moving_to = None
    moving_distance = 0
    moving_str = "Arrived at 0s"
    arrived_at = 0

    def __init__(self, id_num, start_station, line_num, direction="up"):
        self.id_num = id_num
        self.station = start_station
        self.line_num = line_num
        self.direction = direction
        self.position = start_station.get_coordinates()

    def get_id_num(self):
        return self.id_num

    def get_position(self):
        return self.position

    def get_moving_str(self):
        return self.moving_str

    def move(self):
        if not self.moving:
            return

        #current station coordinates
        x0, y0 = self.station.get_coordinates()

        #getting "moving to" station
        if self.direction == "up":
            if self.station.get_next_station(self.line_num) is None:
                self.direction = "down"
                self.move()
                return
            self.moving_to = self.station.get_next_station(self.line_num)
            self.moving_distance = self.station.get_next_station_distance(self.line_num)
        elif self.direction == "down":
            if self.station.get_previous_station(self.line_num) is None:
                self.direction = "up"
                self.move()
                return
            self.moving_to = self.station.get_previous_station(self.line_num)
            self.moving_distance = self.station.get_previous_station_distance(self.line_num)
        else:
            return

        #getting to station coordinates
        x1, y1 = self.moving_to.get_coordinates()

        #when train is moving position is between stations
        self.position = ((x0+x1)/2, (y0+y1)/2)

    def stop(self):
        if self.moving:
            return

        self.position = self.moving_to.get_coordinates()
        self.station = self.moving_to
        self.moving_to = None
        self.moving_distance = 0

    def update_up(self, time, speed):
        if self.time_state < 0:
            self.time_state = time
            return

        # 60ticks = 2s (irl) = 30s (sim) <-> 2ticks = 1s (sim)
        #jezeli sie nie rusza to po (0.5min)
        if not self.moving:
            self.moving_str = "Arrived at " + str(self.arrived_at) + "s"
            if (time-self.time_state)/self.station.get_departure_time() >= 1:
                self.moving = True
                self.time_state = time
                self.move()

        #jezeli sie rusza to (pretkosc 9.4m/s) counter = 30 to 15s -> 4.7m/counter
        elif self.moving:
            self.moving_str = "Moving " + str((time - self.time_state) / 2) + "s"
            if (time-self.time_state) * speed / self.moving_distance >= 1:
                self.arrived_at = (time - self.time_state) / 2
                self.moving = False
                self.time_state = time
                self.stop()

    def is_moving(self):
        return self.moving


class Inspiro(Train):
    capacity = 1500
    power = 140
    speed = 5.5

    @staticmethod
    def get_model_name():
        return "Inspiro"

    def update(self, time):
        self.update_up(time, self.speed)

class Alstom(Train):
    capacity = 1700
    power = 180
    speed = 5.6

    @staticmethod
    def get_model_name():
        return "Alstom"

    def update(self, time):
        self.update_up(time, self.speed)

class Ussr81(Train):
    capacity = 1200
    power = 110
    speed = 5.3

    def update(self, time):
        self.update_up(time, self.speed)

    @staticmethod
    def get_model_name():
        return "Ussr81"
