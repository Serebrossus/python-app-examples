import os
import random

import numpy as np
from PIL import Image
from captcha.image import ImageCaptcha
import doctest

characters = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
CAPTCHA_LENGTH = 4
CAPTCHA_WIDTH = 360
CAPTCHA_HEIGTH = 130
CAPTCHA_DIR = 'images'


def random_string():
    """
    generate random text from captcha
    :return:
    >>> random_string()
    """
    rnd_string = (random.choice(characters) for _ in range(CAPTCHA_LENGTH))
    return ''.join(rnd_string)


def generate_captcha(count):
    """
    :param count: how many times generate captcha
    :return:
    >>> generate_captcha(1)
    >>> generate_captcha(-1)
    """
    for _ in range(int(count)):
        captcha_text = random_string()
        generate_image_captcha(captcha_text)
        print(captcha_text)


def generate_image_captcha(captcha_text, width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGTH):
    """
    :param captcha_text: input text
    :param width: image width
    :param height: image height
    :return: captcha text and array from captcha image

    >>> generate_image_captcha(random_string(), 150,20)
    >>> generate_image_captcha(random_string(), 160,40)
    >>> generate_image_captcha(random_string(), 170,30)
    """

    if not os.path.exists(CAPTCHA_DIR):
        os.makedirs(CAPTCHA_DIR)
    image = ImageCaptcha(width=width, height=height)
    captcha = image.generate(captcha_text)
    image.write(captcha_text, os.path.join(CAPTCHA_DIR, captcha_text + '.png'))
    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image


# auto test
# doctest.testmod()
generate_captcha(10000)

# generates captcha text and saves it to file
# text, c_image = generate_image_captcha(random_string())
# print('Text: {} image: {}'.format(text, c_image))
