from typing import List, Union, Any
from Crypto.Util.strxor import strxor
from PIL import Image
import numpy as np


class Color:

    def __init__(self, red: int, green: int, blue: int, alpha: int = 0) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __eq__(self, target: Any) -> bool:
        if not isinstance(target, Color):
            return False
        return self.red == target.red and self.green == target.green and self.blue == target.blue

    def __str__(self) -> str:
        return f"(r:{self.red}, g:{self.green}, b:{self.blue}, a:{self.alpha})"


class Pixel:

    def __init__(self, color: Color, x: int, y: int) -> None:
        self.color = color
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'color : {self.color}, pos: ({self.x}, {self.y})'


def get_all_pixel_with_color(image: List[List[List[int]]], color_to_pick: Color) -> List[Pixel]:
    pixels = []

    for y, row in enumerate(image):
        for x, color_of_pixel in enumerate(row):
            color = Color(*color_of_pixel)

            if color == color_to_pick:
                pixels.append(Pixel(color, x, y))

    return pixels


def get_all_red_component(image: List[List[List[int]]]) -> List[int]:
    red_values = []

    for row in image:
        for red, green, blue, alpha in row:
            red_values.append(red)

    return red_values


def convert_list_of_int_in_bin(values: List[int]) -> str:
    return "".join(bin(value)[2:].zfill(8) for value in values)


def get_message_from_file(path: str):
    bytes_output = b""

    with open(path, 'rb') as file:
        for line in file.readlines():
            bytes_output += line

    return bytes_output


def resize_hash(encrypted_message: bytes, hash: bytes) -> bytes:
    return hash[:len(encrypted_message)]

if __name__ == "__main__":
    image = Image.open("image-defi.png")
    image = np.array(image)
    encrypted_message = get_message_from_file("message-mystere.mj")
    red_component = get_all_red_component(image)
    hash = bytes(red_component)
    resized_hash = resize_hash(encrypted_message, hash)

    print(strxor(resized_hash, encrypted_message).decode('utf-8'))