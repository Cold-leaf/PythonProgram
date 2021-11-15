from PIL import Image
from PIL import ImageEnhance
from typing import *
import numpy as np
from PIL import Image
import cv2
import time

# 计算耗时
def timecost(img1,img2):
    start = time.time()
    save(color_car(img1,img2),"Finally")
    end = time.time()
    print("time cost:"+str(end-start))

# 保存图像
def save(img1_g,filename):
    img1_g.save(filename+".png")

class UI(object):
    def __init__(self):
        self.img1 = Image.open('Import/792edcd3841fc1b85968fd3b534a15638a768a2e.jpg')   # 上层
        self.img2 = Image.open('Import/1b7eb3af49441b6f4ddca0c683873a1aadb71a24.jpg')   # 下层
    def to_fun(self):
        timecost(self.img1, self.img2)

def color_car(
    wimg: Image.Image,
    bimg: Image.Image,
    wlight: float = 1.0,
    blight: float = 0.5,
    wcolor: float = 1,
    bcolor: float = 1,
    chess: bool = False,
) -> Image.Image:
    """
    发彩色车
    :param wimg: 白色背景下的图片
    :param bimg: 黑色背景下的图片
    :param wlight: wimg 的亮度
    :param blight: bimg 的亮度
    :param wcolor: wimg 的色彩保留比例
    :param bcolor: bimg 的色彩保留比例
    :param chess: 是否棋盘格化
    :return: 处理后的图像
    """
    wimg = ImageEnhance.Brightness(wimg).enhance(wlight)
    bimg = ImageEnhance.Brightness(bimg).enhance(blight)

    wimg = wimg.resize((1980, 1280),Image.ANTIALIAS)
    bimg = bimg.resize((1980, 1280),Image.ANTIALIAS)

    wimg, bimg = resize_image(wimg, bimg, "RGB")

    wpix = np.array(wimg).astype("float64")
    bpix = np.array(bimg).astype("float64")

    if chess:
        wpix[::2, ::2] = [255., 255., 255.]
        bpix[1::2, 1::2] = [0., 0., 0.]

    wpix /= 255.
    bpix /= 255.

    wgray = wpix[:, :, 0] * 0.334 + wpix[:, :, 1] * 0.333 + wpix[:, :, 2] * 0.333
    wpix *= wcolor
    wpix[:, :, 0] += wgray * (1. - wcolor)
    wpix[:, :, 1] += wgray * (1. - wcolor)
    wpix[:, :, 2] += wgray * (1. - wcolor)

    bgray = bpix[:, :, 0] * 0.334 + bpix[:, :, 1] * 0.333 + bpix[:, :, 2] * 0.333
    bpix *= bcolor
    bpix[:, :, 0] += bgray * (1. - bcolor)
    bpix[:, :, 1] += bgray * (1. - bcolor)
    bpix[:, :, 2] += bgray * (1. - bcolor)

    d = 1. - wpix + bpix

    d[:, :, 0] = d[:, :, 1] = d[:, :, 2] = d[:, :, 0] * 0.222 + d[:, :, 1] * 0.707 + d[:, :, 2] * 0.071

    p = np.where(d != 0, bpix / d * 255., 255.)
    a = d[:, :, 0] * 255.

    colors = np.zeros((p.shape[0], p.shape[1], 4))
    colors[:, :, :3] = p
    colors[:, :, -1] = a

    colors[colors > 255] = 255

    return Image.fromarray(colors.astype("uint8")).convert("RGBA")

def resize_image(im1: Image.Image, im2: Image.Image, mode: str) -> Tuple[Image.Image, Image.Image]:
    """
    统一图像大小
    """
    _wimg = im1.convert(mode)
    _bimg = im2.convert(mode)

    wwidth, wheight = _wimg.size
    bwidth, bheight = _bimg.size

    width = max(wwidth, bwidth)
    height = max(wheight, bheight)

    _wimg.resize((width,height))
    _bimg.resize((width,height))

    wimg = Image.new(mode, (width, height), 255)
    bimg = Image.new(mode, (width, height), 0)

    wimg.paste(_wimg, ((width - width) // 2, (height - height) // 2))
    bimg.paste(_bimg, ((width - width) // 2, (height - height) // 2))

    return wimg, bimg

if __name__ =='__main__':
    ui=UI()
    ui.to_fun()


