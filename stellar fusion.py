# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:03:11 2022

@author: ackut
"""
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
from IPython.display import Image
import pandas as pd

pMass = 1.6726219236951*10**(-27) # mass of proton #kg

atomicMassUnit = 1.66054*10**(-27) # kg
pMassInAMU = pMass/atomicMassUnit #proton mass in atomic units

print(f"Proton's mass in atomic mass units: {pMassInAMU} u")
c = 299792458 # speed of light in m/s
pEnergy= pMass*c**2 #rest energy of proton
print(f"Proton's rest energy {pEnergy} J")

eV = 1.602176634*10**(-19) # J

pEnergyeV= pEnergy/eV #proton energy in eV
print(f"Proton's rest energy: {pEnergyeV/1000000} MeV")

pM = 1.00727646662153 # proton mass in u

#Calculate the Protons rest energy again but this time use atomic mass units. Give the answer in MeV

utoE = 931.4941024228 # MeV/c^2
pE = pM*utoE
print(f"Proton's rest energy: {pE} MeV")

eMass= 9.109383701528*10**(-31)/atomicMassUnit #electron mass in atomic mass units
eE= eMass*utoE 
print(f"Electron's rest energy is {eE} MeV")

nMass= 1.6749274980495*10**(-27)/atomicMassUnit #neutron mass in atomic mass units
nE= nMass*utoE
print(f"Neutron's rest energy is {nE} MeV") #neutron's rest energy calculation

"""----------------------------------------"""

#The mass excess of hydrogen is calculated by DeltaM= m - A 

deltaM_H= 1.0078250321-1

print(f"Mass excess for 1H atom: {deltaM_H} u")
print(f"Mass excess for 1H atom in keV : {deltaM_H*utoE*1e3} keV")


"""----------------------------------------"""

#Getting the excess for the nucleus mass excess is much more complicated and requires us to subtract the binding 
#energies. ( m_nucleus = m - Z*m_e + B_e ) (B_e: Binding energy of electron 13.6eV for hydrogen.)

#The mass defect is the difference between the actual mass and the mass number. 
# Delta m = m_a - Z(m_p + m_e) - (A-Z)*m_n

deltaM_defect_He= 4.002603 -2*(pM+eMass) - (4-2)*nMass
print(f"Mass defect for the 4He Atom: {deltaM_defect_He} u ")


#nuclear binding energy is the energy needed the break the nucleus into protons and neutrons
#electron binding energy is the energy needed to break the electrons free from the atom. {Ionisation Energy}

#since fusion deals with nuclei we will only consider the nuclear binding energy which is commonly expressed as binding
#energy per nucleon in keV or MeV (nucleon being a proton or neutron).

#because the electrons and their binding energies are so small we can assume the atomic values for mass excess
#defect etc are the same as the values for the nucleus.
#If we wanted the nuclear binding energy we would first need to calculate the mass of the nucleus, m_nucleus.


BE_He= abs(deltaM_defect_He*utoE)
print(f"Binding energy for 4He nucleus: {BE_He} MeV")
print(f"Binding energy per Nucleon for 4He Nucleus: {BE_He/4} MeV")

df= pd.read_csv("mass16abundant.csv",delimiter=";")
print(df.head())

fig= plt.figure(1) 
#add axis labels to this graph!

plt.xlabel("Z")
plt.ylabel("B/A (keV/nucleon)")

plt.scatter(df["Z"], df["BINDING ENERGY (keV)"], marker='o', alpha=0.75)


"""-------------------------------------------------------------------"""

me= 511 #keV 

Q= 4*df["MASS EXCESS (keV)"][0] - df["MASS EXCESS (keV)"][1] - 4*me #Q value for reaction
#if energy is released Q>0 , if energy is used Q<0
Q /= 1000
print(f"Q = {round(Q,3)} MeV") #that's a lot of energy per reaction!

#If the two positrons annihilate with two electrons in the plasma (which they most likely will) then an extra 4me of energy
#is produced. Calculate the new Q values taking this into account

Q= 4*df["MASS EXCESS (keV)"][0] - df["MASS EXCESS (keV)"][1]
Q /= 1000
print(f"Q= {round(Q,3)} MeV")

#We can use this fact to estimate how long the Sun can shine by fusing Hydrogen only. We have to assume that
### The Sun was initially 100% Hydrogen & The sun can only convert the inner 10% to Helium
#This means only 0.007* 0.1* M_sun is converted to energy. 

mSun= 1.989e30 #kg
Enuclear= 0.007*(0.1*mSun)*c**2 #J
print(f"Total energy from fusing Hydrogen in the Sun = {Enuclear:.2e} J ")
Lsun= 3.828e26 #Watt
#Divide the total energy by the energy radiated per second by the Sun (the luminosity of the Sun)
tnuclear= Enuclear/Lsun
print(f"Sun's Hydrogen fusing lifetime = {tnuclear/3600/24/365.25:.1e} years")
#This means a 10 billion years on the main sequence. 
