<div align="center">
  <h1>🕵️‍♂️ Hidden Pixels</h1>
  <p><b>A Python-based Least Significant Bit (LSB) image steganography engine.</b></p>

  <!-- Dynamic Badges -->
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3-blue.svg?logo=python&logoColor=white" alt="Python 3"></a>
  <a href="https://github.com/Pillow/Pillow"><img src="https://img.shields.io/badge/Dependency-Pillow-yellow.svg" alt="Pillow"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
</div>

<br />

## 📖 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [How It Works (The Math)](#-how-it-works-the-math)
- [Prerequisites](#-prerequisites)
- [Usage Guide](#-usage-guide)
- [License](#-license)

---

## 🔎 Overview

**Hidden Pixels** is a lightweight steganography tool that allows users to secretly embed hidden text messages inside standard image files without noticeably altering the image's appearance. It serves as a practical demonstration of data obfuscation and bit-level image manipulation.

---

## ✨ Features

* **🔒 Imperceptible Encoding:** Hides custom text messages within the Least Significant Bits (LSB) of an image's RGB channels.
* **🔄 Precision Decoding:** Extracts hidden messages from stego-images, stopping automatically when the secret cryptographic delimiter is reached.
* **🛡️ Lossless Output:** Automatically saves output images in `.png` format to ensure hidden data is not destroyed by lossy compression algorithms.
* **⚙️ Dynamic Edge-Case Handling:** Safely handles pixel edge cases, ensuring data is written securely even if the payload bit length isn't a perfect multiple of three.

---

## 🔬 How it Works (The Math)

This tool utilizes the **Least Significant Bit (LSB) replacement** algorithm. 

Every pixel in a standard image is made of Red, Green, and Blue (RGB) channels, represented by 8-bit integers (ranging from 0-255). By modifying only the *last* bit of these integers, the decimal color value changes by a maximum of 1 unit.

| Channel | Original Value | Original Binary | Payload Bit | New Binary | New Value | Visual Shift |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Red** | `150` | `1001011`**`0`** | **`1`** | `1001011`**`1`** | `151` | None |
| **Green** | `200` | `1100100`**`0`** | **`0`** | `1100100`**`0`** | `200` | None |
| **Blue** | `85` | `0101010`**`1`** | **`0`** | `0101010`**`0`** | `84` | None |

Because the human eye cannot detect such a microscopic shift in color (`±1`), we can safely overwrite these last bits with the binary representation of our secret text. The decoder then walks the exact same path across the image's grid, sweeps up those last bits, and reassembles them back into characters.

---

## 🛠️ Prerequisites

To run this project, you will need **Python 3** installed on your machine, along with the `Pillow` library for image processing.

Install the required dependency using pip:
```bash
pip install Pillow

💻 Usage Guide
Ensure that your cover image (e.g., sample.jpg) is located in the same directory as the scripts before running them.

1. Encoding a Message
To hide a message inside an image, run the encoder script from your terminal:

Bash
## python encoder.py
The script will prompt you for an input image name.

Enter your secret message.

Provide a name for the output file. The script will generate a new .png file containing your hidden text.

2. Decoding a Message
To extract a hidden message from a stego-image, run the decoder script:

Bash
 ## python decoder.py
The script will prompt you for the name of the stego-image (e.g., secret_output.png).

It will extract the bits, translate them back into characters, and print your hidden message to the terminal!

Developed by shubh shanker shukla / shubhshukla098-design]
