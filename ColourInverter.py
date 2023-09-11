from PIL import Image, ImageOps
from tkinter import Tk, filedialog
import os

# Cria uma janela de seleção de arquivo do Windows
root = Tk()
root.withdraw()  # Oculta a janela principal

# Solicita ao usuário que selecione o arquivo da imagem
nome_arquivo = filedialog.askopenfilename()

try:
    # Tenta carregar a imagem
    imagem = Image.open(nome_arquivo)

    # Inverte as cores da imagem
    imagem_invertida = ImageOps.invert(imagem)

    # Define o nome de saída baseado no nome original
    nome_saida_base = 'imagem_invertida'
    extensao = imagem.format.lower()

    # Verifica se o arquivo de saída já existe
    contador = 1
    nome_saida = f"{nome_saida_base}.{extensao}"
    while os.path.exists(nome_saida):
        nome_saida = f"{nome_saida_base}_{contador}.{extensao}"
        contador += 1

    # Salva a imagem invertida
    imagem_invertida.save(nome_saida)

    # Fecha a imagem original
    imagem.close()

    print(f"Imagem invertida salva com sucesso como '{nome_saida}'!")
except FileNotFoundError:
    print("Arquivo não encontrado. Certifique-se de que o nome do arquivo e o caminho estão corretos.")
except Exception as e:
    print(f"Ocorreu um erro ao processar a imagem: {str(e)}")
