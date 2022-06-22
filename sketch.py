# Firstly import all the relevant libraries needed 
from PIL import ImageFont, Image, ImageDraw, ImageOps
import numpy as np
import cv2

# Lets define now the Character_Set Map 
# It stores the luminoscity order
Character_Set = {
    "standard" : "@%#*+=:. ",
    "complex" : "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

# Let us define the background black or white
background = "white"                # you can change it to black according to the image chosen
if background == "white":
    background_code = 255
elif background == "black":
    background_code = 0

def character_data(mode):
    font = ImageFont.truetype("./fonts/cour.ttf", 10)
    scale = 2                                          #To make the width and height equal
    character_list = Character_Set[mode]
    return character_list, font, scale


# Now we initialise the character_list, font, scale for the square pixels
character_list, font, scale = character_data("complex")

chars_size = len(character_list)
col_size = 500                                  # this value depends upon the image selected

# Input the image in 'scan' variable
scan = cv2.imread('./data/cake.jpg')

# Converting the colored image to Grayscale form
scan = cv2.cvtColor(scan, cv2.COLOR_BGR2GRAY)


# Now to make the pencil sketch of the image we took :

# first inverting the black and white image
scan_inverted = cv2.bitwise_not(scan)

# Now applying Gausiian blur to image
# here 25 is kernel size estimated by trial and error method
scan_blurred = cv2.GaussianBlur(scan_inverted, (25,25), 0)

# now inverting the blurred image
scan_inverted_blurred = cv2.bitwise_not(scan_blurred)

# Now finally converting the black and white image to pencil sketch
sketch_scan = cv2.divide(scan, scan_inverted_blurred , scale=256.0)

# now save the Pencil sketched image in output folder under 'sketch_scan' name
cv2.imwrite("./output/tree_sketch.jpg", sketch_scan)

# Now we have to make ascii art of the pencil sketch image we just formed

# Reading Input : pencil sketch form of Image under 'scan' name
scan = cv2.imread("./output/tree_sketch.jpg")

# Converting Color Image to Grayscale version
scan = cv2.cvtColor(scan, cv2.COLOR_BGR2GRAY)

# Extracting height and width of the image
height, width = scan.shape

# Now we define the height and width of each cell ,i.e. pixel
cell_width = width / col_size
cell_height = scale * cell_width

# number of rows
rows_size = int(height / cell_height)

# Now we find the Height and Width of ASCII image
character_width, character_height = font.getsize("A")

# Now we calculate final output width and height
output_width = character_width * col_size
output_height = scale * character_height * rows_size

# Now we make a new Image using PIL
output_scan = Image.new("L", (output_width, output_height), background_code)
draw = ImageDraw.Draw(output_scan)

# Mapping the Characters
for i in range(rows_size):
    min_height = min(int((i + 1) * cell_height), height)
    row_pix = int(i * cell_height)

    line = "".join([character_list[
        min(int(
            np.mean(scan[row_pix:min_height, int(j*cell_width)
                    :min(int((j + 1) * cell_width), width)]) / 255 * chars_size
        ), chars_size - 1)]
        for j in range(col_size)]) + "\n"

    # Draw string at a given position (x,y)
    draw.text((0, i * character_height), line, fill=255-background_code, font=font)

# Now some editing by inverting the image and removing the extra border
if background == "white":
    scan_edited = ImageOps.invert(output_scan).getbbox()
elif background == "black":
    scan_edited = output_scan.getbbox()

# Saving the final ascii art form of pencil sketch of the image taken
ascii_sketch = output_scan.crop(scan_edited)
ascii_sketch.save("./output/tree_ascii.jpg")