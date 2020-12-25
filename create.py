import json
import os
import shutil

###
# This script will create a folder with all icons named after their uid,
# based on a json file which contains the required information.
###

# Folder containing named icons
namedFolder = 'name'

# Output folder for icons with uid names
outputFolder = 'uid'

# Set this to the old output folder if you want to create based on it
baseFolder = 'icons'

# Set this true if you always want to use the base icon when in doubt
forceBase = False

# Data used for matching
# Must contain uid and icon
correlationSet = 'correlation.json'

with open(correlationSet, encoding='utf-8') as json_file:
    items = json.load(json_file)
    for item in items:
        src = namedFolder + os.path.sep + item['icon']

        if not os.path.exists(src):
            print(item['uid'] + " - Could not find: " + src)

            baseSrc = baseFolder + os.path.sep + item['uid'] + '.png'
            if not os.path.exists(baseSrc):
                print(item['uid'] + " - Could not find base source at: " + baseSrc)
                continue

            print(item['uid'] + " - Found base source at: " + baseSrc)

            if not forceBase:
                print(item['uid'] + " - Do you want to use this icon? [Y/n]")
                if input().lower() == 'n':
                    continue

            try:
                dest = outputFolder + os.path.sep + item['uid'] + '.png'
                shutil.copyfile(baseSrc, dest)
            except Exception as e:
                print(item['uid'] + " - Error while copying icon: " + str(e))

            continue

        try:
            dest = outputFolder + os.path.sep + item['uid'] + '.png'
            shutil.copyfile(src, dest)
        except Exception as e:
            print(item['uid'] + " - Error while copying icon: " + str(e))