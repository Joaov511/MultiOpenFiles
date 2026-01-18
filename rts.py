import os
relativePath = os.path.dirname(os.path.abspath(__file__))
programsFilepaths = relativePath + "/paths.txt"

with open(programsFilepaths, 'r') as paths:
    for path in paths:
        os.startfile(path.strip())



