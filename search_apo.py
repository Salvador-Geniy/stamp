import cv2


def apo_mask(crop_img):
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    edged = cv2.Canny(gray, 280, 300)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    return closed


def get_contour(crop_img):
    closed = apo_mask(crop_img)
    contours, _ = cv2.findContours(closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=lambda q: cv2.contourArea(q), reverse=True)
    for c in contours[:1]:
        # Find width, height
        rect = cv2.boundingRect(c)
        w_apo, h_apo = rect[2:]

        # Find center of contour
        m = cv2.moments(c)
        if m['m00'] != 0.0:
            a = int(m['m10'] / m['m00'])
            b = int(m['m01'] / m['m00'])

    return a, b, w_apo, h_apo
