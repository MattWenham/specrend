from collections import namedtuple
from typing import Tuple, Callable

rgb = namedtuple('rgb', 'r g b')
colour_point = namedtuple('colour_point', 'x y')

illuminantC: colour_point = colour_point(0.3101, 0.3162)
illuminantD65: colour_point = colour_point(0.3127, 0.3291)
illuminantE: colour_point = colour_point(0.33333333, 0.33333333)

colour_system = namedtuple('colour_point', 'red green blue white gamma')
GAMMA_REC709 = 0
CC = 0.018

cie_colour_match = (
    (0.0014, 0.0000, 0.0065), (0.0022, 0.0001, 0.0105), (0.0042, 0.0001, 0.0201),
    (0.0076, 0.0002, 0.0362), (0.0143, 0.0004, 0.0679), (0.0232, 0.0006, 0.1102),
    (0.0435, 0.0012, 0.2074), (0.0776, 0.0022, 0.3713), (0.1344, 0.0040, 0.6456),
    (0.2148, 0.0073, 1.0391), (0.2839, 0.0116, 1.3856), (0.3285, 0.0168, 1.6230),
    (0.3483, 0.0230, 1.7471), (0.3481, 0.0298, 1.7826), (0.3362, 0.0380, 1.7721),
    (0.3187, 0.0480, 1.7441), (0.2908, 0.0600, 1.6692), (0.2511, 0.0739, 1.5281),
    (0.1954, 0.0910, 1.2876), (0.1421, 0.1126, 1.0419), (0.0956, 0.1390, 0.8130),
    (0.0580, 0.1693, 0.6162), (0.0320, 0.2080, 0.4652), (0.0147, 0.2586, 0.3533),
    (0.0049, 0.3230, 0.2720), (0.0024, 0.4073, 0.2123), (0.0093, 0.5030, 0.1582),
    (0.0291, 0.6082, 0.1117), (0.0633, 0.7100, 0.0782), (0.1096, 0.7932, 0.0573),
    (0.1655, 0.8620, 0.0422), (0.2257, 0.9149, 0.0298), (0.2904, 0.9540, 0.0203),
    (0.3597, 0.9803, 0.0134), (0.4334, 0.9950, 0.0087), (0.5121, 1.0000, 0.0057),
    (0.5945, 0.9950, 0.0039), (0.6784, 0.9786, 0.0027), (0.7621, 0.9520, 0.0021),
    (0.8425, 0.9154, 0.0018), (0.9163, 0.8700, 0.0017), (0.9786, 0.8163, 0.0014),
    (1.0263, 0.7570, 0.0011), (1.0567, 0.6949, 0.0010), (1.0622, 0.6310, 0.0008),
    (1.0456, 0.5668, 0.0006), (1.0026, 0.5030, 0.0003), (0.9384, 0.4412, 0.0002),
    (0.8544, 0.3810, 0.0002), (0.7514, 0.3210, 0.0001), (0.6424, 0.2650, 0.0000),
    (0.5419, 0.2170, 0.0000), (0.4479, 0.1750, 0.0000), (0.3608, 0.1382, 0.0000),
    (0.2835, 0.1070, 0.0000), (0.2187, 0.0816, 0.0000), (0.1649, 0.0610, 0.0000),
    (0.1212, 0.0446, 0.0000), (0.0874, 0.0320, 0.0000), (0.0636, 0.0232, 0.0000),
    (0.0468, 0.0170, 0.0000), (0.0329, 0.0119, 0.0000), (0.0227, 0.0082, 0.0000),
    (0.0158, 0.0057, 0.0000), (0.0114, 0.0041, 0.0000), (0.0081, 0.0029, 0.0000),
    (0.0058, 0.0021, 0.0000), (0.0041, 0.0015, 0.0000), (0.0029, 0.0010, 0.0000),
    (0.0020, 0.0007, 0.0000), (0.0014, 0.0005, 0.0000), (0.0010, 0.0004, 0.0000),
    (0.0007, 0.0002, 0.0000), (0.0005, 0.0002, 0.0000), (0.0003, 0.0001, 0.0000),
    (0.0002, 0.0001, 0.0000), (0.0002, 0.0001, 0.0000), (0.0001, 0.0000, 0.0000),
    (0.0001, 0.0000, 0.0000), (0.0001, 0.0000, 0.0000), (0.0000, 0.0000, 0.0000)
)

# noinspection PyPep8
colour_sys_dict = {
    "NTSC": colour_system(colour_point(0.67, 0.33), colour_point(0.21, 0.71)
                          , colour_point(0.14, 0.08), illuminantC, GAMMA_REC709)
    ,
    "EBU": colour_system(colour_point(0.64, 0.33), colour_point(0.29, 0.60)
                         , colour_point(0.15, 0.06), illuminantD65, GAMMA_REC709)
    ,
    "SMPTE": colour_system(colour_point(0.630, 0.340), colour_point(0.310, 0.595)
                           , colour_point(0.155, 0.070), illuminantD65, GAMMA_REC709)
    ,
    "HDTV": colour_system(colour_point(0.670, 0.330), colour_point(0.210, 0.710)
                          , colour_point(0.150, 0.060), illuminantD65, GAMMA_REC709)
    ,
    "CIE": colour_system(colour_point(0.7355, 0.2645), colour_point(0.2658, 0.7243)
                         , colour_point(0.1669, 0.0085), illuminantE, GAMMA_REC709)
    ,
    "CIE REC 709": colour_system(colour_point(0.64, 0.33), colour_point(0.30, 0.60)
                                 , colour_point(0.15, 0.06), illuminantD65, GAMMA_REC709)
}


