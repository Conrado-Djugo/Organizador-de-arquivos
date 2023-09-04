import os
import shutil
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma Pasta")

lista_de_arquivos = os.listdir(caminho)


locais = {
    "imagens": [".png", ".jpeg", ".jpg", ".gif", ".webp", ".bitmap", ".tiff", ".raw" ".ppm", ".exif", ".pgm", ".pbm", ".pnm", ".bmp"],
    "pdfs": [".pdf"],
    "arquivos": [".pptx", ".zip", ".cdr", ".doc", ".docx", ".psd"],
    "programas": [".exe"],
    "musicas e videos":[".mp3", ".mp4", ".m4a"]
}

for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")    