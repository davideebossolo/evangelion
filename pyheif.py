import pyheif
from PIL import Image

input_files = ["IMG_7273.HEIC", "IMG_7274.HEIC"]
output_files = ["30.jpg", "31.jpg"]

for input_file, output_file in zip(input_files, output_files):
    heif_file = pyheif.read(input_file)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(output_file, "JPEG")
