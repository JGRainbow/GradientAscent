from gradientascent.ascent_plotter import AscentPlotter
from gradientascent.digital_elevation_model import DigitalElevationModel
from gradientascent.ascender import Ascender, Coordinate


EVEREST_PATH = r"C:\Users\jacob\OneDrive\Documents\Data\HeightData\Everest\GeoTiffs\n27e086.tif"

dem = DigitalElevationModel.from_file_path(EVEREST_PATH)
array = dem.get_array()
array = array[-500:, -500:]

coord = Coordinate(130, 194)
asc = Ascender(array, coord)
ap = AscentPlotter.animate(asc)


