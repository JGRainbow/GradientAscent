import numpy as np


def generate_gaussian_array(h, w, noise_factor=0.5):
    x, y = np.meshgrid(np.linspace(-1, 1, h), np.linspace(-1, 1, w))
    d = np.sqrt(x*x + y*y)
    sigma, mu = 1.0, 0.0
    white_noise = np.random.rand(w, h)
    g = np.exp(-( (d - mu) ** 2 / ( 2.0 * sigma ** 2 ) ) )
    return g + noise_factor * white_noise
