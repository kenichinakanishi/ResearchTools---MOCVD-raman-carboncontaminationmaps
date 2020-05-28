import os
from analysis import *

folder = os.getcwd() + r'\Raman Data'
file = r'dms0_05mbar_map.txt'
fn = os.path.join(folder, file)
print(fn)
spectra = spline_WS2map_analysis(fn)
# print(list((spectra[0].keys())))

plot_map(spectra, 'WS1_height', show=True)
plot_map(spectra, 'WS2_height', show=True)
plot_map(spectra, 'D_height', show=True)
plot_map(spectra, 'G_height', show=True)
