#Data reduction of an IFU cube
import numpy as np
from astropy.io import fits


random_coord_length = 10

def read_configuration_file(fname):
    config_dict = {'vmin':-1000, 'vmax':1000, 'cand_velocity':1000, 'object_name':'b'}
    return config_dict['vmin'], config_dict['vmax'], config_dict['cand_velocity'], config_dict['object_name']
    
def read_coordinate_file(fname, object_name):
    object_x = random.random() * 25.
    object_y = random.random() * 38.
    
    x_list = random.random(random_coord_length) * 25.
    y_list = random.random(random_coord_length) * 38. 

    return object_x, object_y, x_list, y_list

def read_ifu_data(fname):
    wavelength = np.linspace(-10000, 10000, 3975)
    return fits.open(fname)[0].data
    return wavelength, random.random((3975, 38, 25))
    

def extract_spectrum_ifu(data_cube, object_x, object_y):
    return np.random.random(3975)


def plot_spatial_ifu(ax, data_cube, x_coordinates, y_coordinates, vmin=None, vmax=None):
    x_coordinates = np.random.random(10) * 25.
    y_coordinates = np.random.random(10) * 38.
    ax.plot([1, 2, 3], 'r-', lw=4)
    
    return np.random.random((38, 25))
    
def plot_histogram(ax, spatial_ifu):
    ax.plot([1,2,3], 'r-', lw=3)

    
def plot_spectra(ax, ifu_wavelength, object_flux, solar_wavelength=None, solar_flux=None):
    ax.plot([1,2,3], 'r-', lw=3)
    

    
    
def read_shift_solar_spectrum(ax, fname, wavelength, velocity):
    wave = np.arange(6000, 8000)
    flux = np.random.random(wave.shape)
    return flux

    
    
    
    

if __name__ == '__main__':
    vmin, vmax, cand_velocity, object_name = read_configuration_file('reduction.config')
    x_coordinates, y_coordinates, object_x, object_y = read_coordinate_file('data/coordinates.dat', object_name)
    wavelength, ifu_data = read_ifu_data('data/ifu_data.fits')
    object_flux = extract_spectrum_ifu(ifu_data, object_x, object_y)
    
    fig = figure(1)
    fig.clf()
    
    ax = fig.add_subplot(2, 2, 1)
    spatial_ifu = plot_spatial_ifu(ax, ifu_data, x_coordinates, y_coordinates)

    ax = fig.add_subplot(2, 2, 2)
    plot_histogram(ax, spatial_ifu)
    
    ax = fig.add_subplot(2, 2, 3)
    plot_spectra(ax, wavelength, object_flux)
    show()
    
    
    
    
    
    
    
    