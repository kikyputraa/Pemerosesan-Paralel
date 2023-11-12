import cv2
import numpy as np
import requests
from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)
    img = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    return img

def image_stitching(images, crop):
    print("[INFO] stitching images...")
    stitcher = cv2.createStitcher() if cv2.__version__.startswith('3') else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    if status == 0:
        if crop > 0:
            print("[INFO] cropping...")
            stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0, 0, 0))

            gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            c = max(cnts, key=cv2.contourArea)

            mask = np.zeros(thresh.shape, dtype="uint8")
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

            minRect = mask.copy()
            sub = mask.copy()

            while cv2.countNonZero(sub) > 0:
                minRect = cv2.erode(minRect, None)
                sub = cv2.subtract(minRect, thresh)

            cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            c = max(cnts, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(c)

            stitched = stitched[y:y + h, x:x + w]

        return stitched

    else:
        print("[INFO] image stitching failed ({})".format(status))
        return None

if __name__ == "__main__":
    image_urls = [
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/1.png',
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/2.png',
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/3.png',
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/4.png',
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/5.png',
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/6.png',
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/7.png',
        'https://raw.githubusercontent.com/kaliadi/image-Stiching/main/8.png',
    ]

    images = [load_image_from_url(url) for url in image_urls]

    result = image_stitching(images, 1)

    if result is not None:
        cv2.imwrite('output.png', result)
        cv2.imshow("Stitched", result)
        cv2.waitKey(0)
    else:
        print("[INFO] Stitching failed.")
