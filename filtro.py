import cv2
import numpy as np
from matplotlib import pyplot as plt

def manter_objeto_principal(imagem):

    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    imagem_blur = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)  # Reduz os ruídos
    
    # Aplicando um threshold adaptativo para segmentar o objeto do fundo
    mascara = cv2.adaptiveThreshold(imagem_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
  
    kernel = np.ones((5, 5), np.uint8)   # Aqui ocorre as  operações morfológicas para limpar a máscara e realçar o objeto principal

    mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel, iterations=2) 
    
    # Abertura para remover pequenos ruídos ao redor do objeto
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Aqui é criado uma imagem de fundo preto
    fundo_preto = np.zeros_like(imagem)
    
    # Criando uma imagem do objeto em branco
    objeto_branco = np.ones_like(imagem) * 255
    
    # Aplicando a máscara para manter o objeto branco e fundo preto
    resultado = fundo_preto.copy()
    resultado[mascara == 255] = objeto_branco[mascara == 255]
    
    return resultado

def main(caminho_imagem):
   
    imagem = cv2.imread(caminho_imagem)
    if imagem is None:
        print("Erro: Imagem não encontrada ou não pode ser carregada.")
        return

   
    resultado = manter_objeto_principal(imagem)   # Foca no objeto principal

    # Mostra os resultados
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Objeto Principal")
    plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()


if __name__ == "__main__":  
    main('objetos.jpg')
