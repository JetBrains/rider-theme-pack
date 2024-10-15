# rider-theme-pack

[![JetBrains team project](https://jb.gg/badges/team.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

## Color scheme editing

After making changes to the color scheme files (`colorSchemes\*.xml`) apply the sorting utility
`tools\PrettyXML.py` to make these files have the same order of elements and attributes. 
This utility requires Python 3.7 . 

There is an IDEA run configuration *'Sort color scheme files'* for that task.

#### Rider-specific color themes (`Rider*.xml`)

These files are created by a utility which is not published yet. Please don't edit them manually, 
these changes will be lost.

## How to debug the plugin in Rider

Since this plugin is bundled with Rider *and* hidden from the list of installed plugins *and* also protected from being
deactivated, it's not easy to develop a new version of the plugin since the newer version of the plugin is not loaded 
because of the protection of the bundled version.

To circumvent this, change the plugin ID in the file `META-INF/plugin.xml`:
    
    <idea-plugin>
    <id>Rider UI Theme Pack DEBUG</id>
    <name>Rider UI Theme Pack</name>
    ...

Now the new version of the plugin will be loaded. Well, because now it's essentially just another plugin. Since 
the UI themes' and schemes' names are still the same, there can be some confusion selecting the proper theme/scheme. 

The lists of UI themes will have two instances of each theme:

    Rider Light
    Rider Light     <- from the updated plugin
    Rider Dark
    Rider Dark      <- from the updated plugin

Unlike the UI themes, the lists of Editor Color Schemes will only contain a single instance of each color theme, 
and these color schemes are the ones from the updated version of the plugin.

**Warning!** While running the sand-boxed Rider, be careful not to save the scheme changes as a user-modified scheme. If you do, the file with the modified scheme will be saved in the profile directory at `build/idea-sandbox/config/colors/`. Such modified scheme has a prioroty over the bundled scheme with the same name. As a result, the changes you do to the scheme you develop, will have no effect.

## How to debug Classic UI

Since version 24.2, it's no longer possible to switch to the Classic UI, and the corresponding registry flag also 
doesn't work. Instead, one is supposed to install a plugin which enables the Classic UI.

The problem is that it might be quite cumbersome to install the plugin into the temporary versions of Rider/IDEA.
To overcome that, add `<iconMapperSuppressor />` to the list of extensions in the `plugin.xml`:

    <extensions defaultExtensionNs="com.intellij">
        <iconMapperSuppressor />
    </extensions>

With this change, Rider/IDEA will launch with the Classic UI turned on.

## Branches

The plugin `Rider Theme Pack` in the IDEA plugin gallery is built from the branch `plugin`.

The branches named `net*` are for the themes bundled with the matching branches of Rider:
* `net232` for Rider 2023.2
* `net233` for Rider 2023.3

Since 2024, the branches' names no longer have the prefix `net`:
* `241` for Rider 2024.1
* `242` for Rider 2024.2
