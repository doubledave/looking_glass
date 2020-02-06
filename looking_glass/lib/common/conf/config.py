from looking_glass import App


class Config(App):

    def filepath_list_build(self, file_names):
        log = self.log
        new_file_names = []
        for file in file_names:
            log.debug(f'Removing {file} from list to be replaced')
            file_names.remove(file)

            new_filepath = str(f'{self.config_dir}{file}')
            log.debug(f'New value will be {new_filepath}')

            new_file_names.append(new_filepath)
            log.debug(f'Added {new_filepath} to list')

        return new_file_names

    def __init__(self, custom_conf=None):
        import os
        from configparser import ConfigParser
        import glob

        parser = ConfigParser()
        import logging
        log = logging.getLogger(str(f'LookingGlass.App.{self.__class__.__name__}'))
        self.log = log
        log.debug(f'Logger started for {self.__class__.__name__}')

        self.config_dir = str(f"{os.getcwd()}/conf/")
        config_dir = self.config_dir
        log.debug(f"Default 'config' directory is {config_dir}")
        file_names = ['config.ini', 'example-config.ini']
        file_names = self.filepath_list_build(file_names)

        log.debug(f'Final paths for default .ini locations: {file_names}')

        log.debug(f'Checking to see if user provided a custom config file path as an argument...')
        if custom_conf is not None:
            log.info(f'Caught argument to specify config file path.')
            file_names.insert(0, custom_conf)

        found = parser.read(file_names)
        log.info(f'Found config file with the following sections: {parser.sections}')
        missing = set(file_names) - set(found)

        print('Found config files:', sorted(found))
        print('Missing files     :', sorted(missing))

    def write(self):
        import os
        with open(os.getcwd() + '/conf/config.ini', 'w') as conf_file:
            self.config.write(conf_file)


if __name__ == "__main__":
    config = Config()
else:
    print(__name__ + ' is being imported, but not running __init__')
