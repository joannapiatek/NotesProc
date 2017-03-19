import cv2


def binarize_image(img):
    img = cv2.GaussianBlur(img, (7, 7), 0)
    img = cv2.bilateralFilter(img, 3, 75, 75)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)

    low_val = 150;
    ret, binarized_image = cv2.threshold(img, low_val, 255, cv2.THRESH_BINARY)

    # ret, thresh2 = cv2.threshold(img, lowVal, 255, cv2.THRESH_BINARY_INV)
    # ret, thresh3 = cv2.threshold(img, lowVal, 255, cv2.THRESH_TRUNC)
    # ret, thresh4 = cv2.threshold(img, lowVal, 255, cv2.THRESH_TOZERO)
    # ret, thresh5 = cv2.threshold(img, lowVal, 255, cv2.THRESH_TOZERO_INV)
    #
    # titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    # images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    #
    # for i in xrange(6):
    #     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])
    #
    # plt.show()

    cv2.destroyAllWindows()

    return binarized_image
