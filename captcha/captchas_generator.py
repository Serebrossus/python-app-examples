import random

characters = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
CAPTCHA_LENGTH = 4


def random_string():
    rnd_string = (random.choice(characters) for _ in range(CAPTCHA_LENGTH))
    return ''.join(rnd_string)


def generate_captcha(count):
    for _ in range(int(count)):
        print(random_string())


generate_captcha(10000)

# TODO
# 1. generate captcha image by text
# 2. save image captcha to file with name captha text
# 3. profit
