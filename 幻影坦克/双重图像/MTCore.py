


def color_car(
    wimg: Image.Image,
    bimg: Image.Image,
    wlight: float = 1.0,
    blight: float = 0.18,
    wcolor: float = 0.5,
    bcolor: float = 0.7,
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



