import cv2
import numpy as np

class OpenCVBasic:
    def __init__(self, image):
        self.image = image

    def read_image(self):
        return cv2.imread(self.image)

    def display_image(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def convert_to_gray(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def convert_to_hsv(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def convert_to_rgb(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

    def resize_image(self, width, height):
        return cv2.resize(self.image, (width, height), interpolation=cv2.INTER_AREA)

    def crop_image(self, x1, y1, x2, y2):
        return self.image[y1:y2, x1:x2]

    def draw_rectangle(self, x1, y1, x2, y2):
        return cv2.rectangle(self.image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    def draw_circle(self, x, y, radius):
        return cv2.circle(self.image, (x, y), radius, (0, 0, 255), 3)

    def draw_line(self, x1, y1, x2, y2):
        return cv2.line(self.image, (x1, y1), (x2, y2), (255, 0, 0), 3)

    def draw_text(self, text, x, y):
        return cv2.putText(self.image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    def save_image(self, filename):
        cv2.imwrite(filename, self.image)

    def show_image(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_gray_image(self):
        cv2.imshow('gray_image', self.convert_to_gray())
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_hsv_image(self):
        cv2.imshow('hsv_image', self.convert_to_hsv())
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_rgb_image(self):
        cv2.imshow('rgb_image', self.convert_to_rgb())
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_resized_image(self, width, height):
        cv2.imshow('resized_image', self.resize_image(width, height))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    image = 'image.jpg'
    opencv = OpenCVBasic(image)
    opencv.show_image()
    opencv.show_gray_image()
    opencv.show_hsv_image()
    opencv.show_rgb_image()
    opencv.show_resized_image(200, 200)