import json
import os

###
# This script will check if all icons contained in the
# correlation data exist in the name / uid folder.
###

# Folder containing named icons
namedFolder = 'name'

# Folder containing icons named after uid
uidFolder = 'uid'

# Output file for cleaned correlation data
correlationDataClean = 'correlationClean.json'

# Data used for matching
# Must contain uid and icon
correlationData = 'correlation.json'

with open(correlationData, encoding='utf-8') as json_file:
    items = json.load(json_file)
    for i in range(len(items)):
        nameSrc = namedFolder + os.path.sep + items[i]['icon']
        uidSrc = uidFolder + os.path.sep + items[i]['uid'] + '.png'

        if not os.path.exists(nameSrc):
            print(items[i]['uid'] + " - Could not find: " + nameSrc)

        if not os.path.exists(uidSrc):
            print(items[i]['uid'] + " - Could not find: " + uidSrc)

    out = [
        item for item in items
        if ((os.path.exists(namedFolder + os.path.sep + item['icon'])) or (os.path.exists(uidFolder + os.path.sep +
                                                                                          item['uid'] + '.png')))
    ]
    open(correlationDataClean, 'w').write(json.dumps(out, sort_keys=True, indent=4, separators=(',', ': ')))
