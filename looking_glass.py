class LookingGlass:
    pass


class App(LookingGlass):
    """
    A class for the main app

    ToDo:
        - add command-line arguments
    """

    def _config_(self):
        from looking_glass.lib import Config
        config = Config()
        conf = Config.config()
        return conf

    def _start_logger_(self):

        import logging
        from colorlog import ColoredFormatter

        formatter = ColoredFormatter(
            "%(bold_cyan)s%(asctime)-s%(reset)s%(log_color)s::%(module)s.%(name)-14s::%(levelname)-10s%(reset)s%(blue)s%(message)-s",
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG': 'bold_cyan',
                'INFO': 'bold_green',
                'WARNING': 'bold_yellow',
                'ERROR': 'bold_red',
                'CRITICAL': 'bold_red',
            }
        )
        name = str(f'LookingGlass.{self.__class__.__name__}')
        logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        logger.info(f'Logger started for %s' % name)
        return logger

    def __init__(self):
        self.log = self._start_logger_()
        from looking_glass.lib import Config

        self.conf = Config()
        self.conf
        self.run()

    # noinspection SpellCheckingInspection
    def run(self, ):
        from looking_glass.lib import GUI



        log = self.log

        log.debug('Getting TopWindow')
        top_window = GUI.top_window(self._config_).window

        log.debug('Instantiating TopWindow')

        log.debug("Setting all other windows to inactive")
        opts_win_active = False

        log.debug('Show window!')

        units = config.get('sense_customize', 'dsp_temp')  # dsp = display

        while True:
            event, values = top_window.read(timeout=100)
            if event is None or event == 'top_win_exit':
                log.info('User indicated a desire to exit.')
                exit()

            # If the options window isn't already active and the user hit Settings on the main window then read the
            # options window and wait for the user to do something else.
            if not opts_win_active and event == 'Settings::_SETTINGS_BUTTON_':
                log.info('User indicated a desire to enter the Settings menu')

                log.debug('Preparing window')
                from looking_glass.lib import OptsWindow
                opts_win_active = True
                log.debug('Options Window set to active.')
                log.debug('Calling Options Window builder')
                log.debug(f'Passing builder a config with these sections {config.sections()}')
                opts_builder = OptsWindow(config=config)
                opts_win = opts_builder.window

            # Read the window and wait for event
            counter = 0
            while opts_win_active:
                event2, values2 = opts_win.read(timeout=100)

                # If the user presses the X button or presses 'cancel' the options window will close.
                if event2 is None or event2 == 'opts_win_cancel':
                    log.debug('User cancelled or closed window')
                    log.debug('Closing Options Window, ignoring changes')
                    opts_win.close()
                    opts_win_active = False
                    log.debug('Options window closed and set to inactive status. No changes saved.')

                # If the user presses 'OK' we call on the Config class to write the current config to a file
                if event2 == 'opts_win_ok':
                    log.debug('User indicated a desire to exit the config window')

                    from looking_glass.lib import Config
                    Config.write(config)

                # If the user presses 'Test Key' we test their API key
                if event2 == 'check_api_key':
                    import PySimpleGUI as gui
                    eprint = gui.EasyPrint()
                    eprint('Checking API key!')


if __name__ == "__main__":
    app = App()
else:
    print('Being imported, but not running __init__')
