import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np
from gradientascent.ascender import Ascender, Coordinate

class AscentPlotter:

    FPS = 200

    @classmethod
    def animate(cls, ascender: Ascender):
        MAX = ascender.summit_height
        MIN = ascender.min_height
        h, w = ascender.array.shape

        plt.style.use('ggplot')
        fig, ax = plt.subplots(1, 2)
        ax[0].imshow(ascender.array, cmap='Reds')
        ax[1].imshow(cls._create_height_array(ascender.current_height, 
                                              max_=MAX, min_=MIN,
                                              height=h, width=w // 8), cmap='Reds')

        def animate_func(i):
            coord = next(ascender)
            cls._highlight_cell(coord, ax[0], 
                                color='limegreen',
                                linewidth=3)
            ax[1].imshow(cls._create_height_array(ascender.current_height, 
                                                  max_=MAX, min_=MIN,
                                                  height=h, width=w // 8), cmap='Reds')
            return [ax]

        _ = animation.FuncAnimation(fig,
                                    animate_func,
                                    interval = 1000 / cls.FPS)
        plt.axis('off')
        ax[0].set_axis_off()
        ax[1].set_axis_off()
        plt.show()


    @staticmethod
    def _create_height_array(current_height, max_, min_, height, width, **kwargs):
        height_val = int(height * (current_height - min_) / (max_ - min_))
        array = np.zeros((height, 1))
        array[-height_val:] = 1
        return np.concatenate([array] * width, axis=1)           


    @staticmethod
    def _highlight_cell(coordinate: Coordinate, ax, **kwargs):
        rect = plt.Rectangle((coordinate.x-.5, coordinate.y-.5), 1, 1, 
                             fill=False, **kwargs)
        ax.add_patch(rect)
        return rect


if __name__ == '__main__':
    import numpy as np
    from utils import generate_gaussian_array

    arr = generate_gaussian_array(20, 20, 0.05)
    crd = Coordinate(0, 0)
    asc = Ascender(arr, crd)
    ap = AscentPlotter.animate(asc)
