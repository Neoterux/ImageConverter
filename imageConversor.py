from PIL import Image
import os
import re

def make_dir(name):
    try:
        os.stat(name)
    except:
        os.mkdir(name)

def find_file(pathList, extension):
    all_files = list(os.listdir("input"))
    r = re.compile(extension + "$")
    pathList = list(filter(r.search, all_files))
    return pathList

def get_option():
    op = input("a)webm\nb)png\nc)jpg\n")
    if op.lower() == "a":
        return ".webp"
    elif op.lower() == "b":
        return ".png"
    elif op.lower == "c":
        return ".jpg"
    else:
        return get_Option()

make_dir("input")
print("Seleccione la extension objetivo:")
old_ext = get_option()

print("Lista de archivos")

files = []
files = find_file(files, old_ext)
print(files)

if not files:
    print("No se han encontrado archivos con esa extension")
    exit()
    
print("selecciones la extension a convertir")
new_ext = get_option()

if new_ext != old_ext:
    make_dir("output")
    for image_file in files:
        image = Image.open("input\\" + image_file)
        image.save("output\\" + image_file.lower().replace(old_ext, new_ext))

print("Finalizado")
    


    

