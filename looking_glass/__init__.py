def configure():
    if __name__ == '__main__':
        from looking_glass.lib.common.logger import start
        start(__name__, 'DEBUG')

    from looking_glass.lib.common.conf import Config
    conf = Config()
    return conf.parser


def start_logger(quiet=False, dev=False, verbose=False, gui=True):
    from .lib.common import logger
    from .lib.common.logger import InvalidLevelError
    import logging
    level = ''
    if dev:
        level = 'DEBUG'
    elif verbose:
        level = 'INFO'
    elif quiet:
        level = 'CRITICAL'

    try:
        log = logger.start(__name__, level=level)
    except InvalidLevelError:
        log = logging.getLogger()
        log.fatal('Invalid log level provided')

    return log


def start_gui(config):
    from looking_glass.lib.gui import GUI
    gui = GUI(config)
    return gui
