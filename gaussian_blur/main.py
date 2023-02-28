from gauss_blur import *
import cv2


def main():


    image = cv2.imread("/home/oleg/Рабочий стол/signal_processing/picture/picture_ocean.jpeg")

    start_app = GaysBlur()
    start_app.gaussian_blur(image, 5, verbose=True)

if __name__ == '__main__':
    main()

