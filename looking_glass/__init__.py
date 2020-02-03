def configure():
    from .lib.common import conf


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
