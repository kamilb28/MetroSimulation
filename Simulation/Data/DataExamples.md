### Trains:
- format : $train_model, $train_id, $start_station, $line_number, $direction*
---
* train_model: {Inspiro, Ussr81, Alstom}
* train_id: Integer
* start_station: eg. line1["Kabaty"], line2["Uniwersytet"] etc.
* line_number: {1,2}
* direction: {"up", "down"}

Example trains.txt file:
"""
Inspiro, 1, Kabaty, 1, "up"
Ussr81, 2, Trocka, 2, "down"
"""

### Stations line1
* format : Station_name:$density
---
* density: {"low", "medium", "high", "very_high"

Example stations_1.txt:
```
Kabaty:low
Natolin:low
Imielin:low
Stokłosy:low
Ursynów:low
Służew:low
Wilanowska:low
Wierzbno:low
Racławicka:low
Pole Mokotowskie:low
Politechnika:low
Centrum:very_high
Świętokrzyska:medium
Ratusz Arsenał:low
Dworzec Gdański:low
Plac Wilsona:low
Marymont:low
Słodowiec:low
Stare Bielany:low
Wawrzyszew:low
Młociny:low
```

Example stations_2.txt:
```
Płocka:low
Rondo Daszyńskiego:low
Rondo ONZ:low
Świętokrzyska:medium
Uniwersytet:low
Centrum Nauki Kopernik:low
Stadion Narodowy:high
Dworzec Wileński:low
Szwedzka:low
Targówek:low
Trocka:low
```