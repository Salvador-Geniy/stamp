import cv2
from search_stamp import colored_mask, get_circle


def birth_face(path_to_file):
    img_rgb = cv2.imread(path_to_file)
    h, w = img_rgb.shape[:2]
    crop_img = img_rgb[h // 3 * 2:h, 0:w // 2]
    dst = colored_mask(crop_img)
    a, b, r = get_circle(dst, crop_img, h, w)

    b += h // 3 * 2
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


def birth_back(path_to_file):
    img_rgb = cv2.imread(path_to_file)
    h, w = img_rgb.shape[:2]
    crop_img = img_rgb[h // 3:h // 3 * 2, 0:w // 2]
    dst = colored_mask(crop_img)
    a, b, r = get_circle(dst, crop_img, h, w)

    b += h // 3
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


def sertificate_face():
    pass


def sertificate_back():
    pass


def sort_func(doc_type, doc):

    if doc_type == 'rus_birth_certificate_new':
        result = birth_face(doc)

    # elif doc_type == 'apostille_zags':
    #     result = birth_back(doc)

    return result
