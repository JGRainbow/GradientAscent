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
    from utils import generate_gaussian_array

    arr = generate_gaussian_array(20, 20, 0.05)
    crd = Coordinate(0, 0)
    asc = Ascender(arr, crd)
    ap = AscentPlotter.animate(asc)
