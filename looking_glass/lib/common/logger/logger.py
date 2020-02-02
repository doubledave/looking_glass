#!/usr/bin/env python3

    
    # root_name = None
    #
    # @staticmethod
    # def name_registrar(caller_name):
    #     """
    #         This method can be called to get the right name for a module to get a logger with
    #
    #         :param caller_name:
    #         :return:
    #     """
    #     root_name = 'LookingGlass'
    #
    #     return
    #
    # def setup_logger(self, caller_name=None):
    #     import logging
    #     from colorlog import ColoredFormatter
    #
    #     print(self.name_registrar('App'))
    #
    #     if not Logger.root_name:
    #         root_name = 'LookingGlass.App'
    #         caller_name = root_name
    #         Logger.root_name = root_name
    #     else:
    #         caller_name = Logger.root_name + '.' + caller_name
    #     formatter = ColoredFormatter(
    #         "%(bold_cyan)s%(asctime)-s%(reset)s%(log_color)s::%(name)-14s::%(levelname)-10s%(reset)s%(blue)s%(message)-s",
    #         datefmt=None,
    #         reset=True,
    #         log_colors={
    #             'DEBUG': 'bold_cyan',
    #             'INFO': 'bold_green',
    #             'WARNING': 'bold_yellow',
    #             'ERROR': 'bold_red',
    #             'CRITICAL': 'bold_red',
    #         }
    #     )
    #
    #     logger = logging.getLogger(caller_name)
    #     handler = logging.StreamHandler()
    #     handler.setFormatter(formatter)
    #     logger.addHandler(handler)
    #     logger.setLevel(logging.DEBUG)
    #     logger.info(f'Logger started for %s' % caller_name)
    #
    #     return logger
    #
    # def __init__(self, name):
    #     root_name = 'LookingGlass'
    #
    #     name = str(f'{root_name}.{name}')
    #
    #     self.log = self.setup_logger(caller_name=name)
class Logger:
    import logging

    root = 'LookingGlass.App'

    parents = [

        'GUI'

    ]

    def


class Default(Logger):




