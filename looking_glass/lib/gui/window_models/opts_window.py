def _localization_frame_(config):
    """
    This frame helps us group settings related to region-specific measurement systems

    :return:
    """

    import PySimpleGUIQt as qt
    frame = [
        [qt.Text('Primary Temperature Unit:', justification='left'),
         qt.Radio('Fahrenheit', group_id='temp_unit', default=True), qt.Radio('Celsius', group_id='temp_unit'),
         qt.Radio('Kelvin', group_id='temp_unit')
         ]
    ]
    return frame


def _weather_api_frame_(config):
    """
    This frame helps us group settings related to the weather API together to present in the GUI for the end-user


    :return:
    """
    import PySimpleGUIQt as qt

    struct = [
        [qt.Text('DarkSky API Key:', justification='left'),
         qt.InputText(config.get("weather_api_settings", "key"), key='darksky_api_key_input', justification='right')],
        [qt.Button('Reset', key='reset_fields'), qt.Button('Check Key', key='check_api_key')]
    ]

    return struct


def geolocale_frame(config):
    """
    This frame helps us group settings related to the geo-location together to present in the GUI for the end-user

    :return:
    """

    import PySimpleGUIQt as qt

    struct = [
        [qt.Text('Street Address:', justification="left"), qt.InputText('', key='input_st_address')],
        [qt.Text('City:', justification='left'), qt.InputText('', key='input_city')],
        [qt.Text('State:', justification='left'), qt.InputText('', key='input_state')],
        [qt.Text('Lat:', justification='left'), qt.InputText('', key='lat_input'),
         qt.Text('Lon:', justification='center'), qt.InputText('', key='lon_input'),
         ]
    ]

    return struct


def main_layout(config):
    """
    The main layout structure logic for the preferences window

    :return:
    """
    import PySimpleGUIQt as qt
    # noinspection SpellCheckingInspection
    layout = [
        [qt.Frame('', _localization_frame_(config), background_color='#00c2c7'),
         qt.Frame('', _weather_api_frame_(config),
                  background_color='#97ebdb')],
        [qt.Frame('', geolocale_frame(config), background_color='#005582')],
        [qt.Button('Cancel', key='opts_win_cancel'), qt.Button('OK', key='opts_win_ok')]

    ]

    return layout
