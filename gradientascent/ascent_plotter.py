import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
from gradientascent.ascender import Ascender, Coordinate

class AscentPlotter:

    FPS = 2

    @classmethod
    def animate(cls, ascender: Ascender):
        plt.style.use('ggplot')
        fig, ax = plt.subplots()
        ax.imshow(ascender.array, cmap='Reds')

        def animate_func(i):
            coord = next(ascender)
            cls._highlight_cell(coord, ax, 
                                color='limegreen',
                                linewidth=3)
            return [ax]

        _ = animation.FuncAnimation(fig,
                                    animate_func,
                                    interval = 1000 / cls.FPS)
        plt.axis('off')
        plt.show()


    @staticmethod
    def _highlight_cell(coordinate: Coordinate, ax, **kwargs):
        rect = plt.Rectangle((coordinate.x-.5, coordinate.y-.5), 1, 1, 
                             fill=False, **kwargs)
        ax = ax or plt.gca()
        ax.add_patch(rect)
        plt.axis('off')
        return rect


if __name__ == '__main__':
    import numpy as np

    def generate_gaussian_array(h, w, noise_factor=0.5):
        x, y = np.meshgrid(np.linspace(-1, 1, h), np.linspace(-1, 1, w))
        d = np.sqrt(x*x + y*y)
        sigma, mu = 1.0, 0.0
        white_noise = np.random.rand(h, w)
        g = np.exp(-( (d - mu) ** 2 / ( 2.0 * sigma ** 2 ) ) )
        return g + noise_factor * white_noise

    arr = generate_gaussian_array(20, 20, 0.05)
    crd = Coordinate(0, 0)
    asc = Ascender(arr, crd)
    ap = AscentPlotter().animate(asc)
