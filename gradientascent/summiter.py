from typing import List

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from gradientascent.ascender import Ascender, Coordinate


class Summitter:

    def __init__(self, ascender: Ascender):
        self.ascender = ascender
        # -1 represents unvisited, 0 represents does not reach summit, 1 represents reaches summit
        self.summit_heatmap = np.zeros_like(ascender.array) - 1
        self.summit_coord = self._get_summit_coord(self.ascender.array)

    @staticmethod
    def _get_summit_coord(array):
        y, x = np.unravel_index(np.argmax(array), array.shape)
        return Coordinate(x, y)

    def _mark_trace_state(self, trace: List[Coordinate], new_state):
        for coord in trace:
            self.summit_heatmap[coord.y][coord.x] = new_state

    def _get_next_unvisited_coord(self):
        try:
            cy, cx =  np.argwhere(self.summit_heatmap == -1)[0]
            return Coordinate(cx, cy)
        except IndexError:
            return None

    def _is_visited(self, coordinate):
        return self.summit_heatmap[coordinate.y][coordinate.x] >= 0

    def _get_trace_to_visited_coordinate(self, next_unvisited_coord):
        self.ascender.reset_start_coordinate(next_unvisited_coord)
        trace = [coord for coord in self.ascender if not self._is_visited(coord)]
        last_coord = self.ascender.current_coordinate
        value = self.summit_heatmap[last_coord.y][last_coord.x] 
        return trace, max(value, 0)

    def create_summit_heatmap(self):
        # 0. Find summit coordinate and mark as 1
        # 1. Get next unvisited coordinate (-1)
        # 2. Trace route to next visited coordinate, 
            # a. If next visisted coordinate is 0, then mark all trace coordinates as 0
            # b. If next visited coordinate is 1, then mark all trace coordinates a 1
        # 3. Terminate when no remaining unvisited coordinates (-1)

        self.summit_heatmap[self.summit_coord.y][self.summit_coord.x] = 1

        while True:
            next_unvisited_coord = self._get_next_unvisited_coord()
            if not next_unvisited_coord:
                break
            trace, value = self._get_trace_to_visited_coordinate(next_unvisited_coord)
            self._mark_trace_state(trace, value)

        return self.summit_heatmap

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
    from gradientascent.ascent_plotter import AscentPlotter

    arr = generate_gaussian_array(99, 99, 1e-3)
    crd = Coordinate(5, 24)
    asc = Ascender(arr, crd)
    AscentPlotter.animate(asc)
    smt = Summitter(asc)
    c = smt.summit_coord
    smt.plot_summit_heatmap()
    print(smt.summit_heatmap)

