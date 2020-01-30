# from kivy.app import App
# from kivy.uix.button import Button
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
# class TestApp(App):
#     def build(self):
#         return Button(text='Hello World')

class Source:
    _numofsources = 0

    def __init__(self, position, activity):
        self.position = position # source [x, y] position
        self.activity = activity # source activity in Ci
        self.type = 'IR-192' # source type
        self.aks = ((activity * 1000) / 0.243) * 0.0001 # Air Kerma strength

        Source._numofsources += 1

    def readAttributes(self):

        loc = '192ir-hdr-flexisource.xls'

        WS = pd.read_excel(loc, header=None)
        WS_np = np.array(WS)

        self.DR_Const = WS_np[4, 2]
        self.g_l = pd.read_excel(loc, skiprows=10, nrows=13, usecols="B:C", index_col=0)
        self.g_l_np = np.array(WS_np[11:24, 1:3], dtype='f')
        self.activeLength = WS_np[9, 2]
        self.F = pd.read_excel(loc, skiprows=10, nrows=48, usecols="E:O", index_col=0)
        # self.F_np[0,0] = 0
        # self.F_np = self.F_np.astype(float)
        r = self.F.columns
        theta = self.F.index
        F_vals = self.F.to_numpy()
        self.f = interpolate.interp2d(r, theta, F_vals) # 2D interpolate f(r, theta)
        self.along_away = pd.read_excel(loc, skiprows=10, nrows=19, usecols="Q:AC", index_col=0)

    def computeDose(self, dosepoint):
        """ Computes dose at a reference point dosepoint = [x,y] due to this source"""
        # Convert dosepoint to polar coordinates
        x = dosepoint[0] - self.position[0] # dosepoint position relative to source
        y = dosepoint[1] - self.position[1] # dosepoint position relatove to source
        r = np.sqrt(x**2 + y**2) # dist in cm
        theta = np.rad2deg(np.arctan(y/x)) # angle in degrees

        # Compute beta
        # beta = np.arcsin( (self.L * np.sin(np.arctan())) / () )

def computeDose(source, dosepoint, treatment_time):

    # Convert dosepoint to polar coordinates
    x = dosepoint[0] - source.position[0] # dosepoint position relative to source
    y = dosepoint[1] - source.position[1] # dosepoint position relatove to source
    r = np.sqrt(x**2 + y**2) # dist in cm
    theta = (np.arctan(y/x)) # angle in degrees
    source.readAttributes()

    # TODO uncomment line before submitting
    # L = source.activeLength

    # TODO cancel this line before submitting
    L = .36 # Set to example active length (for testing)

    beta = np.arcsin( (L * np.sin( np.arctan((r*np.sin(theta))/(r*np.cos(theta) - (L/2)))))/ (np.sqrt((r*np.sin(theta))**2 + ((L/2)+r*np.cos(theta))**2)) )
    beta = np.rad2deg(beta)

    G_L = beta/(L*y)

    G_L_0 = (2 * np.rad2deg(np.arctan(L/2)))/(L)

    normalized_G_L = G_L / G_L_0
    aks = source.aks
    DR_const = source.DR_Const

    g_l = np.interp(r, source.g_l_np[:,0], source.g_l_np[:,1]) # Interpolate g_l for given r

    F = source.f(r, np.rad2deg(theta))

    DoseRate = source.aks * source.DR_Const * normalized_G_L * g_l * F /.0001 # Doserate in cGy/hr

    treatment_time_hours = treatment_time/60

    Dose = DoseRate * treatment_time_hours # Dose in cGy

    return Dose

def readFile():

    loc = '192ir-hdr-flexisource.xls'


    WS = pd.read_excel(loc, header=None)
    WS_np = np.array(WS)

    DR_Const = WS_np[4, 2]
    g_l = pd.read_excel(loc, skiprows=10, nrows=13, usecols="B:C", index_col=0)
    L = WS_np[9, 2]
    F = pd.read_excel(loc, skiprows=10, nrows=48, usecols="E:O", index_col=0)
    along_away = pd.read_excel(loc, skiprows=10, nrows=19, usecols="Q:AC", index_col=0)
    return DR_Const, g_l, L, F, along_away


def main():
    source1 = Source([0, 0], 10)
    source2 = Source([1, 1], 10)
    sourcelist = []
    doselist = []
    sourcelist.append(source1)
    sourcelist.append(source2)
    doselist.append(computeDose(source1, [3.1, 2.6], 10))
    doselist.append(computeDose(source2, [3.1, 2.6], 10))

    print(doselist)

    # source1.readAttributes()
    # source2.readAttributes()
    #
    # source1.computeDose([3.1, 2.6])
    # params = readFile()
    # print(params)
if __name__ == "__main__":
    main()