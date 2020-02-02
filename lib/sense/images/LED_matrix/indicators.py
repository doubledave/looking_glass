"""
This module contains the definitions of the indicators presented through the SenseHat's LED Matrix.

Available Indicators:

success
checking
fail

"""


def fail():
    O = [0, 0, 255]
    X = [255, 0, 0]
    img = [
        X, O, O, O, O, O, O, X,
        O, X, O, O, O, O, X, O,
        O, O, X, O, O, X, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, X, O, O, O, O, X, O,
        X, O, O, O, O, O, O, X
    ]

    return img


def success():
    """

        A check-mark image for indicating that the system succeeded in it's last query to the sensors

        :return:

    """

    X = [0, 255, 0]
    O = [0, 0, 255]

    img = [
        O, O, O, O, O, O, O, X,
        O, O, O, O, O, O, X, O,
        O, O, O, O, O, X, O, O,
        X, O, O, O, X, O, O, O,
        O, X, O, X, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]

    return img


def checking():
    """
        A question mark image for indicating a user prompt or to flash and indicate that the system is working.
    """
    X = [0, 100, 100]
    O = [0, 0, 255]
    img = [
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, O, O, O, O
    ]

    return img


class Indicators(object):

    def __init__(self):
        self.checking = checking()
        self.success = success()
        self.fail = fail()

    @staticmethod
    def flash(img):
        import time
        from sense_emu import SenseHat

        sense = SenseHat()

        for i in range(3):
            sense.set_pixels(pixel_list=img)
            print('Flash')
            time.sleep(0.5)
            sense.clear()
            time.sleep(0.5)
