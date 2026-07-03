Hidden Pixels: LSB Image Steganography

Hidden Pixels is a Python-based steganography engine that allows users to secretly embed hidden text messages inside standard image files without noticeably altering the image's appearance.

🚀 Features

Encode: Hides custom text messages within the Least Significant Bits (LSB) of an image's RGB channels.

Decode: Extracts hidden messages from stego-images, stopping automatically when the secret delimiter is reached.

Lossless Output: Automatically saves output images in .png format to ensure hidden data is not destroyed by compression algorithms.

Dynamic Handling: Safely handles pixel edge cases ensuring data is written securely even if the bit length isn't a perfect multiple of three.

🛠️ Prerequisites

To run this project, you will need Python 3 installed on your machine, along with the Pillow library for image processing.

pip install Pillow


💻 Usage

1. Encoding a Message

To hide a message inside an image, run the encoder script from your terminal:

python encoder.py


The script will prompt you for an input image (e.g., sample.jpg). Note: The image must be in the same directory as the script.

Enter your secret message.

Provide a name for the output file. The script will generate a new .png file containing your hidden text.

2. Decoding a Message

To extract a hidden message from a stego-image, run the decoder script:

python decoder.py


The script will prompt you for the name of the stego-image (e.g., secret_output.png).

It will extract the bits, translate them back into characters, and print your hidden message to the terminal!

🧠 How it Works (The Math)

This tool uses Least Significant Bit (LSB) replacement.

Every pixel in a standard image is made of Red, Green, and Blue (RGB) channels, represented by 8-bit integers (0-255). By modifying only the last bit of these integers, the color value changes by a maximum of 1 unit (e.g., a Red value of 150 becomes 151).

Because the human eye cannot detect such a microscopic shift in color, we can safely overwrite these last bits with the binary representation of our secret text. The decoder then walks the exact same path across the image's grid, sweeps up those last bits, and reassembles them into characters.
