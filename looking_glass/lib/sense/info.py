
class SenseInfo(object):

    def __init__(self):
        import logging
        self.log = logging.getLogger(__name__)

    @staticmethod
    def _get_device_():
        """
        Instantiate the sense-hat and return an instance to the worker
        :return:
        """
        try:
            from sense_hat import SenseHat
        except ModuleNotFoundError:
            from sense_emu import SenseHat
        finally:
            sense = SenseHat()
        return sense

    @staticmethod
    def convert_temp(temp):
        f = (temp * 9/5) + 32

        return f

    def get_temp(self, raw=True):
        sense = self._get_device_()
        temp = sense.temperature
        if raw:
            pass
        else:
            temp = str(sense.temperature) + ' °C'

        return temp

    def get_temp_f(self):
        rounded = round(self.convert_temp(self.get_temp()))
        temp = str(rounded) + ' °F'

        return temp

    def get_humidity(self):
        sense = self._get_device_()
        sense.show_message('Getting Humidity')

        return sense.humidity

    def get_pressure(self):
        sense = self._get_device_()
        pres = sense.pressure
        pres = round(pres)

        pres = str(pres)

        return pres

