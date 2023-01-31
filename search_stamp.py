import cv2
import numpy as np


def colored_mask(img, threshold=-1):
    # Denoise picture.
    denoised = cv2.medianBlur(img, 3)

    # Create GRAY.
    gray = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)

    # Create mask.
    adaptiveThreshold = threshold if threshold >= 0 else cv2.mean(img)[0]
    color = cv2.cvtColor(denoised, cv2.COLOR_BGR2HLS)
    mask = cv2.inRange(color, (0, int(adaptiveThreshold / 6), 60), (180, adaptiveThreshold, 255))

    # Create mask of color part of picture.
    dst = cv2.bitwise_and(gray, gray, mask=mask)

    return dst


def get_circle(gray_blurred, img, h, w):
    # coordinates = {}
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=20,
                                        param2=10, minRadius=round(w * 0.07), maxRadius=round(h * 0.12))

    # Draw rectangle that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for (a, b, r) in detected_circles[0, :]:
            r += 5
            # Draw the rectangle of the circle.
            cv2.rectangle(img, (a - r, b - r), (a + r, b + r), (0, 255, 0), 4)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            cv2.imshow("Detected Circle", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return a, b, r