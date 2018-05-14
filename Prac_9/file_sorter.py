import os
import shutil

def main():
    os.chdir('FilesToSort/FilesToSort')
    type_doc = input('What category would you like to sort doc files into?')
    type_docx = input('What category would you like to sort docx files into?')
    type_png = input('What category would you like to sort png files into?')
    type_gif = input('What category would you like to sort gif files into?')
    type_txt = input('What category would you like to sort txt files into?')
    type_xls = input('What category would you like to sort xls files into?')
    type_xlsx = input('What category would you like to sort xlsx files into?')
    type_jpg = input('What category would you like to sort jpg files into?')
    type_list = [type_doc, type_docx, type_png, type_gif, type_txt, type_xls, type_xlsx, type_jpg]
    for dir_name, subdir_list, file_list in os.walk('.'):
        for filename in file_list:
            if filename != '.DS_Store':
                print(filename)
                sort_files(filename, type_list)


def sort_files(filename, type_list):
    if filename[filename.find('.') + 1: len(filename)] == 'xlsx':
        try:
            shutil.move(filename, type_list[6] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[6])
            shutil.move(filename, type_list[6] + '/' + filename)

    elif filename[filename.find('.') + 1: len(filename)] == 'docx':
        try:
            shutil.move(filename, type_list[1] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[1])
            shutil.move(filename, type_list[1] + '/' + filename)

    elif filename[filename.find('.') + 1: len(filename)] == 'png':
        try:
            shutil.move(filename, type_list[2] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[2])
            shutil.move(filename, type_list[2] + '/' + filename)

    elif filename[filename.find('.') + 1: len(filename)] == 'doc':
        try:
            shutil.move(filename, type_list[0] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[0])
            shutil.move(filename, type_list[0] + '/' + filename)

    elif filename[filename.find('.') + 1: len(filename)] == 'jpg':
        try:
            shutil.move(filename, type_list[7] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[7])
            shutil.move(filename, type_list[7] + '/' + filename)

    elif filename[filename.find('.') + 1: len(filename)] == 'xls':
        try:
            shutil.move(filename, type_list[5] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[5])
            shutil.move(filename, type_list[5] + '/' + filename)

    elif filename[filename.find('.') + 1: len(filename)] == 'txt':
        try:
            shutil.move(filename, type_list[4] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[4])
            shutil.move(filename, type_list[4] + '/' + filename)

    elif filename[filename.find('.') + 1: len(filename)] == 'gif':
        try:
            shutil.move(filename, type_list[3] + '/' + filename)
        except FileNotFoundError:
            os.mkdir(type_list[3])
            shutil.move(filename, type_list[3] + '/' + filename)

    else:
        print('something went wrong OWO')
        print(filename[filename.find('.') + 1: len(filename)])



main()