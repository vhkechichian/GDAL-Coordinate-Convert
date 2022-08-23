# -*- coding: utf-8 -*-
# -------------------------------------------------------
# __author__ = 'Ishafizan'
# date: 23/Aug/2022
# -------------------------------------------------------

from osgeo import gdal
import shutil


# ---------------------------------------
# PARALLEL processing manipulations
# -------------------------------------

# ---------------------------------------
# file manipulations
# -------------------------------------
def zipit(dst, dst_dir):
    shutil.make_archive(dst, 'zip', dst_dir)


# ---------------------------------------
# coordinate manipulations
# ---------------------------------------
def geojson2geojson(trans_format, infile, outfile, espg_src, espg_dst):
    options = gdal.VectorTranslateOptions(format=trans_format, srcSRS=espg_src,
                                          dstSRS=espg_dst, reproject=True)
    gdal.VectorTranslate(outfile, infile, options=options)


def geojson2shp(trans_format, infile, outfile, espg_src, espg_dst):
    # (format="GeoJSON", srcSRS="EPSG:900913", dstSRS="EPSG:4326", reproject=True, )
    options = gdal.VectorTranslateOptions(format=trans_format, srcSRS=espg_src,
                                          dstSRS=espg_dst, reproject=True)
    gdal.VectorTranslate(outfile, infile, options=options)

# ---------------------------------------
# TEXT manipulations
# ---------------------------------------

# ---------------------------------------
# TIME manipulations
# ---------------------------------------
