from sys import argv
import re


filename = argv[1]
with open(filename + '.json', 'r') as f:
    with open(filename + '.json.new', 'w') as g:
        for line in f.readlines():
            # if re.search('locations\/IN\/india\/\?page=', line) is None:
            # if re.search('explore/locations\/IN\/india\/', line) is None:
            # if re.search('\/\?page=', line) is None:
            if line[:-1].strip():
                g.write(line)
            else:
                pass

# shutil.move(filename + '.json', filename + '.json.new')
