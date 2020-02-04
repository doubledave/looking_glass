def menu():
    """
    Will return the structure for the top-menu, which will be shown on the top_window

    :return: List containing various buttons
    """
    main_menu = [
        ['File', ['Settings::_SETTINGS_BUTTON_']],
        ['Help', ['Docs', ['@softworks.inspyre.tech'],
                  ],
         ],
    ]
    return main_menu
