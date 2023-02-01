import cv2
from search_stamp import colored_mask, get_circle


def get_stamp_answer(a, b, r, h, w):
    x_1 = round(int(a - r) / w, 3)
    x_2 = round(int(a + r) / w, 3)
    y_1 = round(int(b - r) / h, 3)
    y_2 = round(int(b + r) / h, 3)
    coordinates = {'coordinates': {
        'stamp': [
            [x_1, y_1],
            [x_2, y_1],
            [x_2, y_2],
            [x_1, y_2]
        ]
    }
    }

    return coordinates


def birth_face(path_to_file):
    img_rgb = cv2.imread(path_to_file)
    h, w = img_rgb.shape[:2]
    crop_img = img_rgb[h // 3 * 2:h, 0:w // 2]
    dst = colored_mask(crop_img)
    a, b, r = get_circle(dst, crop_img, w*0.07, h*0.12)

    b += h // 3 * 2

    coordinates = get_stamp_answer(a, b, r, h, w)

    return coordinates


def birth_back(path_to_file):
    img_rgb = cv2.imread(path_to_file)
    h, w = img_rgb.shape[:2]
    crop_img = img_rgb[h // 3:h // 3 * 2, 0:w // 2]
    dst = colored_mask(crop_img)
    a, b, r = get_circle(dst, crop_img, w*0.07, h*0.12)

    b += h // 3
    coordinates = get_stamp_answer(a, b, r, h, w)

    return coordinates


def mvd(path_to_file):
    img_rgb = cv2.imread(path_to_file)
    h, w = img_rgb.shape[:2]
    crop_img = img_rgb[h // 4 * 3:h, w // 5:w // 4 * 3]
    dst = colored_mask(crop_img)
    a, b, r = get_circle(dst, crop_img, w*0.05, w*0.11)

    a += w // 5
    b += h // 4 * 3

    coordinates = get_stamp_answer(a, b, r, h, w)

    return coordinates


def mvd_back(path_to_file):
    img_rgb = cv2.imread(path_to_file)
    h, w = img_rgb.shape[:2]
    crop_img = img_rgb[h // 2:h // 6 * 5, 0:w // 4 * 3]
    dst = colored_mask(crop_img)
    a, b, r = get_circle(dst, crop_img, w * 0.07, h * 0.12)

    b += h // 2

    coordinates = get_stamp_answer(a, b, r, h, w)

    return coordinates


def sort_func(doc_type, doc):

    if doc_type == 'birth_face':
        result = birth_face(doc)

    elif doc_type == 'birth_back':
        result = birth_back(doc)

    elif doc_type == 'mvd':
        result = mvd(doc)

    elif doc_type == 'mvd_back':
        result = mvd_back(doc)

    return result
