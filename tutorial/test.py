import numpy as np
from MODULO.read_db import ReadData
from MODULO.modulo import MODULO
import os
import sys


def main():
    sys.path.append(os.getcwd())
    FOLDER = "./Ex_4_TR_PIV_Jet"
    # --- Component fields (N=2 for 2D velocity fields, N=1 for pressure fields)
    N = 2
    # --- Number of mesh points
    N_S = 6840
    # --- Header, footer to be skipped during acquisition
    H = 1
    F = 0
    # --- Read one sample snapshot (to get N_S)
    Name = "./Ex_4_TR_PIV_jet/Res00001.dat"
    Dat = np.genfromtxt(Name, skip_header=H, skip_footer=F)

    D = ReadData._from_dat(folder='./Ex_4_TR_PIV_jet/', filename='Res%05d', N=2, N_S=2 * Dat.shape[0],
                           h=H, f=F, c=1)

    # --- Initialize MODULO object
    m = MODULO(data=D,
               MEMORY_SAVING=True,
               N_PARTITIONS=11)
    # --- Check for D
    D = m._data_processing()
    Keep = np.array([1, 1, 1, 1])
    Nf = np.array([201, 201, 201, 201])
    # --- Test Case Data:
    # + Stand off distance nozzle to plate
    H = 4 / 1000
    # + Mean velocity of the jet at the outlet
    U0 = 6.5
    # + Input frequency splitting vector in dimensionless form (Strohual Number)
    ST_V = np.array([0.1, 0.2, 0.25, 0.4])
    # + Frequency Splitting Vector in Hz
    F_V = ST_V * U0 / H
    # + Size of the extension for the BC (Check Docs)
    Ex = 203  # This must be at least as Nf.
    dt = 1 / 2000
    boundaries = 'reflective'
    MODE = 'reduced'
    # K = np.load("./MODULO_tmp/correlation_matrix/k_matrix.npz")['K']
    Phis, Psis, Sigmas = m.compute_mPOD(Nf, Ex, F_V, Keep, boundaries, MODE, dt, False)

    return Phis, Psis, Sigmas


if __name__ == '__main__':
    _, _, _ = main()
