import os

path = os.getcwd()

files = os.listdir(path=path)

for file in files:
    if len(file) > 12:
        hour = file[-10:-8]
        minute = file[-8:-6]
        second = file[-6:-4]
        formula = hour + ':' + minute + ':' + second + '.mp4'
        os.rename(file, formula)
    else:
        print('Done')
