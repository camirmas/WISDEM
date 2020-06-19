# Imports and loading an airfoil
from wisdem.airfoilprep import Polar, Airfoil
import numpy as np

airfoil = Airfoil.initFromAerodynFile('../../wisdem/test/test_ccblade/5MW_AFFiles/DU21_A17.dat')
# ------

# first polar
Re = 7e6
alpha = [-14.50, -12.01, -11.00, -9.98, -8.12, -7.62, -7.11, -6.60, -6.50,
         -6.00, -5.50, -5.00, -4.50, -4.00, -3.50, -3.00, -2.50, -2.00, -1.50,
         -1.00, -0.50, 0.00, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00,
         4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 8.50, 9.00, 9.50,
         10.00, 10.50, 11.00, 11.50, 12.00, 12.50, 13.00, 13.50, 14.00, 14.50,
         15.00, 15.50, 16.00, 16.50, 17.00, 17.50, 18.00, 18.50, 19.00, 19.50,
         20.00, 20.50]
cl = [-1.050, -0.953, -0.900, -0.827, -0.536, -0.467, -0.393, -0.323, -0.311,
      -0.245, -0.178, -0.113, -0.048, 0.016, 0.080, 0.145, 0.208, 0.270, 0.333,
      0.396, 0.458, 0.521, 0.583, 0.645, 0.706, 0.768, 0.828, 0.888, 0.948,
      0.996, 1.046, 1.095, 1.145, 1.192, 1.239, 1.283, 1.324, 1.358, 1.385,
      1.403, 1.401, 1.358, 1.313, 1.287, 1.274, 1.272, 1.273, 1.273, 1.273,
      1.272, 1.273, 1.275, 1.281, 1.284, 1.296, 1.306, 1.308, 1.308, 1.308,
      1.308, 1.307, 1.311, 1.325]
cd = [0.0567, 0.0271, 0.0303, 0.0287, 0.0124, 0.0109, 0.0092, 0.0083, 0.0089,
      0.0082, 0.0074, 0.0069, 0.0065, 0.0063, 0.0061, 0.0058, 0.0057, 0.0057,
      0.0057, 0.0057, 0.0057, 0.0057, 0.0057, 0.0058, 0.0058, 0.0059, 0.0061,
      0.0063, 0.0066, 0.0071, 0.0079, 0.0090, 0.0103, 0.0113, 0.0122, 0.0131,
      0.0139, 0.0147, 0.0158, 0.0181, 0.0211, 0.0255, 0.0301, 0.0347, 0.0401,
      0.0468, 0.0545, 0.0633, 0.0722, 0.0806, 0.0900, 0.0987, 0.1075, 0.1170,
      0.1270, 0.1368, 0.1464, 0.1562, 0.1664, 0.1770, 0.1878, 0.1987, 0.2100]
cm = [-0.0378, -0.0349, -0.0361, -0.0464, -0.0821, -0.0924, -0.1015, -0.1073,
      -0.1083, -0.1112, -0.1146, -0.1172, -0.1194, -0.1213, -0.1232, -0.1252,
      -0.1268, -0.1282, -0.1297, -0.1310, -0.1324, -0.1337, -0.1350, -0.1363,
      -0.1374, -0.1385, -0.1395, -0.1403, -0.1406, -0.1398, -0.1390, -0.1378,
      -0.1369, -0.1353, -0.1338, -0.1317, -0.1291, -0.1249, -0.1213, -0.1177,
      -0.1142, -0.1103, -0.1066, -0.1032, -0.1002, -0.0971, -0.0940, -0.0909,
      -0.0883, -0.0865, -0.0854, -0.0849, -0.0847, -0.0850, -0.0858, -0.0869,
      -0.0883, -0.0901, -0.0922, -0.0949, -0.0980, -0.1017, -0.105]
         
p1 = Polar(Re, alpha, cl, cd, cm)

# second polar
Re = 9e6
alpha = [-14.24, -13.24, -12.22, -11.22, -10.19, -9.70, -9.18, -8.18, -7.19,
         -6.65, -6.13, -6.00, -5.50, -5.00, -4.50, -4.00, -3.50, -3.00, -2.50,
         -2.00, -1.50, -1.00, -0.50, 0.00, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00,
         3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50, 8.00, 9.00,
         9.50, 10.00, 10.50, 11.00, 11.50, 12.00, 12.50, 13.00, 13.50, 14.00,
         14.50, 15.00, 15.50, 16.00, 16.50, 17.00, 17.50, 18.00, 18.50, 19.00]
