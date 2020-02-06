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
        import looking_glass
        gui = looking_glass.start_gui(self.config)
        log = self.log

        log.debug('Starting GUI')

        while True:
            event, val = gui.top_win.read(timeout=100)



if __name__ == "__main__":
    app = App()
    app.run()
else:
    print('Being imported, but not running __init__')
