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

    def run(self, config):
        import PySimpleGUIQt as qt
        import looking_glass.lib.gui.window_models.top_window as top_window
        log = self.log
        log.debug('Creating top window')
        top_win = qt.Window('Looking Glass', layout=top_window._layout_(config=self.config))

        while True:
            event, vals = top_win.read(timeout=100)

            if event is None or event == 'top_win_exit':
                exit()


