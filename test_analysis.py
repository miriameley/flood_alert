import datetime
from floodsystem.analysis import polyfit
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import random 

def test_polyfit():
    """Tests the function polyfit used for 2F."""
    stations = build_station_list()
    update_water_levels(stations)
    dt=2
    station = stations[(random.randint(1, len(stations)))]          #gets a random station from the list of stations
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))            #gathers dates and levels for that station
    poly, d0 = polyfit(dates, levels, 3)                #forms the polynomial of best fit for the given data

    assert float('%.1g' % poly(0)) == float('%.1g' % station.latest_level)     #asserts that the result from the polynomial is equal to the relative water level at that time (to 1 sig fig) e.g. current time

def test_stations_level_over_threshold():
    """Tests the function stations_level_over_threshold used in 2B"""

    #creates a fake station with data
    s1 = "station id 1"
    m1 = "measure id 1"
    label1 = "station 1"
    coord1 = (1.0, 5.0)
    range1 = (-1, 1)
    river1 = "River 1"
    town1 = "Town 1"
    s_1 = MonitoringStation(s1, m1, label1, coord1, range1, river1, town1)

    #creates a second fake station with data
    s2 = "station id 2"
    m2 = "measure id 2"
    label2 = "station 2"
    coord2 = (-3.0, 2.0)
    range2 = (3, 7)
    river2 = "River 2"
    town2 = "Town 2"
    s_2 = MonitoringStation(s2, m2, label2, coord2, range2, river2, town2)

    #assigns latest water levels to each, one having a rel water level of 0 and the other of 0.8
    s_1.latest_level = 1
    s_2.latest_level = 6

    #puts these in a list
    stations = [s_1, s_2]

    #applies the function being tested to the stations with an expected output of just the second station
    x = stations_level_over_threshold(stations, 0.5)
    print(x)

    #asserts test to make sure only one station is returned by the function
    assert len(x) == 1

def test_stations_highest_rel_level():
    """Test for stations_highest_rel_function used in task 2C"""

    #create list of stations with the data updated
    stations = build_station_list()
    update_water_levels(stations)

    #spply the function to get the 7 stations with the highest water level
    x = stations_highest_rel_level(stations, 7)

    #assert a test that there are 7 stations in the return of the function
    assert len(x) == 7