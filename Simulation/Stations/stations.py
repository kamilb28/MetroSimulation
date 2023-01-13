from Simulation.Stations import station

line1 = {
    "Kabaty":           station.LastStation("Kabaty"),
    "Natolin":          station.MiddleStation("Natolin"),
    "Imielin":          station.MiddleStation("Imielin"),
    "Stokłosy":         station.MiddleStation("Stokłosy"),
    "Ursynów":          station.MiddleStation("Ursynów"),
    "Służew":           station.MiddleStation("Służew"),
    "Wilanowska":       station.MiddleStation("Wilanowska"),
    "Wierzbno":         station.MiddleStation("Wierzbno"),
    "Racławicka":       station.MiddleStation("Racławicka"),
    "Pole Mokotowskie": station.MiddleStation("Pole Mokotowskie"),
    "Politechnika":     station.MiddleStation("Politechnika"),
    "Centrum":          station.MiddleStation("Centrum"),
    "Świętokrzyska":    station.CrossingStation("Świętokrzyska"),
    "Ratusz Arsenał":   station.MiddleStation("Ratusz Arsenał"),
    "Dworzec Gdański":  station.MiddleStation("Dworzec Gdański"),
    "Plac Wilsona":     station.MiddleStation("Plac Wilsona"),
    "Marymont":         station.MiddleStation("Marymont"),
    "Słodowiec":        station.MiddleStation("Słodowiec"),
    "Stare Bielany":    station.MiddleStation("Stare Bielany"),
    "Wawrzyszew":       station.MiddleStation("Wawrzyszew"),
    "Młociny":          station.LastStation("Młociny")
}

line1["Kabaty"].add_neighbours_stations(line1["Natolin"], 1162, start_station=True)
line1["Natolin"].add_neighbours_stations(line1["Kabaty"], 1162, line1["Imielin"], 1143)
line1["Imielin"].add_neighbours_stations(line1["Natolin"], 1143, line1["Stokłosy"], 1108)
line1["Stokłosy"].add_neighbours_stations(line1["Imielin"], 1108, line1["Ursynów"], 835)
line1["Ursynów"].add_neighbours_stations(line1["Stokłosy"], 835, line1["Służew"], 1189)
line1["Służew"].add_neighbours_stations(line1["Ursynów"], 1189, line1["Wilanowska"], 1124)
line1["Wilanowska"].add_neighbours_stations(line1["Służew"], 1124, line1["Wierzbno"], 1007)
line1["Wierzbno"].add_neighbours_stations(line1["Wilanowska"], 1007, line1["Racławicka"], 1047)
line1["Racławicka"].add_neighbours_stations(line1["Wierzbno"], 1047, line1["Pole Mokotowskie"], 1142)
line1["Pole Mokotowskie"].add_neighbours_stations(line1["Racławicka"], 1142, line1["Politechnika"], 1248)
line1["Politechnika"].add_neighbours_stations(line1["Pole Mokotowskie"], 1248, line1["Centrum"], 1450)
line1["Centrum"].add_neighbours_stations(line1["Politechnika"], 1450, line1["Świętokrzyska"], 577)
line1["Świętokrzyska"].add_neighbours_stations_on_line1(line1["Centrum"], 577, line1["Ratusz Arsenał"], 1128)
line1["Ratusz Arsenał"].add_neighbours_stations(line1["Świętokrzyska"], 1128, line1["Dworzec Gdański"], 1534)
line1["Dworzec Gdański"].add_neighbours_stations(line1["Ratusz Arsenał"], 1534, line1["Plac Wilsona"], 1463)
line1["Plac Wilsona"].add_neighbours_stations(line1["Dworzec Gdański"], 1463, line1["Marymont"], 896)
line1["Marymont"].add_neighbours_stations(line1["Plac Wilsona"], 896, line1["Słodowiec"], 1014)
line1["Słodowiec"].add_neighbours_stations(line1["Marymont"], 1014, line1["Stare Bielany"], 918)
line1["Stare Bielany"].add_neighbours_stations(line1["Słodowiec"], 918, line1["Wawrzyszew"], 844)
line1["Wawrzyszew"].add_neighbours_stations(line1["Stare Bielany"], 844, line1["Młociny"], 819)
line1["Młociny"].add_neighbours_stations(line1["Wawrzyszew"], 819, start_station=False)

middle_line = 180

for i, s in enumerate(line1.values()):
    s.set_coordinates((middle_line, 820 - i*40))

line2 = {
    "Płocka":                 station.LastStation("Płocka"),
    "Rondo Daszyńskiego":     station.MiddleStation("R.Daszyńskiego"),
    "Rondo ONZ":              station.MiddleStation("R.ONZ"),
    "Świętokrzyska":          line1["Świętokrzyska"],
    "Uniwersytet":            station.MiddleStation("Uniwersytet"),
    "Centrum Nauki Kopernik": station.MiddleStation("C.N. Kopernik"),
    "Stadion Narodowy":       station.MiddleStation("Stadion N."),
    "Dworzec Wileński":       station.MiddleStation("Dw.Wileński"),
    "Szwedzka":               station.MiddleStation("Szwedzka"),
    "Targówek":               station.MiddleStation("Targówek"),
    "Trocka":                 station.LastStation("Trocka")
}

line2["Płocka"].add_neighbours_stations(line2["Rondo Daszyńskiego"], 1490, start_station=True)
line2["Rondo Daszyńskiego"].add_neighbours_stations(line2["Płocka"], 1490, line2["Rondo ONZ"], 1040)
line2["Rondo ONZ"].add_neighbours_stations(line2["Rondo Daszyńskiego"], 1040, line2["Świętokrzyska"], 719)
line2["Świętokrzyska"].add_neighbours_stations_on_line2(line2["Rondo ONZ"], 719, line2["Uniwersytet"], 633)
line2["Uniwersytet"].add_neighbours_stations(line2["Świętokrzyska"], 633, line2["Centrum Nauki Kopernik"], 1020)
line2["Centrum Nauki Kopernik"].add_neighbours_stations(line2["Uniwersytet"], 1020, line2["Stadion Narodowy"], 1230)
line2["Stadion Narodowy"].add_neighbours_stations(line2["Centrum Nauki Kopernik"], 1230, line2["Dworzec Wileński"], 1002)
line2["Dworzec Wileński"].add_neighbours_stations(line2["Stadion Narodowy"], 1002, line2["Szwedzka"], 1364)
line2["Szwedzka"].add_neighbours_stations(line2["Dworzec Wileński"], 1364, line2["Targówek"], 925)
line2["Targówek"].add_neighbours_stations(line2["Szwedzka"], 925, line2["Trocka"], 721)
line2["Trocka"].add_neighbours_stations(line2["Targówek"], 721, start_station=False)

# liczba_stacji_przed_świętokrzyska = 3
num_bef = 3
x, y = line1["Świętokrzyska"].get_coordinates()

for i, s in enumerate(line2.values()):
    s.set_coordinates((x - (num_bef * 40) + i*40, y))
