#!/usr/bin/env python

import logging
logger = logging.getLogger(__name__)

#IMGS_FOLDER = "_gen_render_m00c000"
#IMGS_FOLDER = "_gen_render_it0"
IMGS_FOLDER = "_gen_render_it1"

def gen_mp4():
    import os
    from utils.mp4_maker import Mp4Maker

    dir_root = os.getcwd()

    src_dir = "{}/{}".format(dir_root, IMGS_FOLDER)
    dst_dir = "{}/_gen_render_mp4".format(dir_root)
    os.makedirs(dst_dir, exist_ok=True)

    src_name = IMGS_FOLDER.replace("_gen_render", "")

    if not os.path.isdir(src_dir):
        logger.error("{} not exist, abort".format(src_dir))
        return

    filenames = Mp4Maker.get_sorted_img_files(src_dir)
    mp4_filename = Mp4Maker.create_mp4_file(dst_dir, filenames, src_name, fps=24.0)
    logger.info("\nmp4 generated: {}\n".format(mp4_filename))


if __name__ == '__main__':
    import coloredlogs
    logging.getLogger().setLevel(logging.INFO)
    coloredlogs.install(fmt='%(asctime)s %(levelname)s %(message)s @%(name)s')

    gen_mp4()


#!/bin/bash
#ffmpeg -framerate 24 -i _gen_render_little_star/20220306_%06d.png output.mp4
