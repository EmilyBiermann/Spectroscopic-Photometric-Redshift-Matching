"""
Emily Biermann
Get col info for asctoldac config file
6/18/19
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy import stats
from scipy.stats import norm

magZpt = 27.0

pwd = '/home/ebiermann/cat/MACS0454_Astrometry/scamp/'
fname = 'crawford_spec_SCAMP_ref13.fits'

hdul = fits.open(pwd+fname)
data = hdul[1].data

cols=hdul[1].columns

hdul.close()
