import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 8.617333262145e-5  # Boltzmann constant in eV/K
h = 6.62607015e-27       # Planck's constant in erg*s
m_e = 9.10938356e-28     # Electron mass in g
chi_ion = 13.595         # Ionization energy of hydrogen in eV
E2_E1 = 10.2             # Energy difference between n=2 and n=1 in eV
g2 = 8                   # Degeneracy of n=2
g1 = 2                   # Degeneracy of n=1
Pe_cgs = 2e8             # Electron pressure in erg/cm^3

# Temperature range (5000K to 25000K in 1K increments)
Teff = np.arange(5000, 25001, 1)

# Calculate Ne from Pe and T
def calculate_ne(Teff):
    return Pe_cgs / (k_B * Teff)

# Saha equation: NII / NI
def saha_equation(Teff, Ne):
    saha_prefactor = (2 * np.pi * m_e * k_B * Teff / h**2)**1.5 * 2 / Ne
    saha_exp = np.exp(-chi_ion / (k_B * Teff))
    NII_NI = saha_prefactor * saha_exp
    return NII_NI

# Boltzmann equation: N2 / N1
def boltzmann_equation(Teff):
    boltzmann_exp = np.exp(-E2_E1 / (k_B * Teff))
    N2_N1 = (g2 / g1) * boltzmann_exp
    return N2_N1

# Calculate N2 / (N1 + N2), NII / Ntotal, and N2 / Ntotal
def calculate_ratios(Teff):
    Ne = calculate_ne(Teff)
    NII_NI = saha_equation(Teff, Ne)
    N2_N1 = boltzmann_equation(Teff)
    
    # Neutral hydrogen fraction
    NI_NII = 1 / (1 + NII_NI)  # Fraction of neutral H
    N2_Ntotal = (N2_N1 * NI_NII) / (1 + N2_N1)
    
    # N2 / (N1 + N2)
    N2_N1_N2 = N2_N1 / (1 + N2_N1)
    
    # Ionized hydrogen fraction
    NII_Ntotal = NII_NI / (1 + NII_NI)
    
    return N2_N1_N2, NII_Ntotal, N2_Ntotal

# Plot results
def plot_results(Teff, N2_N1_N2, NII_Ntotal, N2_Ntotal):
    plt.figure()
    plt.plot(Teff, N2_N1_N2, label='$N_2 / (N_1 + N_2)$')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Fraction')
    plt.title('$N_2 / (N_1 + N_2)$ vs Temperature')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    plt.figure()
    plt.plot(Teff, NII_Ntotal, label='$N_{II} / N_{total}$', color='orange')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Fraction')
    plt.title('$N_{II} / N_{total}$ vs Temperature')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    plt.figure()
    plt.plot(Teff, N2_Ntotal, label='$N_2 / N_{total}$', color='green')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Fraction')
    plt.title('$N_2 / N_{total}$ vs Temperature')
    plt.grid(True)
    plt.legend()
    plt.show()

# Main function
def main():
    N2_N1_N2, NII_Ntotal, N2_Ntotal = calculate_ratios(Teff)
    plot_results(Teff, N2_N1_N2, NII_Ntotal, N2_Ntotal)

if __name__ == "__main__":
    main()
