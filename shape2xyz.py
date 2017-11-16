#!/usr/bin/env python
# -*- coding: utf-8 -*-

from osgeo import gdal, ogr

def shp2xyz(shpin, xyz):
    '''
    collector of functions that reformats shapefiles (.shp) to .xyz files
    :param shpin: shapefile (point, line, or polygon)
    :param xyz: filename to store output
    :return: MIKE compatible .xyz formated shapefile
    '''
    shp_ds = ogr.Open(shpin)
    shp_lyr = shp_ds.GetLayer()

    # gets the shapefile type and applies the necessary function
    if shp_lyr.GetGeomType() == 1:
        print "Type: point"
        point2xyz(shpin, xyz)
    elif shp_lyr.GetGeomType() == 2:
        print "Type: polyline"
        line2xyz(shpin, xyz)
    elif shp_lyr.GetGeomType() == 3:
        print "Type: polygon"
        poly2xyz(shpin, xyz)


def point2xyz(shpin, xyz):
    '''
    reformat point-type .shp to .xyz
    :param shpin:
    :param xyz:
    :return:
    '''
    shp_ds = ogr.Open(shpin)
    shp_lyr = shp_ds.GetLayer()

    print 'found %d number of features!' % len(shp_lyr)

    fopen = open(xyz, 'a')

    for feat in shp_lyr:
        geom = feat.GetGeometryRef()
        print geom.GetGeometryType()

        connectivity = feat.GetFieldAsInteger('CON')
        print connectivity
        line = ''.join([str(geom.GetX()), ' ', str(geom.GetY()), ' ', str(connectivity), '\n'])
        fopen.write(line)

    fopen.close()

def line2xyz(shpin, xyz):
    '''
    reformat line-type .shp to .xyz
    :param shpin:
    :param xyz:
    :return:
    '''
    shp_ds = ogr.Open(shpin)
    shp_lyr = shp_ds.GetLayer()

    print 'found %d number of features!' % len(shp_lyr)

    first_line = True

    fopen = open(xyz, 'a')

    for feat in shp_lyr:
        geom = feat.GetGeometryRef()

        for i in range(0, geom.GetPointCount()):
            if first_line:
                line = ''.join([str(geom.GetPoint(i)[0]), ' ', str(geom.GetPoint(i)[1]), ' ', '1\n'])
                first_line = False
            else:
                line = ''.join([str(geom.GetPoint(i)[0]), ' ', str(geom.GetPoint(i)[1]), ' ', '0\n'])
            fopen.write(line)

    fopen.close()

def poly2xyz(shpin, xyz):
    '''
    reformat polygon-type .shp to .xyz
    :param shpin:
    :param xyz:
    :return:
    '''
    shp_ds = ogr.Open(shpin)
    shp_lyr = shp_ds.GetLayer()

    print 'found %d number of features!' % len(shp_lyr)

    first_line = True

    fopen = open(xyz, 'a')

    for feat in shp_lyr:
        geom = feat.GetGeometryRef()
        ring = geom.GetGeometryRef(0)
        for i in range(0, ring.GetPointCount()):
            if first_line:
                line = ''.join([str(ring.GetPoint(i)[0]), ' ', str(ring.GetPoint(i)[1]), ' ', '1\n'])
                first_line = False
            else:
                line = ''.join([str(ring.GetPoint(i)[0]), ' ', str(ring.GetPoint(i)[1]), ' ', '0\n'])
            fopen.write(line)
    fopen.close()



if __name__=='__main__':
    test_folder = './test/'

    shp_point = 'test_point.shp'
    shp_point_xyz = 'test_point.xyz'

    shp_line = 'test_line.shp'
    shp_line_xyz = 'test_line.xyz'

    shp_poly = 'test_poly.shp'
    shp_poly_xyz = 'test_poly.xyz'

    #point2xyz(test_folder + shp_point, test_folder + shp_point_xyz)
    #line2xyz(test_folder + shp_line, test_folder + shp_line_xyz)
    #poly2xyz(test_folder + shp_poly, test_folder + shp_poly_xyz)
    shp2xyz(test_folder + shp_poly, test_folder + shp_poly_xyz)