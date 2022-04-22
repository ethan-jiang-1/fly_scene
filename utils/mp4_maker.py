import os
import logging
logger = logging.getLogger(__name__)

class Mp4Maker(object):
    @classmethod
    def get_sorted_img_files(cls, src_dir):
        names = os.listdir(src_dir)

        filenames = []
        for name in names:
            if not (name.endswith(".jpg") or name.endswith(".png")):
                continue
            filename = "{}{}{}".format(src_dir, os.sep, name)
            filenames.append(filename)
        return sorted(filenames)

    @classmethod
    def get_resolution(cls, filename0):
        import cv2
        img = cv2.imread(filename0, cv2.IMREAD_COLOR)
        resolution = (img.shape[0], img.shape[1])
        return resolution

    @classmethod
    def create_mp4_file(cls, dst_dir, filenames, src_name, fps=24.0):
        import cv2
        output_pathname = "output{}.mp4".format(src_name)
        dst_path = "{}{}{}".format(dst_dir, os.sep, output_pathname)
        if os.path.isfile(dst_path):
            os.unlink(dst_path)

        resolution = cls.get_resolution(filenames[0])

        #fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #out = cv2.VideoWriter(dst_path, fourcc, fps, resolution)

        #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        #out = cv2.VideoWriter('output.mp4', fourcc, 20.0, resolution)

        fourcc = cv2.VideoWriter_fourcc(*'X264')
        out = cv2.VideoWriter(dst_path, fourcc, fps, resolution)

        for idx, filename in enumerate(filenames):
            logger.info("add {}:{} into video".format(idx, filename))
            img = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)
            out.write(img)

        out.release()
        logger.info("found output here: {}".format(dst_path))
        logger.info("mp4 length:   \t{:.2f}sec".format(len(filenames)/24))
        logger.info("mp4 filesize: \t{:.2f}kbytes".format(os.path.getsize(dst_path)/1024))
        return dst_path
