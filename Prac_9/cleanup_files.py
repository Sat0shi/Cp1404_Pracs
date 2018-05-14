"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory

    # NOTE: These options won't just work...
    # they show you ways of renaming and moving files,
    # but you need to have valid filenames. You can't make a file with
    # a blank name, and on Windows you can't have files with the same
    # characters but different case (e.g. a.TXT and A.txt)
    # So, you need to get valid filenames before you can use these.

    # Option 1: rename file to new name - in place
    # os.rename(filename, new_name)

    # Option 2: move file to new place, with new name
    # shutil.move(filename, 'temp/' + new_name)

    # Processing subdirectories using os.walk()

    # os.chdir('..')  # .. means "up" one directory
    for dir_name, subdir_list, file_list in os.walk('.'):
        for filename in file_list:
            # ignore directories, just process files
            if not os.path.isdir(filename) and filename != '.DS_Store':
                new_name = get_fixed_filename(filename)
                print(new_name)
                os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    fileNameJoining = ''
    for letter in filename:
        if len(fileNameJoining) == 0:
            fileNameJoining += letter
        else:
            if letter.isupper() and fileNameJoining[-1].isalpha() == True:
                fileNameJoining += '_' + letter
            elif fileNameJoining[-1].isalpha() == False and fileNameJoining[-1] != '.' and fileNameJoining[-1] != "'":
                fileNameJoining += letter.capitalize()
            else:
                fileNameJoining = fileNameJoining + letter

    new_name = fileNameJoining

    return new_name


main()
