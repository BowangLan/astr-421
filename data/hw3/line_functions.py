import numpy as np
import astropy.units as u
from astropy.modeling.models import BlackBody

def planck(lam, temp):
    '''
    Calculates the intensity of a perfect blackbody
    in thermal equilibrium at a given temperature and
    wavelength
    
    Parameters
    ----------
    lam: float
        Wavelength (in cm) of light being considered
    temp: float
        Temperature (in K) of the blackbody
        
    Returns
    -------
    float
        The value of the planck function (in cgs units)
        at the given temperature and wavelength
    
    '''
    bb = BlackBody(temp*u.K, scale=1*u.erg/u.s/u.cm**2/u.sr/u.cm)
    return bb(lam*u.cm).value

def one_layer_I(i0, tau, B):
    '''
    Calculates the emergent intensity of a beam of light
    with an intial intensity of i0 travelling an optical 
    depth tau through a layer with blackbody radiance B
    
    Parameters
    ----------
    i0: float
        The initial intensity of the beam (in erg s^-1 cm^-2 sr^-1 cm^-1)
    tau: float
        The optical depth that  the beam travels
    B: float
        The blackbody radiance of the medium (in erg s^-1 cm^-2 sr^-1 cm^-1)
        
    Returns
    -------
    float
        The emergent intensity of the light (in erg s^-1 cm^-2 sr^-1 cm^-1)
    
    '''
    return i0*np.exp(-tau) + B*(1 - np.exp(-tau))


def two_layer_I(i0, tau_l, Bl, tau_s, Bs):
    '''
    Calculates the emergent intensity of a light beam
    with initial intensity i0  that travels an optical depth
    tau_l through an interior layer with blackbody radiance Bl 
    and then travels and optical depth tau_s through a surface 
    layer with blackbody radiance Bs
    
    Parameters
    ----------
    i0: float
        The initial intensity of the beam (in erg s^-1 cm^-2 sr^-1 cm^-1)
    tau_l: float
        The optical depth that  the beam travels through the interior layer
    Bl: float
        The blackbody radiance of interior layer (in erg s^-1 cm^-2 sr^-1 cm^-1)
    tau_s: float
        The optical depth that  the beam travels through the surface layer
    Bs: float
        The blackbody radiance of the surface layer (in erg s^-1 cm^-2 sr^-1 cm^-1)
        
    Returns
    -------
    float
        The emergent intensity of the light (in erg s^-1 cm^-2 str^-1 cm^-1)
    
    '''
    i1 = i0*np.exp(-tau_l) + Bl*(1 - np.exp(-tau_l))
    return i1*np.exp(-tau_s) + Bs*(1 - np.exp(-tau_s))