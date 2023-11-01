import numpy as np
import subprocess
import ffmpeg

# input is RGB array
# output is YUV  array
def RGB2YUV(rgb):
    m = np.array([[0.29900, -0.16874, 0.50000],
                  [0.58700, -0.33126, -0.41869],
                  [0.11400, 0.50000, -0.08131]])

    yuv = np.dot(rgb, m)
    yuv[:] += 128.0
    return yuv


# transforms YUV coordinates to RGB coordinates
def YUV2RGB(yuv):
    m = np.array([[1.0, 1.0, 1.0],
                  [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                  [1.4019975662231445, -0.7141380310058594, 0.00001542569043522235]])

    rgb = np.dot(yuv, m)
    rgb[:, :, 0] -= 179.45477266423404
    rgb[:, :, 1] += 135.45870971679688
    rgb[:, :, 2] -= 226.8183044444304
    return rgb

#test
rgb=(100,150,200)
x=RGB2YUV(rgb)
print(x)


################################################EX 2####################################################

#calls ffmpeg to resize image
def resize_image(input_im,output_im,new_w,new_h):


    ffmpeg_command = [
        'ffmpeg',
        '-i', input_im,
        '-vf', f'scale={new_w}:{new_h}',
        output_im
    ]



    subprocess.run(ffmpeg_command)

#test
input_image='hill.jpeg'
output_image='/home/manu/Desktop/SCAV/resized_image.jpeg'
new_width=640
new_height=480

resize_image(input_image,output_image,new_width,new_height)

################################################EX 3####################################################

#serpentine algorithm
def serpentine(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the entire file into a bytes object
            jpeg_bytes = file.read()

        # Extract the image data
        image_data = jpeg_bytes[2:]

        # Initialize variables for zigzag pattern
        rows, cols = 0, 0
        width = 0
        height = 0

        while len(image_data) > 0:
            # Read and process the byte at the current position
            current_byte = image_data[:1]

            # Do something with the current_byte, for example, print it
            print(current_byte[0], end=' ')

            # Move to the next position in zigzag pattern
            if (rows + cols) % 2 == 0:
                if cols < width - 1:
                    cols += 1
                else:
                    rows += 1
                if rows > height - 1:
                    rows = height - 1
                    cols += 2
                if cols > width - 1:
                    cols = width - 1
            else:
                if rows < height - 1:
                    rows += 1
                else:
                    cols += 1
                if cols > width - 1:
                    cols = width - 1
                if rows > height - 1:
                    rows = height - 1
                    cols += 2

            # Remove the processed byte from the image data
            image_data = image_data[1:]

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage example
serpentine('hill.jpeg')

################################################EX 4####################################################

#using ffmpeg transform to bw and compress

def transform_to_bw_and_compress(input_path, output_path, quality=0):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_path,
        '-vf', 'format=gray',  # Convert to black and white
        '-q:v', str(quality),  # Adjust quality to achieve maximum compression
        output_path
    ]

    subprocess.run(ffmpeg_cmd)


# Example :
input_image = 'hill.jpeg'  # Replace with the path to your input image
output_image = '/home/manu/Desktop/SCAV/bw_image.jpeg'  # Replace with the path where you want to save the black and white image
compression_quality = 1  # Adjust quality (0-51) to maximize compression (lower quality means higher compression)

transform_to_bw_and_compress(input_image, output_image, compression_quality)


################################################EX 5####################################################


def run_length_encode(data):
    if not data:
        return []

    encoded_data = []
    current_byte = data[0]
    count = 1

    for byte in data[1:]:
        if byte == current_byte:
            count += 1
        else:
            encoded_data.extend([current_byte, count])
            current_byte = byte
            count = 1

    encoded_data.extend([current_byte, count])
    return encoded_data

def run_length_decode(encoded_data):
    if not encoded_data:
        return []

    decoded_data = []
    for i in range(0, len(encoded_data), 2):
        byte = encoded_data[i]
        count = encoded_data[i + 1]
        decoded_data.extend([byte] * count)

    return decoded_data

# Example usage
data = b'\x01\x01\x01\x02\x02\x03\x03\x03\x03'
encoded_data = run_length_encode(data)
decoded_data = run_length_decode(encoded_data)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)

################################################EX 5####################################################
from scipy import fft


#Test
x=[-6, 5, -4, 3, -2, 1]

#dct call
gfg=fft.dct(x,3)

print(gfg)