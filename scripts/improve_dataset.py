 # -*- coding: UTF-8 -*-

import csv
import json
import datetime
import random
import shapefile
from shapely.geometry import shape, Point

def check(lon,lat):
    # read your shapefile
    r = shapefile.Reader("../data/limadmin-shp/LIMADMIN.shp")
    shapes = r.shapes()

    tmp = r.fields[3]

    print(r.fields[3][3])
    
    nbr = len(shapes)
    
    point = Point(lon,lat)

    for i in (0,nbr-1):
        polygon = shape(shapes[i])

        if( polygon.contains(point)):
            return shapes[i]["CODEID"]

    return 0

output = open('../data/improved_spvm_2015-2019.csv','w', encoding="utf8" )
headers = [ 'CATEGORIE', 'JOUR', 'QUART', 'PDQ','LAT','LONG','PLACE_ID' ]

writer = csv.DictWriter(output, fieldnames=headers)
writer.writeheader()

with open('../data/limadmin.json', encoding="ISO-8859-1") as f:
    js = json.load(f)

print("*** Debut du preprocess ***")

with open("../data/crimes_mtl_2015_2019.csv",encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        quart = row['QUART']
        div = row['PDQ']
        lat_ = row['LATITUDE']
        long_ = row['LONGITUDE']

        point = Point(float(long_),float(lat_))

        res = 0

        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                #print('Found containing polygon:', feature['properties']['CODEID'])
                res = int(feature['properties']['CODEID'])

        writer.writerow({ 'CATEGORIE':row['CATEGORIE'], 'JOUR':row['DATE'], 'QUART':quart, 'PDQ' : div, 'LAT':lat_, 'LONG':long_, 'PLACE_ID':res})


output.close()
