import sys
from math import exp
from specrend import spectrum_to_xy, xy_to_rgb, constrain_rgb, norm_rgb

this = sys.modules[__name__]
this.bb_temp = 5000.0    # Hidden temperature argument to bb_spectrum.


def bb_spectrum(wavelength: float) -> float:
    wlm = wavelength * 1e-9   # Wavelength in meters
    return (3.74183e-16 * pow(wlm, -5.0)) / (exp(1.4388e-2 / (wlm * this.bb_temp)) - 1.0)


if __name__ == '__main__':

    print('Temperature       x      y      z       R     G     B')
    print('-----------    ------ ------ ------   ----- ----- -----')

    for t in range(1000, 10200, 500):
        this.bb_temp = t
        xy = spectrum_to_xy(bb_spectrum)
        z = 1.0 - (xy.x + xy.y)
        # noinspection SpellCheckingInspection
        rgb_val = xy_to_rgb('SMPTE', xy)
        print('  %5.0f K      %.4f %.4f %.4f   ' % (t, xy.x, xy.y, z), end='')
        rgb_val, constrained = constrain_rgb(rgb_val)
        if constrained:
            rgb_val = norm_rgb(rgb_val)
            print('%.3f %.3f %.3f (Approximation)' % (rgb_val.r, rgb_val.g, rgb_val.b))
        else:
            rgb_val = norm_rgb(rgb_val)
            print('%.3f %.3f %.3f' % (rgb_val.r, rgb_val.g, rgb_val.b))

