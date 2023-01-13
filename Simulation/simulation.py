import pygame

from Simulation.Trains import train as t
from Simulation.Stations import stations

line1 = stations.line1
line2 = stations.line2

trains = []

colors = {
    "BLUE": (53, 61, 255),
    "RED": (255, 24, 38),
    "WHITE": (255, 255, 255),
    "GRAY": (128, 128, 128),
    "BLACK": (0, 0, 0),
    "ORANGE": (255, 213, 68)
}

screen_size = (920, 840)


def read_data_and_paste_to():
    with open('Simulation/Data/trains') as f:
        for line in f:
            model, id_num, station_str, line, direction = line.strip().split(", ")
            id_num = int(id_num)
            line = int(line)

            station = None
            if line == 1:
                station = line1[station_str]
            elif line == 2:
                station = line2[station_str]

            if station is None or direction not in ["up", "down"]:
                print("Not correct train data")
                continue

            if model.lower() == "inspiro":
                trains.append(t.Inspiro(id_num, station, line, direction))
            elif model.lower() == "alstom":
                trains.append(t.Alstom(id_num, station, line, direction))
            elif model.lower() == "ussr81":
                trains.append(t.Ussr81(id_num, station, line, direction))

    with open('Simulation/Data/stations_1') as f:
        for line in f:
            station_str, density = line.strip().split(sep=":")

            line1[station_str].set_density(density)

    with open('Simulation/Data/stations_2') as f:
        for line in f:
            station_str, density = line.strip().split(sep=":")

            line2[station_str].set_density(density)


def draw_map(screen, font):
    screen.fill(colors["WHITE"])
    pygame.display.set_caption("Metro Simulation")

    # draw metro lines (two lines, red and blue)
    pygame.draw.line(screen, colors["BLUE"], line1["Kabaty"].get_coordinates(), line1["Młociny"].get_coordinates(), 3)
    pygame.draw.line(screen, colors["RED"], line2["Płocka"].get_coordinates(), line2["Trocka"].get_coordinates(), 3)

    # FOR LINE 1
    for station in line1.values():
        x, y = station.get_coordinates()

        # draw circle as station symbol on map
        pygame.draw.circle(screen, colors["WHITE"], (x, y), 5)
        pygame.draw.circle(screen, colors["BLACK"], (x, y), 5, 2)

        # add names on map
        if station.get_name() == "Świętokrzyska":
            screen.blit(font.render(station.get_name(), False, colors["BLACK"]), (x + 5, y + 5))
        else:
            screen.blit(font.render(station.get_name(), False, colors["BLACK"]), (x + 8, y - 5))

    # FOR LINE 2
    for station in line2.values():
        x, y = station.get_coordinates()

        # draw circle as station symbol on map
        pygame.draw.circle(screen, colors["WHITE"], (x, y), 5)
        pygame.draw.circle(screen, colors["BLACK"], (x, y), 5, 2)

        # add names on map
        if station.get_name() in ["R.Daszyńskiego", "Uniwersytet", "Stadion N.", "Szwedzka", "Trocka"]:
            screen.blit(font.render(station.get_name(), False, colors["BLACK"]), (x - 25, y - 15))
        elif station.get_name() == "C.N. Kopernik":
            screen.blit(font.render(station.get_name(), False, colors["BLACK"]), (x - 25, y + 15))
        elif station.get_name() != "Świętokrzyska":
            screen.blit(font.render(station.get_name(), False, colors["BLACK"]), (x - 25, y + 5))


def update_trains(screen, counter, font2, font3):
    screen.blit(font2.render("Trains:", False, colors["BLACK"]), (500, 20))
    for i, train in enumerate(trains):
        pygame.draw.circle(screen, colors["ORANGE"], train.get_position(), 7)

        update_train_list(screen, font3, row=i, train=train)

        train.update(counter)


def update_train_list(screen, font, row, train):
    text1 = "- train id: " + str(train.get_id_num())
    text2 = "model " + train.get_model_name()
    text3 = "current station: " + train.station.get_name()
    text4 = "state: " + ("moving" if train.is_moving() else "not moving")

    screen.blit(font.render(text1, False, colors["RED"]), (500, 50 + row * 52))
    screen.blit(font.render(text2, False, colors["BLACK"]), (500, 60 + row * 52))
    screen.blit(font.render(train.moving_str, False, colors["BLACK"]), (500, 70 + row * 52))
    screen.blit(font.render(text3, False, colors["BLACK"]), (500, 80 + row * 52))
    screen.blit(font.render(text4, False, colors["BLACK"]), (500, 90 + row * 52))


def update_stations_list(screen, font1, font2):
    text1 = "Stations on line 1"
    text2 = "Stations on line 2"
    screen.blit(font1.render(text1, False, colors["BLACK"]), (700, 20))
    screen.blit(font1.render(text2, False, colors["BLACK"]), (700, 480))

    for i, s in enumerate(line1.values()):
        text3 = "- station: " + s.get_name()
        text4 = "density: " + s.get_density()
        screen.blit(font2.render(text3, False, colors["RED"]), (700, 40 + i*20))
        screen.blit(font2.render(text4, False, colors["BLACK"]), (720, 50 + i*20))

    for i, s in enumerate(line2.values()):
        text3 = "- station: " + s.get_name()
        text4 = "density: " + s.get_density()
        screen.blit(font2.render(text3, False, colors["RED"]), (700, 500 + i*20))
        screen.blit(font2.render(text4, False, colors["BLACK"]), (720, 510 + i*20))

def print_time(screen, font, time):
    from datetime import timedelta
    # print Time (one second in rl is counter // fps) fps = 26

    # eg. time = 30 -> 30 // 30 -> 1, so 1*15 = 15s.
    #that mean that in one second in rl equals 15s in sim
    seconds = time//2
    screen.blit(font.render("Time: " + str(timedelta(seconds=seconds)), False, colors["BLACK"]), (0, 0))


def pause():
    is_pause = True
    while is_pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_pause = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def run():
    read_data_and_paste_to()

    pygame.init()
    done = False
    screen = pygame.display.set_mode(screen_size)

    font1 = pygame.font.SysFont('Calibri', 10, True, False)
    font2 = pygame.font.SysFont('Arial', 20, True, False)
    font3 = pygame.font.SysFont('Arial', 10, True, False)

    clock = pygame.time.Clock()
    fps = 30
    counter = 0

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause()

        draw_map(screen, font1)

        update_trains(screen, counter, font2, font3)
        update_stations_list(screen, font2, font3)

        print_time(screen, font2, counter)

        pygame.display.flip()
        counter += 1
        clock.tick(fps)

    pygame.quit()
