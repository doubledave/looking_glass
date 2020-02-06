import PySimpleGUI as gui


class ConfManError(Exception):
    pass


class NoInputError(ConfManError):
    @staticmethod
    def message():
        print('No file selected!')


def load_config(file):
    import configparser

    parser = configparser.ConfigParser()
    parser.read(file)

    return parser


config = None


def check_overwrite(file):
    import ntpath
    from pathlib import Path
    if Path(file).is_file():
        print('File exists')
        confirm = gui.PopupYesNo(f'The file {ntpath.basename(file)} already exists. Overwrite?')
        if confirm.lower() == 'yes':
            return True
        else:
            return False
    else:
        print("File does not exist")
        return True


def save_config():
    print(config.sections())
    from pathlib import Path
    import os
    filepath = os.getcwd()
    filepath = filepath + "/conf_man/output"
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    file = str(filepath + '/config.ini')

    if check_overwrite(file):
        print('Saving...')
        with open(file, 'w') as configfile:

            config.write(configfile)


def grabby(config):
    grab = config.get('gui_settings', 'grab_anywhere')
    print(type(grab))
    if grab.lower() in ['true', '1', 't', 'y', 'yes', 'affirmative', 'positive']:
        return True
    else:
        return False


def show():
    print(config.sections())
    layout = []
    for section in config.sections():
        f_layout = []
        section_title = str(section).replace('_', ' ')
        print(config.options(section=section))
        for option in config.options(section=section):
            f_layout += [gui.Text(option, justification='left', pad=(50,5)),
                         gui.InputText(config.get(section=section, option=option), justification='right', pad=(50,5),
                                       key=str(f'{section}.{option}'))],

            frame = [[gui.Frame(f'{str(section_title).title()}', layout=f_layout)]]

        layout += frame
    layout += [[gui.Button('OK', key='ok'), gui.Button('Apply', key='apply'), gui.Button('Exit', key='exit')]]
    print(config.get('gui_settings', 'grab_anywhere'))
    window = gui.Window('Test Config Window', layout=layout, size=(500,500),element_justification='center', grab_anywhere=grabby(config))

    while True:
        event, vals = window.read(timeout=100)

        if event is None or event == 'exit':
            window.close()
            exit()

        if event == 'apply':
            window.refresh()
            print('window refreshed')


        if event == 'apply' or event == 'ok':
            print(vals)
            for setting in vals:
                val = vals[setting]
                print(val)
                setting = setting.split(sep='.')
                if val != config.get(setting[0], setting[1]):
                    print('value changed')
                config[setting[0]][setting[1]] = val
            confirm = gui.PopupYesNo('Are you sure you want to save config?', title='Confirm Save')
            if confirm.lower() == 'yes':
                print('Saving')
                save_config()
            else:
                print('Cancelled')



def run():
    global config
    import os
    path = os.getcwd()
    path = str(path)
    print(path)
    file = gui.PopupGetFile(
        'Pick a config file',
        default_path=path,
        file_types=(
            ('Config Files', '*.ini'),
        )
    )

    if file == '':
        raise NoInputError

    config = load_config(file)
    show()

try:
    run()
except NoInputError:
    NoInputError.message()
    raise
