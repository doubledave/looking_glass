root_name = str()
logger_started = False


class GUI:
    """
    A class that serves as a parent to each window/menu/pop-up class
    """

    def get_logger(self, is_root=False):
        import logging
        global logger_started
        if is_root:
            name = root_name
            logger_started = True
        else:
            name = str(f"{root_name}.{self.name}")
            self.logger_started = True
        log = logging.getLogger(name)
        log.debug(f'Logger started for {name}')
        return log

    def __init__(self):
        import PySimpleGUIQt as qt
        import PySimpleGUI as psg
        # Todo:
        #    - Find a way to only load the PSG needed

        # Give the GUI frameworks easily accessible names
        self.qt = qt
        self.psg = psg
        global root_name
        root_name = str(f'LookingGlass.App.{self.__class__.__name__}')

        parent_log = self.get_logger(is_root=True)

    @staticmethod
    def qt():
        """
        This will give sub-classes access to the PySimpleGUIQt library

        :return:
        """
        import PySimpleGUIQt as qt
        return qt

    @staticmethod
    def psg():
        """
        This will give sub-classes access to the PySimpleGUI library

        :return:
        """

        import PySimpleGUI as psg
        return psg

    @staticmethod
    def parent_name():
        return root_name

    @staticmethod
    def top_window(config):
        from .window_models.top_window import TopWindow

        builder = TopWindow(config)

        return builder.top_window

