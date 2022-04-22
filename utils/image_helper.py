import cv2 
import numpy as np

class ImgHelper():

    @classmethod
    def ipc_white_balance_color(cls, image):
        # 读取图像
        r, g, b = cv2.split(image)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]

        if r_avg != 0.0 and g_avg != 0.0 and b_avg != 0.0:
            # 求各个通道所占增益
            k = (r_avg + g_avg + b_avg) / 3
            kr = k / r_avg
            kg = k / g_avg
            kb = k / b_avg
            r = cv2.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
            g = cv2.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
            b = cv2.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
        image_wb = cv2.merge([b, g, r])
        return image_wb

    @classmethod
    def ipc_equalizeHist_color(cls, image):
        b, g, r = cv2.split(image)
        
        b1 = cv2.equalizeHist(b)
        g1 = cv2.equalizeHist(g)
        r1 = cv2.equalizeHist(r)
        
        output = cv2.merge([b1,g1,r1])
        return output

    @classmethod
    def ipc_sharpen_color(cls, img_src):
        img_blur = cv2.GaussianBlur(img_src, (0, 0), 5)
        img_usm = cv2.addWeighted(img_src, 1.5, img_blur, -0.5, 0)
        return img_usm

    @classmethod
    def ipc_normalize_color(cls, img_src):
        dst = np.zeros_like(img_src)
        cv2.normalize(img_src, dst, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)   
        return dst

