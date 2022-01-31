"""Unit test for the  geo.py module"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    p = (52.188229, 0.102169)
    stations = build_station_list()
    sorted_distance_list = stations_by_distance(stations, p)
    assert len(sorted_distance_list) == 2165  #number of measuring stations it should return

    sorted_distance_list = stations_by_distance(stations, p)
    assert sorted_distance_list[0][0] == 'Bin Brook'