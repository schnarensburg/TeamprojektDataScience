from PIL import Image, ImageChops
import os

def text_to_image(text):
    # Define the dimensions of the image based on the gear's text representation
    width = len(text.split('\n')[0])
    height = len(text.split('\n'))

    # Create a new image with a white background
    image = Image.new('RGB', (width, height), 'white')

    # Iterate over each character in the text and set the corresponding pixel in the image
    pixels = image.load()
    for y, line in enumerate(text.split('\n')):
        for x, char in enumerate(line.strip()):
            if char != ' ':
                pixels[x, y] = (0, 0, 0)  # Set non-empty characters to black

    return image

def compare_images(image1, image2):
    diff_image = ImageChops.difference(image1, image2)
    diff_pixels = diff_image.getdata()

    # Count the number of non-black pixels in the difference image
    diff_count = sum(pixel != (0, 0, 0) for pixel in diff_pixels)

    # Normalize the difference count to a percentage
    total_pixels = image1.size[0] * image1.size[1]
    difference_percentage = (diff_count / total_pixels) * 100

    return difference_percentage

# Provide the file paths for the original gear and the gear to compare

script_dir = os.path.dirname(os.path.abspath(__file__))
original_gear_path = os.path.join(script_dir, "../../01_DATA/Z13/PointClouds/.txt2D/KW01_2D.txt")

script_dir = os.path.dirname(os.path.abspath(__file__))
compared_gear_path = os.path.join(script_dir, "../../01_DATA/Z13/PointClouds/.txt2D/KW02_2D.txt")

# Read the contents of the gear files
with open(original_gear_path, 'r') as file:
    original_gear_text = file.read()

with open(compared_gear_path, 'r') as file:
    compared_gear_text = file.read()

# Convert the gear texts to images
original_image = text_to_image(original_gear_text)
compared_image = text_to_image(compared_gear_text)

# Compare the images and get the difference percentage
difference_percentage = compare_images(original_image, compared_image)

# Display the difference percentage
print(f"The gears are {difference_percentage}% different.")
