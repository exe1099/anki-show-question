from aqt import mw
from aqt import gui_hooks


def buttonColours(buttons_tuple, reviewer_, card):
    # change button "Easy" to "Try Again"
    buttons = list(buttons_tuple)
    buttons = buttons[:-1]
    buttons.append((4, "Try Again"))
    return tuple(buttons)


def dontproceed(stuff, reviewer, card):
    # don't proceed and show question if button with ease 4 is pressed
    proceed, ease = stuff
    if ease == 4:
        reviewer._showQuestion()
        return (False, ease)
    else:
        return (True, ease)


def add_entry(reviewer, menu):
    # add context menu entry
    # work in progress, adding a shortcut for the entry doesn't work
    entry = [["Show Question", "", reviewer._showQuestion]]
    reviewer._addMenuItems(menu, entry)
    #  shortcuts = reviewer._shortcutKeys()
    #  shortcuts.append(("8", reviewer._showQuestion))
    #  reviewer.mw.setStateShortcuts(shortcuts)


gui_hooks.reviewer_will_init_answer_buttons.append(buttonColours)
gui_hooks.reviewer_will_answer_card.append(dontproceed)
gui_hooks.reviewer_will_show_context_menu.append(add_entry)