def upvp_to_xy(up: float, vp: float) -> colour_point:
    # noinspection PyPep8
    return colour_point((9 * up) / ((6 * up) - (16 * vp) + 12),
                        (4 * vp) / ((6 * up) - (16 * vp) + 12)
                        )


def xy_to_upvp(xy: colour_point) -> Tuple[float, float]:
    return ((4 * xy.x) / ((-2 * xy.x) + (12 * xy.y) + 3),
            (9 * xy.y) / ((-2 * xy.x) + (12 * xy.y) + 3))


def xy_to_rgb(cs_name: str, xy: colour_point) -> rgb:
    colour_sys = colour_sys_dict[cs_name]
    # Colour System z-values
    zr = 1 - (colour_sys.red.x + colour_sys.red.y)
    zg = 1 - (colour_sys.green.x + colour_sys.green.y)
    zb = 1 - (colour_sys.blue.x + colour_sys.blue.y)
    zw = 1 - (colour_sys.white.x + colour_sys.white.y)

    # xyz -> rgb matrix, before scaling to white.

    rx = (colour_sys.green.y * zb) - (colour_sys.blue.y * zg)
    ry = (colour_sys.blue.x * zg) - (colour_sys.green.x * zb)
    rz = (colour_sys.green.x * colour_sys.blue.y) - (colour_sys.blue.x * colour_sys.green.y)

    gx = (colour_sys.blue.y * zr) - (colour_sys.red.y * zb)
    gy = (colour_sys.red.x * zb) - (colour_sys.blue.x * zr)
    gz = (colour_sys.blue.x * colour_sys.red.y) - (colour_sys.red.x * colour_sys.blue.y)

    bx = (colour_sys.red.y * zg) - (colour_sys.green.y * zr)
    by = (colour_sys.green.x * zr) - (colour_sys.red.x * zg)
    bz = (colour_sys.red.x * colour_sys.green.y) - (colour_sys.green.x * colour_sys.red.y)

    # White scaling factors.
    # Dividing by colour_sys.white.y scales the white luminance to unity, as conventional.

    rw = ((rx * colour_sys.white.x) + (ry * colour_sys.white.y) + (rz * zw)) / colour_sys.white.y
    gw = ((gx * colour_sys.white.x) + (gy * colour_sys.white.y) + (gz * zw)) / colour_sys.white.y
    bw = ((bx * colour_sys.white.x) + (by * colour_sys.white.y) + (bz * zw)) / colour_sys.white.y

    # xyz -> rgb matrix, correctly scaled to white.

    rx = rx / rw
    ry = ry / rw
    rz = rz / rw

    gx = gx / gw
    gy = gy / gw
    gz = gz / gw

    bx = bx / bw
    by = by / bw
    bz = bz / bw

    # rgb of the desired point

    zc = 1 - (xy.x + xy.y)

    return rgb(
        (rx * xy.x) + (ry * xy.y) + (rz * zc),
        (gx * xy.x) + (gy * xy.y) + (gz * zc),
        (bx * xy.x) + (by * xy.y) + (bz * zc)
    )


def inside_gamut(rgb_in: rgb) -> bool:
    return all((rgb_in.r >= 0.0, rgb_in.g >= 0.0, rgb_in.b >= 0.0))


def constrain_rgb(rgb_in: rgb) -> Tuple[rgb, bool]:
    # Amount of white needed is w = - min(0, *r, *g, *b) */
    w = -min(rgb_in.r, rgb_in.g, rgb_in.b, 0)

    if w > 0:
        return rgb(rgb_in.r + w, rgb_in.g + w, rgb_in.b + w), True
    else:
        return rgb_in, False


def gamma_correct_rgb(cs_name: str, rgb_in: rgb) -> rgb:
    def gamma_correct(cs_name: str, c: float) -> float:
        colour_sys = colour_sys_dict[cs_name]
        gamma = colour_sys.gamma
        if gamma == GAMMA_REC709:
            # Rec. 709 gamma correction.
            if c < CC:
                return ((1.099 * pow(CC, 0.45)) - 0.099) / CC
            else:
                return (1.099 * pow(c, 0.45)) - 0.099
        else:
            # Nonlinear colour = (Linear colour)^(1/gamma)
            return pow(c, 1.0 / gamma)

    return rgb(
        gamma_correct(cs_name, rgb_in.r),
        gamma_correct(cs_name, rgb_in.g),
        gamma_correct(cs_name, rgb_in.b)
    )


def norm_rgb(rgb_in: rgb) -> rgb:
    greatest = max(rgb_in.r, rgb_in.g, rgb_in.b)
    return rgb(rgb_in.r / greatest, rgb_in.g / greatest, rgb_in.b / greatest)


def spectrum_to_xy(spec_intens: Callable[[float], float]) -> colour_point:
    λ = 380
    x = y = z = 0.0
    for i in range(81):
        me = spec_intens(λ)
        x += me * cie_colour_match[i][0]
        y += me * cie_colour_match[i][1]
        z += me * cie_colour_match[i][2]
        λ += 5
    xyz = x + y + z
    return colour_point(x / xyz, y / xyz)
