#!/usr/bin/env python
# -*- coding: utf-8 -*-

from osgeo import gdal, ogr

def shape_type(shpin, xyz):
    shp_ds = ogr.Open(shpin)
    shp_lyr = shp_ds.GetLayer()
    print shp_lyr.GetExtent()

    if shp_lyr.GetGeomType() == 1:
        print "Point type"
    elif shp_lyr.GetGeomType() == 2:
        print "Line type"
    elif shp_lyr.GetGeomType() == 3:
        print "Poly type"

    print 'found %d number of features!' % len(shp_lyr)

    fopen = open(xyz, 'a')

    for feat in shp_lyr:
        geom = feat.GetGeometryRef()
        print geom.GetGeometryType()
        line = ''.join([str(geom.GetX()), ' ', str(geom.GetY()), ' ', '0', '\n'])
        print line
        fopen.write(line)

    fopen.close()

def point2xyz(shpin, xyz):
    shp_ds = ogr.Open(shpin)
    shp_lyr = shp_ds.GetLayer()
    print shp_lyr.GetExtent()

    if shp_lyr.GetGeomType() == 1:
        print "Point type"
    elif shp_lyr.GetGeomType() == 2:
        print "Line type"
    elif shp_lyr.GetGeomType() == 3:
        print "Poly type"

    print 'found %d number of features!' % len(shp_lyr)

    fopen = open(xyz, 'a')

    for feat in shp_lyr:
        geom = feat.GetGeometryRef()
        print geom.GetGeometryType()

        connectivity = feat.GetFieldAsInteger('CON')
        print connectivity
        line = ''.join([str(geom.GetX()), ' ', str(geom.GetY()), ' ', str(connectivity), '\n'])
        print line
        fopen.write(line)

    fopen.close()

def poly2xyz(shpin, xyz):
    shp_ds = ogr.Open(shpin)
    shp_lyr = shp_ds.GetLayer()
    print shp_lyr.GetExtent()

    print 'found %d number of features!' % len(shp_lyr)

    first_line = True

    fopen = open(xyz, 'a')

    for feat in shp_lyr:
        geom = feat.GetGeometryRef()
        print '%d in geometry' % geom.GetPointCount()
        print geom.next()
        #fopen.write(line)
    fopen.close()

def shp2xyz(shp1, shp2):
    pass



if __name__=='__main__':
    test_folder = './test/'

    shp_point = 'test_point.shp'
    shp_point_xyz = 'test_point.xyz'

    shp_line = 'test_line.shp'
    shp_line_xyz = 'test_line.xyz'

    shp_poly = 'test_poly.shp'
    shp_poly_xyz = 'test_poly.xyz'

    #point2xyz(test_folder + shp_point, test_folder + shp_point_xyz)
    poly2xyz(test_folder + shp_poly, test_folder + shp_poly_xyz)
    #shape_type(test_folder + line)
    #shape_type(test_folder + poly)