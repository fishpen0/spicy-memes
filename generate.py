#!/usr/bin/env python3
"""

This module takes in the local icon directory and outputs yaml files to the packs directory that match the formatting
for emojipacks.

"""

import settings
import yaml

from os import walk, path


def get_icons(directory, iconURL):
    """
    Generates a list of themes and their respective icons and icon sources

    :param directory: directory to gather icons from ordered as "{directory}/theme/icon.foo"
    :return: list of dicts of theme and icon names
    """
    packs = []
    for dirName, subdirList, fileList in walk(directory):
        if dirName != directory:
            # The theme is the directory name
            theme = dirName.split(path.sep)[-1]

            # Generate the list of emojis for the pack
            emojis = list()
            for file in fileList:
                src = "{url}/{theme}/{icon}".format(url=iconURL, theme=theme, icon=file)
                emoji = {
                    "name": file.split('.')[0],
                    "src": src
                }
                emojis.append(emoji)
            emojis = sorted(emojis, key=lambda k: k['name'])

            # Assign pack items to pack
            pack = dict()
            pack["title"] = theme
            pack["emojis"] = emojis
            packs.append(pack)
    return packs


def write_emojipaks(packs, path):
    for pack in packs:
        with open(path+pack['title']+".yml", 'w') as outfile:
            yaml.dump(pack, outfile, default_flow_style=False)


if __name__ == "__main__":
    pack_list = get_icons(settings.GENERATE_ICONS_PATH, settings.GENERATE_URL)
    write_emojipaks(pack_list, settings.GENERATE_PACKS_PATH)
