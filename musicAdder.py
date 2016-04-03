#!/usr/local/bin/python3

###/!usr/bin/env python3
import os,csv,shutil

dire = '/Users/ben/Music/music'

log = 'MusicAdder_log.txt'

existingLog = '~/Music/music/' + log

destination = '~/Music/iTunes/iTunes Music/Automatically Add to iTunes'


def directory(path): #creates list of all files in given directory
    paths = []
    print('parsing files...')
    files  = os.listdir(path)
    for file in files:
        paths.append(path + '/' + file + '\n')
    print(len(paths), 'files detected')
    return paths

def writeOut(dire,log):
    removed = []
    transfer = [] #list of files to transfer
    with open(log, 'r') as f: ##r+ or w alternate mode (readandwrite/write)
        paths = directory(dire)
        print(paths)
        existing = list(f)

        print(existing)
        for d in paths:
            ###f.write(d)
            if d not in existing:
                transfer.append(d.split('\n')[0])
                existing.append(d)
        for e in existing: ### to remove entries not in the existing folder
            if e not in paths:
                existing.remove(e)
                removed.append(e)
        if len(removed) > 0:
                print('removed:', removed, end=" ")
        else:
            print('0 removed')

        existing = list(set(existing))
    with open(existingLog,'w') as f:
        for e in existing:
            f.write(e)


    transfer.remove("~/Music/music/Icon\r")
    return transfer

def addToItunes(transfer):
    print('copying:')
    for t in transfer:
        print(t)
        dest = destination + t
        if os.path.isdir(t)==True:
            shutil.copytree(t,dest)
        elif os.path.isfile(t)==True and '.mp3' in t:
            shutil.copytree(t,dest)
        else:
            print(t," is not music")

wOut = writeOut(dire,log)
addToItunes(wOut)
print('Success!')

