# Helpful Tutorial 1: https://www.youtube.com/watch?v=HHcZbXsZtm0&ab_channel=MaxTeachesTech
# Helpful Tutorial 2: https://www.youtube.com/watch?v=2P30W3TN4nI&ab_channel=MaxTeachesTech
# Helpful Tutorial 3: https://stackoverflow.com/questions/64773484/virtualenv-and-pycharm-folders-and-packages-how-does-it-work#:~:text=Your%20code%20is%20not%20supposed%20to%20go%20there%2C%20it%20is%20for%20your%20environment%20only.%20Move%20any%20source%20files%20to%20the%20root%20of%20your%20project.

# Libraries Required
# tk
# ghostscript
# camelot-py

import camelot

# Make sure you install camelot-py[base]
# Don't install Camelot or CV versions. Those are two different things.
# Cv uses the openCV lib and camelot is a whole diff package
tables = camelot.read_pdf('sample.pdf', pages='2')
print(tables)


# Downgrade the pyPDF: https://github.com/camelot-dev/camelot/issues/339
# Download GhostScript: https://www.youtube.com/watch?v=Y-FYq0tA3-w&ab_channel=EngineerBaaniya
# I had to add the GS bin to the PATH, along with python.exe