from skimage.io import imread
import matplotlib.pyplot as plt


class DigitalElevationModel:

    def __init__(self, file_path):
        self.file_path = file_path
        self.array = imread(self.file_path)

    @classmethod
    def from_file_path(cls, file_path):
        return cls(file_path)

    def display(self):
        plt.imshow(self.array, cmap='winter')
        plt.axis('off')
        plt.show()
    

if __name__ == '__main__':
    file_path = r"C:\Users\jacob\OneDrive\Documents\Data\HeightData\Everest\GeoTiffs\n27e086.tif"
    dem = DigitalElevationModel.from_file_path(file_path)
    dem.display()