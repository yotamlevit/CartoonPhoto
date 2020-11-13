"""
CartoonPhoto
Yotam Levit
Date: 13/11/2020
"""
import cv2


def read_image(image_name):
    return cv2.imread(image_name)


def get_edged(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grey = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)
    return edges


def cartoonization(image, edges):
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


def show_images(image, edges, cartoon):
    cv2.imshow("Image" ,image)
    cv2.imshow("edges", edges)
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convert(image_name):
    image = read_image(image_name)
    edges = get_edged(image)
    cartoon = cartoonization(image, edges)
    show_images(image, edges, cartoon)

convert("dana4.png")