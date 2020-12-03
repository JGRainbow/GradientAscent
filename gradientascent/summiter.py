import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from gradientascent.ascender import Ascender, Coordinate


class Summitter:

    def __init__(self, ascender: Ascender):
        self.ascender = ascender
        self.summit_heatmap = np.zeros_like(ascender.array)
        self.summit_coord = self._get_summit_coord(self.ascender.array)

    @staticmethod
    def _get_summit_coord(array):
        y, x = np.unravel_index(np.argmax(array), array.shape)
        return Coordinate(x, y)

    def create_summit_heatmap(self):
        return self.summit_heatmap + 1

    def plot_summit_heatmap(self):
        summit_heatmap = self.create_summit_heatmap()
        plt.figure(figsize=(5,5))
        sns.heatmap(summit_heatmap, annot=False,
                                    xticklabels=False,
                                    yticklabels=False,
                                    cbar=False)
        plt.show()


if __name__ == '__main__':
    from utils import generate_gaussian_array

    arr = generate_gaussian_array(20, 10, 0.05)
    crd = Coordinate(0, 0)
    asc = Ascender(arr, crd)
    smt = Summitter(asc)
    c = smt.summit_coord
    print(c)
    smt.plot_summit_heatmap()
