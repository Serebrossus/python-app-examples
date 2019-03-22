import os.path
import cv2
import glob
import imutils
# import doctest

CAPTCHA_IMAGE_FOLDER = 'images'
OUTPUT_FOLDER = 'output_images'


def split_captcha_into_separate_letters():
    '''
    >>> split_captcha_into_separate_letters()
    '''

    # Get all captcha images
    captcha_image = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
    counts = {}

    for (i, captcha_image) in enumerate(captcha_image):
        # if i < 2:
        print("[i] start processing image {}-{}\n".format(i + 1, len(captcha_image)))

        file_name = os.path.basename(captcha_image)
        captcha_text = os.path.splitext(file_name)[0]

        img = cv2.imread(captcha_image)

        if img is None:
            continue

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Add padding arround image
        img_gray = cv2.copyMakeBorder(img_gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)

        # convert to black and white
        img_black_white = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        clone = img_black_white.copy()
        contours, hierarchy = cv2.findContours(clone.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print('contours length: {}'.format(len(contours)))

        # hack
        contours = contours[0] if imutils.is_cv2() else contours[1]
        # print('contours : {}'.format(contours))

        img_letter_regions = []
        for contour in contours:
            # abc = cv2.contourArea(contour)
            # print(abc)
            # print(' - ')
            # print(contour)
            # print('\n')
            (x, y, w, h) = cv2.boundingRect(contour)
            print('X: {}\t Y: {}\t W: {}\t H: {}'.format(x, y, w, h))

            if w / h > 1.25:
                half_width = int(w / 2)
                img_letter_regions.append((x, y, half_width, h))
                img_letter_regions.append((x + half_width, y, half_width, h))
            else:
                img_letter_regions.append((x, y, w, h))

        if len(img_letter_regions) != 4:
            continue

        img_letter_regions = sorted(img_letter_regions, key=lambda x: x[0])

        for letter_b_box, letter_text in zip(img_letter_regions, captcha_text):
            x, y, w, h = letter_b_box
            letter_img = img_gray[y - 2: y + h + 2, x - 2:x + w + 2]
            save_path = os.path.join(OUTPUT_FOLDER, letter_text)
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            count = counts.get(letter_text, 1)
            out_path = os.path.join(save_path, "{}.png".format(str(count).zfill(6)))
            cv2.imwrite(out_path, letter_img)

            counts[letter_text] = count + 1



# auto test
# doctest.testmod()
split_captcha_into_separate_letters()
