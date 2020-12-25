import json
import os
import shutil

# Icon cache folder
iconCacheFolder = 'icon_cache'

# Output destination of the correlation data
correlationSet = 'correlation.json'

with open('index.json', encoding='utf-8') as json_file:
    items = json.load(json_file)
    for item in items:
        src = namedFolder + os.path.sep + item['icon']

        if not os.path.exists(src):
            print(item['uid'] + " - Could not find: " + src)

        try:
            dest = outputFolder + os.path.sep + item['uid'] + '.png'
            shutil.copyfile(src, dest)
        except Exception as e:
            print(item['uid'] + " - Error while copying icon: " + str(e))