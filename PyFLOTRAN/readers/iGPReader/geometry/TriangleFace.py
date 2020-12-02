import numpy as np

from rwm_scripts.source.geometry import BaseFace


class TriangleFace(BaseFace):
    def __init__(self, nodes, coords):
        super().__init__(nodes, coords)

    def compute_centroid(self):
        return np.mean(self.coords, axis=0)