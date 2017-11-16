# What is it?

Reformat shapefiles (.shp) to ASCII textfiles (.xyz) to be imported into MIKE. Tested with single feature files. It accepts all common shapefile types:

* Point: Must have a field called CON signfiying the connectivity. 1 is the node point, 0 is a vertex
* Line: Everything is connected. Taking the first element of a polyline as the node
* Polygon: Same as line


# Todo
Make it possible to convert multi-feature files.
