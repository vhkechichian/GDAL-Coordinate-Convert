# -*- coding: utf-8 -*-
# -------------------------------------------------------
# __author__ = 'Ishafizan'
# date: 23/Aug/2022
# -------------------------------------------------------
"""
setup
https://medium.com/@egiron/how-to-install-gdal-and-qgis-on-macos-catalina-ca690dca4f91
https://sandbox.idre.ucla.edu/sandbox/general/how-to-install-and-run-gdal
https://pcjericks.github.io/py-gdalogr-cookbook/
https://gist.github.com/kelvinn/f14f0fc24445a7994368f984c3e37724

conversion from EPSG:900913 coordinates to EPSG:4326 format(meters to latlongs)
- test the new geojson with https://geojsonviewer.nsspot.net/
- test shape files on
- https://mapshaper.org/ (add satellite basemap)
- https://maps.equatorstudios.com/tab/Search
"""
import os

# --------------------------------------------
# DIRECTORIES
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
GEOJSON_SRC = "data/geojson_iplan"
GEOJSON_NEW = "data/geojson_new"
SHAPEFILE_DIR = "data/shapefile"
