
"""
    Define a kind of template object to construct windows on later
"""


def _pop_set_win(config):
    from .opts_window import OptsWindow
    win_builder = OptsWindow()
    opts_window = win_builder.window

    while True:
        event, value = opts_window.read(timeout=100)
        if event is None or event == 'opts_win_cancel':
            opts_window.close()
            break

        if event == 'opts_win_ok':
            from looking_glass.lib import Config
            Config.write("conf/config.ini")

def _first_time_(self, config):
    """
    This is run when the system detects no config file or a malformed config

    :param config:
    :return:
    """
    import PySimpleGUIQt as qt
    from icons.app_icons import config_icon
    icon = config_icon()

    # Build popup to ask user to config
    message = "It seems that you haven't gone through setting your options yet. Would you like me to open " \
              "the options window immediately after starting this one time to initialize your config file?"

    # Pop the question
    query = qt.PopupYesNo(message, title='Config warning...', keep_on_top=True, icon=icon, location=(475, 325))

    # If
    if str(query).lower() == 'yes':
        _pop_set_win(config)




def _button_frame_():
    """
    Create a frame for our buttons at the bottom of the window

    :returns: Button frame object
    :rtype:
    """
    import PySimpleGUIQt as qt
    b_frame = [
        [qt.Button('Make Another', key='dupe'), qt.Button('Exit', key='top_win_exit')]
    ]
    return b_frame


def _sense_frame_(config):
    device_name = 'Living Room'
    import PySimpleGUIQt as qt
    from looking_glass.lib.sense.info import SenseInfo
    info = SenseInfo()

    if config.get('sense_customize', 'dsp_temp') == 'F':
        temp = info.get_temp_f()
    else:
        temp = info.get_temp(raw=False)

    humidity = round(info.get_humidity(quick=True))
    humidity = humidity.__str__()
    print(humidity)

    struct = [[qt.Text(f'Current Interior Temperature in {device_name}'), qt.Text(temp, key='test_field', justification='right'),],
              [qt.Text(f'Current humidity in {device_name}'), qt.Text(f"{humidity}%", key='humidity_results', justification='right')],
              [qt.Text(f"Current barometric pressure in {device_name}"),
               qt.Text(info.get_pressure(), key='pressure_results'),
               qt.Text('MB')]
    ]
    return struct

def _layout_(config):
    import PySimpleGUIQt as qt
    from looking_glass.lib.gui.menus import top
    top_menu = top.menu()
    struct = [
        [qt.Menu(top_menu)],
        [qt.Text('Welcome to Test API!')],
        [qt.Combo(['Living Room', 'Playroom'])],
        [qt.Frame('', _sense_frame_(config))],
        [qt.Frame('', list(_button_frame_()))]
    ]

    return struct


