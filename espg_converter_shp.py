# -*- coding: utf-8 -*-
# -------------------------------------------------------
# __author__ = 'Ishafizan'
# date: 23/Aug/2022
# converts coords from iplan geojson to proper lat, longs in esri shapefile
# conversion from EPSG:900913 coordinates to EPSG:4326 format
# -------------------------------------------------------
"""
- read from folder data/geojson_iplan
- convert geojson to shape file
- note:
    - limitation of 10 char in field descriptions. shapefile issue
    - cannot immediately zip, as files need to be created first.
"""
import os
import sys
import settings
from datetime import datetime
import shutil

try:
    sys.path.append(settings.BASE_DIR)
    from osgeo import gdal

    from utils import util_gen, util_log

    # -------------------------
    # instantiate logger
    log = util_log.logger()
except ImportError as err:
    print(err)
    raise Exception("import util files failed")

# ----------------------------------------------------
# initial settings
# ----------------------------------------------------
start_all = datetime.now()
print("#" * 50)
print("START")
print("#" * 50)

# -------------------------
# read from src directory
log.info("reading from src: %s" % settings.GEOJSON_SRC)
dir_path = r'%s' % settings.GEOJSON_SRC

file_list = os.listdir(dir_path)
log.info("no of files: %s" % len(file_list))
# log.info(file_list)

# -------------------------
# loop through each file

no = 1  # counter
for item in file_list:

    log.info("%s) %s" % (no, item))
    name = item.split(".")[0]

    infile = "%s/%s" % (settings.GEOJSON_SRC, item)
    outfile = "%s/%s" % (settings.SHAPEFILE_DIR, name)

    # -------------------------
    # transformation
    try:

        # -------------------------
        # call function to transform files
        util_gen.geojson2shp("ESRI Shapefile", infile, outfile, "EPSG:900913", "EPSG:4326")
    except Exception as e:
        log.error(e)
        exit()
    """
    # -------------------------
    # zipping files in diectory
    try:
        util_gen.zipit("%s" % outfile, 'zip', settings.SHAPEFILE_DIR)
        # shutil.make_archive("%s" % outfile, 'zip', settings.SHAPEFILE_DIR)
    except Exception as e:
        log.error(e)
        exit()
    """
    no += 1  # increase counter
# ----------------------------------------------------
# FINISH
# ----------------------------------------------------
end_all = datetime.now()
elapsed_time_all = end_all - start_all

print("#" * 50)
print("FINISH")
print("#" * 50)
# print("line count: %s" % line_count)
log.info('overall execution time -> %s%s' % (elapsed_time_all.total_seconds(), 's'))

