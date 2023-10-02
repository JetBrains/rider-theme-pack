import json
import logging

def copyTheme(src: str, dest: str, name: str = None, scheme: str = None):
    source = None
    try:
        source = open(src, "r", encoding = "UTF-8", newline = "")
        destination = open(dest, mode = "w", encoding = "UTF-8", newline = "")

        theme = json.load(source)
        if name:
            theme["name"] = name
        if scheme:
            theme["editorScheme"] = scheme
        json.dump(
            {"commentary": "This document is auto-generated, do not edit manually", **theme},
            destination,
            indent = 2)
    except IOError as e:
        if source:
            print("'{0}': {1} (I/O error({2}))".format(dest, e.strerror, e.errno))
        else:
            print("'{0}': {1} (I/O error({2}))".format(src, e.strerror, e.errno))
    except json.JSONDecodeError:
        logging.warning(src + " is not a valid JSON file")

    pass

if __name__ == "__main__":

    # Old UI

    # Rider -> Rider Melon
    # Separate theme only for convenience in switching
    copyTheme(
        src = "RiderLight.theme.json",
        dest = "RiderMelonLight.theme.json",
        name = "Rider Melon Light",
        scheme = "Rider Melon Light")

    copyTheme(
        src = "RiderDark.theme.json",
        dest = "RiderMelonDark.theme.json",
        name = "Rider Melon Dark",
        scheme = "Rider Melon Dark")


    # Rider -> Visual Studio
    # For now, they look the same but later VS should become a separate theme
    copyTheme(
        src = "RiderLight.theme.json",
        dest = "VisualStudioLight.theme.json",
        name = "Visual Studio Light",
        scheme = "Visual Studio Light")

    copyTheme(
        src = "RiderDark.theme.json",
        dest = "VisualStudioDark.theme.json",
        name = "Visual Studio Dark",
        scheme = "Visual Studio Dark")


    # Visual Studio -> ReSharper
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioLight.theme.json",
        dest = "ReSharperLight.theme.json",
        name = "ReSharper Light",
        scheme = "ReSharper Light")

    copyTheme(
        src = "VisualStudioDark.theme.json",
        dest = "ReSharperDark.theme.json",
        name = "ReSharper Dark",
        scheme = "ReSharper Dark")


    # Visual Studio -> Visual Assist
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioLight.theme.json",
        dest = "VisualAssistLight.theme.json",
        name = "Visual Assist Light",
        scheme = "Visual Assist Light")

    copyTheme(
        src = "VisualStudioDark.theme.json",
        dest = "VisualAssistDark.theme.json",
        name = "Visual Assist Dark",
        scheme = "Visual Assist Dark")

############## New UI ##############################

    # Rider -> Rider Melon
    # Separate theme only for convenience in switching
    copyTheme(
        src = "RiderDay.theme.json",
        dest = "RiderMelonDay.theme.json",
        name = "Rider Melon Day",
        scheme = "Rider Melon Light")

    copyTheme(
        src = "RiderNight.theme.json",
        dest = "RiderMelonNight.theme.json",
        name = "Rider Melon Night",
        scheme = "Rider Melon Dark")


    # Rider -> Visual Studio
    # For now, they look the same but later VS should become a separate theme
    copyTheme(
        src = "RiderDay.theme.json",
        dest = "VisualStudioDay.theme.json",
        name = "Visual Studio Day",
        scheme = "Visual Studio Light")

    copyTheme(
        src = "RiderNight.theme.json",
        dest = "VisualStudioNight.theme.json",
        name = "Visual Studio Night",
        scheme = "Visual Studio Dark")


    # Visual Studio -> ReSharper
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioDay.theme.json",
        dest = "ReSharperDay.theme.json",
        name = "ReSharper Day",
        scheme = "ReSharper Light")

    copyTheme(
        src = "VisualStudioNight.theme.json",
        dest = "ReSharperNight.theme.json",
        name = "ReSharper Night",
        scheme = "ReSharper Dark")


    # Visual Studio -> Visual Assist
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioDay.theme.json",
        dest = "VisualAssistDay.theme.json",
        name = "Visual Assist Day",
        scheme = "Visual Assist Light")

    copyTheme(
        src = "VisualStudioNight.theme.json",
        dest = "VisualAssistNight.theme.json",
        name = "Visual Assist Night",
        scheme = "Visual Assist Dark")
