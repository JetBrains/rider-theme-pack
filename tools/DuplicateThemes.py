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
        scheme = "/colorSchemes/RiderMelonLight.xml")

    copyTheme(
        src = "RiderDark.theme.json",
        dest = "RiderMelonDark.theme.json",
        name = "Rider Melon Dark",
        scheme = "/colorSchemes/RiderMelonDark.xml")


    # Rider -> Visual Studio
    # For now, they look the same but later VS should become a separate theme
    copyTheme(
        src = "RiderLight.theme.json",
        dest = "VisualStudioLight.theme.json",
        name = "Visual Studio Light",
        scheme = "/colorSchemes/VisualStudioLight.xml")

    copyTheme(
        src = "RiderDark.theme.json",
        dest = "VisualStudioDark.theme.json",
        name = "Visual Studio Dark",
        scheme = "/colorSchemes/VisualStudioDark.xml")


    # Visual Studio -> ReSharper
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioLight.theme.json",
        dest = "ReSharperLight.theme.json",
        name = "ReSharper Light",
        scheme = "/colorSchemes/ReSharperLight.xml")

    copyTheme(
        src = "VisualStudioDark.theme.json",
        dest = "ReSharperDark.theme.json",
        name = "ReSharper Dark",
        scheme = "/colorSchemes/ReSharperDark.xml")


    # Visual Studio -> Visual Assist
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioLight.theme.json",
        dest = "VisualAssistLight.theme.json",
        name = "Visual Assist Light",
        scheme = "/colorSchemes/VisualAssistLight.xml")

    copyTheme(
        src = "VisualStudioDark.theme.json",
        dest = "VisualAssistDark.theme.json",
        name = "Visual Assist Dark",
        scheme = "/colorSchemes/VisualAssistDark.xml")

    # New UI

    # Rider -> Rider Melon
    # Separate theme only for convenience in switching
    copyTheme(
        src = "RiderDay.theme.json",
        dest = "RiderMelonDay.theme.json",
        name = "Rider Melon Day",
        scheme = "/colorSchemes/RiderMelonDay.xml")

    copyTheme(
        src = "RiderNight.theme.json",
        dest = "RiderMelonNight.theme.json",
        name = "Rider Melon Night",
        scheme = "/colorSchemes/RiderMelonNight.xml")


    # Rider -> Visual Studio
    # For now, they look the same but later VS should become a separate theme
    copyTheme(
        src = "RiderDay.theme.json",
        dest = "VisualStudioDay.theme.json",
        name = "Visual Studio Day",
        scheme = "/colorSchemes/VisualStudioDay.xml")

    copyTheme(
        src = "RiderNight.theme.json",
        dest = "VisualStudioNight.theme.json",
        name = "Visual Studio Night",
        scheme = "/colorSchemes/VisualStudioNight.xml")


    # Visual Studio -> ReSharper
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioDay.theme.json",
        dest = "ReSharperDay.theme.json",
        name = "ReSharper Day",
        scheme = "/colorSchemes/ReSharperDay.xml")

    copyTheme(
        src = "VisualStudioNight.theme.json",
        dest = "ReSharperNight.theme.json",
        name = "ReSharper Night",
        scheme = "/colorSchemes/ReSharperNight.xml")


    # Visual Studio -> Visual Assist
    # Separate theme only for convenience in switching
    copyTheme(
        src = "VisualStudioDay.theme.json",
        dest = "VisualAssistDay.theme.json",
        name = "Visual Assist Day",
        scheme = "/colorSchemes/VisualAssistDay.xml")

    copyTheme(
        src = "VisualStudioNight.theme.json",
        dest = "VisualAssistNight.theme.json",
        name = "Visual Assist Night",
        scheme = "/colorSchemes/VisualAssistNight.xml")
