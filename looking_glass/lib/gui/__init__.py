class GUI:
    """
    A class that serves as a parent to each window/menu/pop-up class
    """

    def __init__(self, config):
        import logging

        self.config = config

        log = logging.getLogger(__name__)
        log.debug(f'Logger started for {__name__}')
        self.log = log
        self.top_win = None
        self.run()

    def run(self):
        import PySimpleGUIQt as qt
        from looking_glass.lib.gui.animations import loading as loading
        import looking_glass.lib.gui.window_models.top_window as top_window
        from looking_glass.lib.gui.window_models.opts_window import main_layout as opts_layout
        loading()
        opts_win_active = False
        log = self.log
        log.debug('Creating top window')
        self.top_win = qt.Window('Looking Glass', layout=top_window._layout_(config=self.config))

        while True:
            event, vals = self.top_win.read(timeout=100)

            # If the user hits the 'X' button in the top right of the window or the "Exit" button on the bottom right
            # they will exit the app cleanly
            if event is None or event == 'top_win_exit':
                log.info('User indicated desire to exit')
                log.debug('Exiting cleanly')
                exit()

            if not opts_win_active and event == 'Settings::_SETTINGS_BUTTON_':
                log.info('User indicated desire to open settings window')

                opts_win = qt.Window('Settings', layout=opts_layout(self.config))
                opts_win_active = True
                while opts_win_active:
                    opts_event, opts_values = opts_win.read(timeout=100)

                    if opts_event in [None, 'opts_win_cancel']:
                        log.info('User indicated desire to exit from the settings window without saving values.')
                        log.debug('Closing window')
                        opts_win.close()
                        log.debug("Setting window's active flag to False")
                        opts_win_active = False

                    if opts_event == 'check_api_key':
                        import PySimpleGUI as sg
                        for i in range(100000):
                            sg.popup_animated('/home/taylor/.src/LookingGlass/source.gif', background_color='white',
                                              time_between_frames=100)
                        sg.popup_animated(None)