cl = [-1.229, -1.148, -1.052, -0.965, -0.867, -0.822, -0.769, -0.756, -0.690,
      -0.616, -0.542, -0.525, -0.451, -0.382, -0.314, -0.251, -0.189, -0.120,
      -0.051, 0.017, 0.085, 0.152, 0.219, 0.288, 0.354, 0.421, 0.487, 0.554,
      0.619, 0.685, 0.749, 0.815, 0.879, 0.944, 1.008, 1.072, 1.135, 1.197,
      1.256, 1.305, 1.390, 1.424, 1.458, 1.488, 1.512, 1.533, 1.549, 1.558,
      1.470, 1.398, 1.354, 1.336, 1.333, 1.326, 1.329, 1.326, 1.321, 1.331,
      1.333, 1.340, 1.362]
cd = [0.1461, 0.1263, 0.1051, 0.0886, 0.0740, 0.0684, 0.0605, 0.0270, 0.0180,
      0.0166, 0.0152, 0.0117, 0.0105, 0.0097, 0.0092, 0.0091, 0.0089, 0.0089,
      0.0088, 0.0088, 0.0088, 0.0088, 0.0088, 0.0087, 0.0087, 0.0088, 0.0089,
      0.0090, 0.0091, 0.0092, 0.0093, 0.0095, 0.0096, 0.0097, 0.0099, 0.0101,
      0.0103, 0.0107, 0.0112, 0.0125, 0.0155, 0.0171, 0.0192, 0.0219, 0.0255,
      0.0307, 0.0370, 0.0452, 0.0630, 0.0784, 0.0931, 0.1081, 0.1239, 0.1415,
      0.1592, 0.1743, 0.1903, 0.2044, 0.2186, 0.2324, 0.2455]
cm = [-0.0378, -0.0349, -0.0361, -0.0464, -0.0821, -0.0924, -0.1015, -0.1073,
      -0.1083, -0.1112, -0.1146, -0.1172, -0.1194, -0.1213, -0.1232, -0.1252,
      -0.1268, -0.1282, -0.1297, -0.1310, -0.1324, -0.1337, -0.1350, -0.1363,
      -0.1374, -0.1385, -0.1395, -0.1403, -0.1406, -0.1398, -0.1390, -0.1378,
      -0.1369, -0.1353, -0.1338, -0.1317, -0.1291, -0.1249, -0.1213, -0.1177,
      -0.1142, -0.1103, -0.1066, -0.1032, -0.1002, -0.0971, -0.0940, -0.0909,
      -0.0883, -0.0865, -0.0854, -0.0849, -0.0847, -0.0850, -0.0858, -0.0869,
      -0.0883, -0.0901, -0.0922, -0.0949, -0.0980]
      
p2 = Polar(Re, alpha, cl, cd, cm)

# create airfoil object (can contain as many polars as desired)
af = Airfoil([p1, p2])
# ------

# read in airfoils from AeroDyn files
airfoil1 = Airfoil.initFromAerodynFile('../../wisdem/test/test_ccblade/5MW_AFFiles/DU21_A17.dat')
airfoil2 = Airfoil.initFromAerodynFile('../../wisdem/test/test_ccblade/5MW_AFFiles/DU25_A17.dat')

# blend the two airfoils
airfoil_blend = airfoil1.blend(airfoil2, 0.3)
# ------

# apply 3D corrections as desired
r_over_R = 0.5
chord_over_r = 0.15
tsr = 5.0

# 3D stall correction
af3D_ex1 = af.correction3D(r_over_R, chord_over_r, tsr)

# a second example using the optional inputs
alpha_max_corr = 25  # apply full rotational correction only up to this angle of attack
alpha_linear_min = -3  # angle of attack to start evaluating slope of linear region
alpha_linear_max = 7  # angle of attack to stop evaluating slope of linear region

af3D_ex2 = af.correction3D(r_over_R, chord_over_r, tsr,
                           alpha_max_corr=alpha_max_corr,
                           alpha_linear_min=alpha_linear_min,
                           alpha_linear_max=alpha_linear_max)
# ------

# extend airfoil data to high angles of attack with 3D effects
cdmax = 1.3

# compute a 3D corrected and extended airfoil
af_extrap1 = af.extrapolate(cdmax)

# a second example using the optional inputs
AR = 17  # blade aspect ratio. If provided, cdmax is estimated using the aspect ratio.
cdmin = 0.001  # minimum drag coefficient.  Viterna's method can occasionally produce
               # negative drag coefficients.  A minimum is used to prevent unphysical data.
               # The passed in value is used to override the default.

af_extrap2 = af.extrapolate(cdmax, AR=AR, cdmin=cdmin)
# ------

# create new airfoil that uses the same angles of attack at each Reynolds number
af_common1 = af.interpToCommonAlpha()

# default approach uses a union of all defined angles of attack
# alternatively, specify the exact angles to use
alpha = np.arange(-180, 180)
af_common2 = af.interpToCommonAlpha(alpha)
# ------

# extract a data grid from airfoil
alpha, Re, cl, cd, cm = af.createDataGrid()

# cl[i, j] is the lift coefficient for alpha[i] and Re[j]

# write a new AeroDyn file
af.writeToAerodynFile('output.dat')
# ------
