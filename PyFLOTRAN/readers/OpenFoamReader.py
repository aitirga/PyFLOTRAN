"""
Base interface for a reader class
"""
import numpy as np
import logging
from PyFLOTRAN.readers import BaseReader
logger = logging.getLogger(__name__)
import Ofpp
from PyFLOTRAN.config import config
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class OpenFoamReader(BaseReader):
    def __init__(self, filename=None):
        self.filename = Path(filename) if filename else Path(config.open_foam_reader.filename)
        logger.info(f"Reading OpenFOAM mesh file from {self.filename}")
        super().__init__(filename=self.filename)


    def open_file(self, filename):
        self.mesh = Ofpp.FoamMesh(self.filename)

    @property
    def cell_centers(self) -> np.array:
        if not config.globals.is_cell_centers_read:
            logger.info(f"Reading cell center locations from {self.filename / '0/C'}")
            self.mesh.read_cell_centres(self.filename / "0/C")
            config.globals.is_cell_centers_read = True
        return self.mesh.cell_centres

    def get_data(self) -> np.ndarray:
        """
        Outputs the read data
        :return:
        """
        return np.array(0)

    def build_info(self):
        """
        Generates a dictionary containing the basic info of the read data
        :return:
        """
        self.info = {}

