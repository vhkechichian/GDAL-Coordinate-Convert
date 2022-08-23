# -*- coding: utf-8 -*-
import logging
import os.path
import sys


# -------------------------------------------------------
# __author__ = 'Ishafizan'
# date: 22/May/2020
# -------------------------------------------------------


# init logger
def logger():
    """
    Function returns logger instance
    :return: log
    :rtype: object
    """
    program = os.path.basename(sys.argv[0])
    log = logging.getLogger(program)
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.basicConfig(format='%(asctime)s : [%(filename)s:%(lineno)d] : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    log.info("running %s" % ' '.join(sys.argv))

    # add to file
    fh = logging.FileHandler("log/{0}.log".format(program.split(".")[0]))
    fh.setLevel(logging.DEBUG)
    fh_format = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname)-8s - %(message)s')
    fh.setFormatter(fh_format)
    log.addHandler(fh)
    return log
