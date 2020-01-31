# from kivy.app import App
# from kivy.uix.button import Button
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
# class TestApp(App):
#     def build(self):
#         return Button(text='Hello World')

class DoseRefPoint:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.cartesian = [x, y, z]


    def computeDose(self, source_list, time):
        """Method to compute dose from a list of sources at this point"""
        time = time/60
        for source in source_list:
            xdist = np.abs(source.x - self.x)
            ydist = np.abs(source.y - self.y)
            zdist = np.abs(source.z - self.z)
            r, phi, theta = cartesian2Polar(xdist, ydist, zdist)

            L = source.data.getActiveLength()
            G = computeRadialDose(r, theta, L)
            G_0 = computeRadialDose(1, np.deg2rad(90), L)

            DoseRate = source.aks * source.data.getDoseRateConst() * (G/G_0) * source.data.getRadialDoseConst(r) * source.data.getAnisotropyConst(r, np.rad2deg(theta)) *(1/.0001)
            Dose = DoseRate * time # Dose in cGy
            return Dose
class DataTable:
    """Class used to hold Data from .xls files"""
    def __init__(self, loc):
        self.loc = loc
        self.sheet = pd.read_excel(loc, header=None)

    def getActiveLength(self):
        return self.sheet[2][9]

    def getDoseRateConst(self):
        return self.sheet[2][4]

    def getRadialDoseConst(self, r):
        table = pd.read_excel(self.loc, skiprows=10, nrows=13, usecols="B:C", index_col=0)
        return np.interp(r, table.index, table.values.flatten())

    def getAnisotropyConst(self, r, theta):
        table = pd.read_excel(self.loc, skiprows=10, nrows=48, usecols="E:O", index_col=0)
        r_vals = table.columns
        theta_vals = table.index
        F_vals = table.to_numpy()
        f = interpolate.interp2d(r_vals, theta_vals, F_vals)  # 2D interpolate f(r, theta)
        return f(r, theta)

    def getAlongAwayConst(self, along, away):
        pd.read_excel(self.loc, skiprows=10, nrows=19, usecols="Q:AC", index_col=0)


class Source:
    _numofsources = 0

    def __init__(self, x, y, z, activity):
        self.x = x
        self.y = y
        self.z = z
        self.coordinates = [x, y, z]
        self.activity = activity # source activity in Ci
        self.type = 'IR-192' # source type
        self.aks = ((activity * 1000) / 0.243) * 0.0001 # Air Kerma strength

        # May want to change for various sources
        self.data = DataTable('192ir-hdr-flexisource.xls')

        Source._numofsources += 1

def cartesian2Polar(x, y, z, in_degrees=False):
    """Converts from cartesian to Polar"""
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(y, x)
    phi = np.arccos(z/r)
    if in_degrees:
        r = np.rad2deg(r)
        phi = np.rad2deg(phi)
        theta = np.rad2deg(theta)
    return [r, phi, theta]

def computeRadialDose(r, theta, L):
    beta = np.arcsin((L * np.sin(np.arctan2((r * np.sin(theta)) , (r * np.cos(theta) - (L / 2))))) / (
        np.sqrt((r * np.sin(theta)) ** 2 + ((L / 2) + r * np.cos(theta)) ** 2)))
    beta = np.rad2deg(beta)
    if not theta == 0:
        G = beta/(L * r * np.sin(theta))
    else:
        G = 1/(r**2 - (L**2/4))
    return G

def computeDose(source, dosepoint, treatment_time):

    # Convert dosepoint to polar coordinates
    x = dosepoint[0] - source.position[0] # dosepoint position relative to source
    y = dosepoint[1] - source.position[1] # dosepoint position relatove to source
    r = np.sqrt(x**2 + y**2) # dist in cm
    theta = (np.arctan(y/x)) # angle in degrees
    # theta = np.arctan2(y, x)
    # theta = np.rad2deg(theta)
    source.readAttributes()

    L = source.activeLength

    # L = .36 # Set to example active length (for testing)

    beta = np.arcsin( (L * np.sin( np.arctan((r*np.sin(theta))/(r*np.cos(theta) - (L/2)))))/ (np.sqrt((r*np.sin(theta))**2 + ((L/2)+r*np.cos(theta))**2)) )
    beta = np.rad2deg(beta)

    # what if y = 0?
    G_L = beta/(L*r)

    G_L_0 = (2 * np.rad2deg(np.arctan(L/2)))/(L)

    normalized_G_L = G_L / G_L_0

    g_l = np.interp(r, source.g_l_np[:,0], source.g_l_np[:,1]) # Interpolate g_l for given r

    F = source.f(r, np.rad2deg(theta))

    DoseRate = source.aks * source.DR_Const * normalized_G_L * g_l * F /.0001 # Doserate in cGy/hr

    treatment_time_hours = treatment_time/60

    Dose = DoseRate * treatment_time_hours # Dose in cGy

    return Dose

def main():

    # loc = '192ir-hdr-flexisource.xls'
    # a = DataTable(loc)
    # print(a.getAnisotropyConst(10, 10))
    # print(a.getActiveLength())
    # print(a.getRadialDoseConst(9))
    #
    # print(cartesian2Polar(1, 2, 0, in_degrees=True))
    a = DoseRefPoint(3.1, 2.6, 0)
    list = []
    list.append(Source(0, 0, 0, 10))
    b = a.computeDose(list, 10)
    print(b)


if __name__ == "__main__":
    main()