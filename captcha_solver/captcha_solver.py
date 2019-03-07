import cv2
import numpy as np
import imutils
from pytesseract import image_to_string
import re


def __get_angled_rect(x0, y0, width, height, angle):
    """
Return rotated rectangle coordinates
    :param x0: center of the rectangle on horizontal axis
    :param y0: center of the rectangle on vertical axis
    :param width: width of the rectangle
    :param height: haighr of the rectangle
    :param angle: angle of the rectangle
    :return: list of four points of the rectangle grouped in tuples
    """
    _angle = angle * np.pi / 180.0
    b = np.cos(_angle) * 0.5
    a = np.sin(_angle) * 0.5
    pt0 = (int(x0 - a * height - b * width),
           int(y0 + b * height - a * width))
    pt1 = (int(x0 + a * height - b * width),
           int(y0 - b * height - a * width))
    pt2 = (int(2 * x0 - pt0[0]), int(2 * y0 - pt0[1]))
    pt3 = (int(2 * x0 - pt1[0]), int(2 * y0 - pt1[1]))

    return [pt0, pt1, pt2, pt3]


def __detect_angle(img):
    """
    Function try to detect an angle of the text by looking for the most white zone (bar-shaped) above the text.
    We turn around bar-mask and calculating histogram (of white specter) of this bar,
    gradually down this bar along the vertical axis at the center of the image
    The angle of the whitest bar - is the text orientation angle (in 95% cases)
    :param img:
    :return:
    """
    #

    h, w, *_ = img.shape
    bar_len = int(0.8 * w)
    bar_width = 10
    r_angle = -1
    r_hist = 0

    for h1 in range(40, h - 40, 1):
        for angle in range(-45, 45, 1):
            mask = np.zeros((w, h), np.uint8)
            pts = __get_angled_rect(w / 2, h1, bar_len, bar_width, angle)
            npts = np.array([pts], dtype=np.int32)
            cv2.fillPoly(mask, npts, 255)
            hist = cv2.calcHist([img], [0], mask, [1], [230, 256])

            if r_hist < hist[-1]:
                r_hist = hist[-1]
                r_angle = angle

    return -r_angle


def __rotate_crop_ocr(img, angle, lang, show_image=False):
    rotated = imutils.rotate_bound(img, angle) if angle != 0 else img.copy()
    h, w = img.shape
    hr, wr = rotated.shape
    cropped = rotated[hr // 2 - 25:hr // 2 + 50, wr // 2 - w // 2:wr // 2 + w // 2]

    if show_image:
        cv2.imshow('Cropped captcha', cropped)
        if 27 == cv2.waitKey(10):
            cv2.destroyAllWindows()
            exit()

    return (image_to_string(cropped, lang=lang,
                            config='--psm 8 --oem 3 tessedit_char_whitelist=0123456789'),
            cropped)


def solve_captcha(filename, show_image=False, lang='hat'):
    img = cv2.imread(filename)
    if show_image:
        cv2.imshow('Captcha', img)
        if 27 == cv2.waitKey(10):
            cv2.destroyAllWindows()
            exit()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((2, 2), np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=1)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    angle = __detect_angle(thresh)

    res, cropped = __rotate_crop_ocr(gray, angle, lang, show_image=show_image)
    res = re.sub(r'[^\d]', '', res)
    if len(res) != 6:
        res = False

    return res
