from PIL import Image
import os
import re

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def make_dir(name):
    try:
        os.stat(name)
    except:
        print("Creando directorio " + name + "...")
        os.mkdir(name)
        print("Exitoso")
        

def find_file(pathList, extension):
    all_files = list(os.listdir("input"))
    r = re.compile(extension + "$")
    pathList = list(filter(r.search, all_files))
    return pathList

def get_option():
    op = str(input("a)webp\nb)png\nc)jpg\nopcion: "))
    if op.lower() == "a":
        return ".webp"
    elif op.lower() == "b":
        return ".png"
    elif op.lower() == "c":
        return ".jpg"
    else:
        return get_option()

def convertion(files, old_ext=".png", new_ext=".jpeg"):
    
        
    for file in files:
        image = Image.open("input\\" + file)
        if(new_ext == ".jpg"):
            background = Image.new("RGB", image.size, (255,255,255))
            background.paste(image, mask=image.split()[-1])
            
            background.save("output\\" + file.lower().replace(old_ext, new_ext), 'JPEG', quality=85)
        else:
            image.save("output\\" + file.lower().replace(old_ext, new_ext))

    

make_dir("input")
input("Ingrese las imagenes a la carpeta input y presione enter para continuar")
clear()

print("\nSeleccione la extension objetivo:")
old_ext = get_option()
clear()
print("Lista de archivos")

files = []
files = find_file(files, old_ext)
print('\n'.join(map(str, files)))

if not files:
    input("No se han encontrado archivos con esa extension")
    exit()
clear()


print("selecciones la extension a convertir current extension [" + old_ext + "]")
new_ext = get_option()

if new_ext != old_ext:
    make_dir("output")
    convertion(files, old_ext, new_ext)

print("Finalizado")
    


    

