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
        doselist = []
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
            doselist.append(float(Dose))
        return doselist

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


def runExample():

    a = DoseRefPoint(-2.0, 0, 0)
    b = DoseRefPoint(1.5, 0, 0)
    c = DoseRefPoint(1.5, 3, 0)
    d = DoseRefPoint(1.5, -4, 0)
    e = DoseRefPoint(4, 0, 0)
    list = []
    list.append(Source(0, 0, 0, 10))
    list.append(Source(0, 2, 0, 10))
    list.append(Source(0, -2, 0, 10))
    list.append(Source(3, 1, 0, 10))
    list.append(Source(3, -1, 0, 10))


    dose_a = a.computeDose(list, 10)
    dose_b = b.computeDose(list, 10)
    dose_c = c.computeDose(list, 10)
    dose_d = d.computeDose(list, 10)
    dose_e = e.computeDose(list, 10)

    dose_list = [dose_a, dose_b, dose_c, dose_d, dose_e]
    sum_dose_list = [np.sum(dose_a), np.sum(dose_b), np.sum(dose_c), np.sum(dose_d), np.sum(dose_e)]


    return dose_list, sum_dose_list

def runTest():

    a = DoseRefPoint(3.1, 2.6, 0)
    sourcelist = [Source(0, 0, 0, 10)]
    return a.computeDose(sourcelist, 10)

def main():
    results = runExample()
    for i in range(len(results[1])):
        print("Total Dose: {:.2f} cGy".format(results[1][i]))

    # print(runTest())
    print("Num of sources: {}".format(Source._numofsources))

if __name__ == "__main__":
    main()