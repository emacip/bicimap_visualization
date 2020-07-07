import json
import csv

if __name__ == "__main__":

    # read stations file

    locations = []

    with open('data/202006_stations.json') as f:
        for line in f:
            locations.append(json.loads(line))
            break

    row_list = [["id", "name", "latitude", "longitude", "activate"]]

    for location in locations:
        for station in location['stations']:
            row_list.append([station['id'], station['name'], station['latitude'], station['longitude'], station['activate']])

    print(row_list)
    with open('data/stations.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)


    # read movements file

    ranges = ["201907_movements","201908_movements","201909_movements","201910_movements","201911_movements",
             "201912_movements","202001_movements","202002_movements","202003_movements","202004_movements","202005_movements","202006_movements"]

    row_list = [["id", "user_type", "age_range", "unplug_hour_time","travel_time","zip_code", "unplug_station_id", "plug_station_id"]]

    for range in ranges:
        print(range)
        movements = []
        with open('data/'+range+'.json') as f:
            for line in f:
                movements.append(json.loads(line))

        for movement in movements:
            row_list.append([movement['_id']['$oid'], movement['user_type'], movement['ageRange'],
                             movement['unplug_hourTime'], movement['travel_time'], movement['zip_code'], movement['idunplug_station'], movement['idplug_station']])
            print("#")

    with open('data/movements.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
