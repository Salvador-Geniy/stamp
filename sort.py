import cv2
from search_stamp import colored_mask, get_circle
from search_apo import get_contour


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


def add_apo_answer(a, b, w_apo, h_apo, w_doc, h_doc):
    x_1 = round((a - w_apo / 2) / w_doc, 3)
    x_2 = round((a + w_apo / 2) / w_doc, 3)
    y_1 = round((b - h_apo / 2) / h_doc, 3)
    y_2 = round((b + h_apo / 2) / h_doc, 3)

    return [[x_1, y_1], [x_2, y_1], [x_2, y_2], [x_1, y_2]]




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


def mvd_back_stamp(image, h, w):
    crop_img = image[h // 2:h // 6 * 5, 0:w // 4 * 3]

    # Set maximum of brightness
    hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = 200
    crop_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    dst = colored_mask(crop_img)
    a, b, r = get_circle(dst, crop_img, w * 0.07, h * 0.12)

    b += h // 2

    coordinates = get_stamp_answer(a, b, r, h, w)

    return coordinates


def mvd_back_apo(image, h_doc, w_doc):
    crop_img = image[h_doc // 5:h_doc // 4 * 3, 0:w_doc]
    a, b, w_apo, h_apo = get_contour(crop_img)
    apo_coordinates = add_apo_answer(a, b, w_apo, h_apo, w_doc, h_doc)

    return apo_coordinates


def mvd_back(path_to_file):
    image = cv2.imread(path_to_file)
    h, w = image.shape[:2]
    coordinates = mvd_back_stamp(image, h, w)
    coordinates['coordinates']['apostille'] = mvd_back_apo(image, h, w)

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

    else:
        result = 'Wrong type of file! Please check your request details.'

    return result
