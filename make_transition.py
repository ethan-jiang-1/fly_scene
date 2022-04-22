import logging 
import cv2
import os
import numpy as np

from utils.plot_helper import PlotHelper
from utils.image_helper import ImgHelper

logger = logging.getLogger(__name__)

class ImageTransision():
    def __init__(self, img0, img1, frame_no=255):
        self.img0 = img0
        self.img1 = img1
        self.frame_no = frame_no

    def make_transfer(self, dir_dst):
        os.makedirs(dir_dst, exist_ok=True)

        img0_float = self.img0.astype("float")
        img1_float = self.img1.astype("float")

        fnum = self.frame_no
        for ndx in range(fnum):
            img_trans = np.zeros_like(self.img0)
            img_trans_float = img_trans.astype("float")

            ratio_0 = (fnum - ndx)/fnum 
            ratio_1 = (ndx)/fnum

            img_trans_float += img0_float * ratio_0
            img_trans_float += img1_float * ratio_1

            img_trans_float -= img_trans_float.min()
            img_trans_float /= img_trans_float.max()
            img_trans_float *= 255

            img_trans = img_trans_float.astype("uint8")

            filename = "{}/image_{:03d}.png".format(dir_dst, ndx)
            cv2.imwrite(filename, img_trans)
            logger.info("{} saved".format(filename))


def gen_transition():
    filename0 = "data/picture_trans_0.jpeg"
    filename1 = "data/picture_trans_1.jpeg"

    img0 = cv2.imread(filename0, cv2.IMREAD_COLOR)
    img1 = cv2.imread(filename1, cv2.IMREAD_COLOR)

    dsize = (640, 640)

    img0 = cv2.resize(img0, dsize)
    img1 = cv2.resize(img1, dsize)

    logger.info(img0.shape)
    logger.info(img1.shape)

    PlotHelper.plot_imgs([ImgHelper.ipc_white_balance_color(img0), ImgHelper.ipc_white_balance_color(img1)])

    it = ImageTransision(img0, img1)
    it.make_transfer("_gen_render_it0")

if __name__ == '__main__':
    import coloredlogs
    logging.getLogger().setLevel(logging.INFO)
    coloredlogs.install(fmt='%(asctime)s %(levelname)s %(message)s @%(name)s')

    gen_transition()
