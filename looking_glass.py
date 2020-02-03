class LookingGlass:
    pass


class App(LookingGlass):
    """
    A class for the main app

    """

    def __init__(self):
        import argparse

        parser = argparse.ArgumentParser()

        parser.add_argument("-v", "--verbose", help="The program will deliver all info that it thinks is helpful."
                                                    " Most of it is not (unless you're a dev).",
                            action="store_true")

        parser.add_argument('-d', '--dev', help="Enables 'dev-mode' for the program. This will disable some checks."
                                                " It will also enable the debug logs to be output to console.",
                            action='store_true')

        parser.add_argument('-g', '--gui', help="Starts the program in GUI mode", action="store_true")

        parser.add_argument('-q', '--quiet', help="Suppresses all log output with level assignments that fall below the"
                                                  " CRITICAL level. This means that WARNINGS will be suppressed! ",
                            action="store_true")

        args = parser.parse_args()

        # Exit after parsing arguments and 'help' was included, but after the help info is delivered
        #
        # This is so the program will stop operating at this point and will not import anything or waste any
        # time/resources
        if args.gui:
            print('Not yet implemented')
        import looking_glass
        log = looking_glass.start_logger(dev=True)
        config = looking_glass.configure()
        sep = ', '
        log.debug(f"Received parsed data with sections: '{sep.join(config.sections())}'")

        self.log = log
        self.args = args
        self.config = config

    def run(self):
        from looking_glass.lib.gui import GUI
        log = self.log

        log.debug('Starting GUI')
        GUI(self.config).run(self.config)



    #     top_window = GUI.top_window(self._config_).window
    #
    #     log.debug('Instantiating TopWindow')
    #
    #     log.debug("Setting all other windows to inactive")
    #     opts_win_active = False
    #
    #     log.debug('Show window!')
    #
    #     units = config.get('sense_customize', 'dsp_temp')  # dsp = display
    #
    #     while True:
    #         event, values = top_window.read(timeout=100)
    #         if event is None or event == 'top_win_exit':
    #             log.info('User indicated a desire to exit.')
    #             exit()
    #
    #         # If the options window isn't already active and the user hit Settings on the main window then read the
    #         # options window and wait for the user to do something else.
    #         if not opts_win_active and event == 'Settings::_SETTINGS_BUTTON_':
    #             log.info('User indicated a desire to enter the Settings menu')
    #
    #             log.debug('Preparing window')
    #             from looking_glass.lib import OptsWindow
    #             opts_win_active = True
    #             log.debug('Options Window set to active.')
    #             log.debug('Calling Options Window builder')
    #             log.debug(f'Passing builder a config with these sections {config.sections()}')
    #             opts_builder = OptsWindow(config=config)
    #             opts_win = opts_builder.window
    #
    #         # Read the window and wait for event
    #         counter = 0
    #         while opts_win_active:
    #             event2, values2 = opts_win.read(timeout=100)
    #
    #             # If the user presses the X button or presses 'cancel' the options window will close.
    #             if event2 is None or event2 == 'opts_win_cancel':
    #                 log.debug('User cancelled or closed window')
    #                 log.debug('Closing Options Window, ignoring changes')
    #                 opts_win.close()
    #                 opts_win_active = False
    #                 log.debug('Options window closed and set to inactive status. No changes saved.')
    #
    #             # If the user presses 'OK' we call on the Config class to write the current config to a file
    #             if event2 == 'opts_win_ok':
    #                 log.debug('User indicated a desire to exit the config window')
    #
    #                 from looking_glass.lib import Config
    #                 Config.write(config)
    #
    #             # If the user presses 'Test Key' we test their API key
    #             if event2 == 'check_api_key':
    #                 import PySimpleGUI as gui
    #                 eprint = gui.EasyPrint()
    #                 eprint('Checking API key!')


if __name__ == "__main__":
    app = App()
    app.run()
else:
    print('Being imported, but not running __init__')
