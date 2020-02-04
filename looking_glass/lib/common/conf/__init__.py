class Config:

    def _determine_filepaths_(self):
        """
        Internal function to build file pathnames from the local environment
        :return:
        """

    def __init__(self, custom_conf=None):
        from configparser import ConfigParser
        import os
        import logging
        import glob

        self.file_pot = []
        parser = ConfigParser()

        log = logging.getLogger(__name__)

        if __name__ == '__main__':
            from looking_glass.lib.common.logger import start
            start(__name__, 'DEBUG')

        log.debug(f'Logger started for {__name__}')

        log.debug('Starting config parser')
        log.debug('Started!')
        print(__name__)

        if custom_conf is None:
            log.info('I did not receive a custom configuration path in the command-line arguments.')
            log.debug('Programatically building configuration file path/filenames from code')
            log.debug('Determining program root path')
            r_path = os.getcwd()
            log.debug(f'Found {r_path}')
            log.debug(f'Figuring configuration file path...')
            conf_path = str(r_path + '/conf')
            log.debug(f'Got {conf_path}')
            example_conf = str(conf_path + '/example_config.ini')
            default_conf = str(conf_path + '/config.ini')

            log.debug(f'Adding example_conf.ini to list of conf files')
            self.file_pot.append(default_conf)
            log.debug(f'State of file list: {self.file_pot}')
            log.debug(f'Adding default_conf.ini to files list:')
            self.file_pot.append(example_conf)
            log.debug(f'State of file list: {self.file_pot}')
            log.debug(f'Looking for the files in this list: {self.file_pot}')

        else:
            log.debug('User provided a custom configuration file path.')
            self.file_pot.append(custom_conf)

        found = parser.read(self.file_pot)
        missing = set(self.file_pot) - set(found)
        log.debug(f'Found the following conf-file: {found}')
        log.info(f'Found config files: {sorted(found)}')
        log.debug(f'Missing files: {sorted(missing)}')
        sep = ', '
        sections = sep.join(parser.sections())
        log.info(f"Config has sections: '{sections}'")

        for section in parser.sections():
            settings = sep.join(parser[section])
            log.debug(f"The keys in '{section}' are '{settings}'")

        self.parser = parser
