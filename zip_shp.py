# -*- coding: utf-8 -*-
# -------------------------------------------------------
# __author__ = 'Ishafizan'
# date: 23/Aug/2022
# zip shapefiles in directory
# -------------------------------------------------------

import os
import sys
import settings
from datetime import datetime

try:
    sys.path.append(settings.BASE_DIR)
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

    name = item.split(".")[0]
    log.info("%s) %s" % (no, name))
    outfile = "%s/%s" % (settings.SHAPEFILE_DIR, name)

    # -------------------------
    # zipping files in diectory
    try:
        util_gen.zipit("%s" % outfile, "%s/%s" % (settings.SHAPEFILE_DIR, name))
    except Exception as e:
        log.error(e)
        exit()
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
