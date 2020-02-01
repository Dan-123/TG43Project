import pandas as pd
import numpy as np
from scipy import interpolate


class DoseRefPoint:
    """
    Class that contains information for a single dose reference point
    """

    def __init__(self, x, y, z):
        """
        Constructor fo the DoseRefPoint class
        :param x: x position of the dose reference point (in cm)
        :param y: y position of the dose reference point (in cm)
        :param z: z position of the dose reference point (in cm)
        """
        self.x = x
        self.y = y
        self.z = z
        self.cartesian = [x, y, z]

    def computeDose(self, source_list, time):
        """
        Method to compute dose from a list of sources at this point
        :param source_list: A list of Source() objects
        :param time: Time of irradiation in minutes
        :return: A list of dose values for given sources after given time
        """
        doselist = []  # Initialize list to contain dose values
        time = time / 60  # Convert from minutes to hours
        for source in source_list:  # Iterate through a list of len(source_list) sources
            xdist = np.abs(source.x - self.x)  # Compute x, y, z distance from reference point to source
            ydist = np.abs(source.y - self.y)
            zdist = np.abs(source.z - self.z)
            r, phi, theta = cartesian2Polar(xdist,  # Call cartesian2polar to convert to polar
                                            ydist,
                                            zdist)

            L = source.data.getActiveLength()  # Source active length
            G = computeRadialDose(r, theta, L)  # Radial dose factor
            G_0 = computeRadialDose(1, np.deg2rad(90), L)  # Normalized radial dose factor

            # Calculate dose rate
            DoseRate = source.aks \
                       * source.data.getDoseRateConst() \
                       * (G / G_0) * source.data.getRadialDoseConst(r) \
                       * source.data.getAnisotropyConst(r, np.rad2deg(theta)) \
                       * (1 / .0001)
            Dose = DoseRate * time  # Dose in cGy
            doselist.append(float(Dose))  # Append dose to doselist
        return doselist


class DataTable:
    """Class used to hold data from .xls files
    """
    def __init__(self, loc):
        """
        Constructor for DataTable class
        :param loc: path to .xls file
        """
        self.loc = loc
        self.sheet = pd.read_excel(loc, header=None)

    def getActiveLength(self):
        """
        Gets source's active length
        :return: Active length of source
        """
        return self.sheet[2][9]

    def getDoseRateConst(self):
        """
        Gets source's dose rate constant
        :return: Dose rate constant
        """
        return self.sheet[2][4]

    def getRadialDoseConst(self, r):
        """
        Gets source's radial dose constant
        :param r: Distance from source (in cm)
        :return: Radial dose constant at distance 'r'
        """
        table = pd.read_excel(self.loc,
                              skiprows=10,
                              nrows=13,
                              usecols="B:C",
                              index_col=0)
        return np.interp(r, table.index, table.values.flatten())

    def getAnisotropyConst(self, r, theta):
        """
        Gets anisotropy constant at distance 'r' and angle 'theta'
        :param r: Distance from source (in cm)
        :param theta: Angle from source's transverse plane (in radians)
        :return: Anisotrpy constant at distance 'r' and angle 'theta'
        """
        table = pd.read_excel(self.loc,
                              skiprows=10,
                              nrows=48,
                              usecols="E:O",
                              index_col=0)
        r_vals = table.columns
        theta_vals = table.index
        F_vals = table.to_numpy()
        f = interpolate.interp2d(r_vals, theta_vals, F_vals)  # 2D interpolate f(r, theta)
        return f(r, theta)

    def getAlongAwayConst(self, along, away):
        """
        TODO Gets along and away constant
        :param along:
        :param away:
        :return:
        """
        pd.read_excel(self.loc,
                      skiprows=10,
                      nrows=19,
                      usecols="Q:AC",
                      index_col=0)


class Source:
    """
    Class used to store data pertaining to specific brachytherapy source
    """
    _numofsources = 0 # Number of sources counter

    def __init__(self, x, y, z, activity):
        """
        Constructor for the Source class
        :param x: x position of source (in cm)
        :param y: y position of source (in cm)
        :param z: z position of source (in cm)
        :param activity: Activity of source (in Ci)
        """
        self.x = x
        self.y = y
        self.z = z
        self.coordinates = [x, y, z]
        self.activity = activity                         # source activity in Ci
        self.type = 'IR-192'                             # source type
        self.aks = ((activity * 1000) / 0.243) * 0.0001  # Air Kerma strength

        # May want to change for various sources
        self.data = DataTable('192ir-hdr-flexisource.xls')

        Source._numofsources += 1

    @property
    def numofsources(self):
        return self._numofsources


def cartesian2Polar(x, y, z, in_degrees=False):
    """
    Helper function to convert from cartesian to polar coordinates
    :param x: x position
    :param y: y position
    :param z: z position
    :param in_degrees: False for return type in radians, True for degrees
    :return: List of polar coordinates transformation of input [r, phi, theta]
    """
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = np.arctan2(y, x)
    phi = np.arccos(z / r)
    if in_degrees:
        r = np.rad2deg(r)
        phi = np.rad2deg(phi)
        theta = np.rad2deg(theta)
    return [r, phi, theta]


def computeRadialDose(r, theta, L):
    """
    Helper function to compute the radial dose function
    :param r: Radial distance from source (in cm)
    :param theta: Angle from transverse plane of source (in radians)
    :param L: Length of active source length (in cm)
    :return: Radial dose factor
    """
    beta = np.arcsin((L * np.sin(np.arctan2((r * np.sin(theta)), (r * np.cos(theta) - (L / 2))))) / (
        np.sqrt((r * np.sin(theta)) ** 2 + ((L / 2) + r * np.cos(theta)) ** 2)))
    beta = np.rad2deg(beta)
    if theta != 0:
        G = beta / (L * r * np.sin(theta))
    else:
        G = 1 / (r ** 2 - (L ** 2 / 4))
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
        print(f'Total Dose: {results[1][i]:.2f} cGy')

    # print(runTest())
    print(f'Num of sources: {Source._numofsources}')


if __name__ == "__main__":
    main()
