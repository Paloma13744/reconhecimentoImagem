# Reconhecimento de Imagem

Este projeto é uma implementação em Python que utiliza OpenCV para manter o objeto principal de uma imagem, removendo o fundo e realçando o objeto de interesse. É uma ferramenta útil para aplicações de processamento de imagem onde a identificação do objeto principal é necessária.

## Tecnologias

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-blue.svg)

## Descrição do Código

O código realiza os seguintes passos:

1. **Leitura da Imagem**: Carrega a imagem de entrada utilizando OpenCV.
2. **Conversão para Escala de Cinza**: Converte a imagem para escala de cinza para simplificar o processamento.
3. **Desfoque Gaussian**: Aplica um filtro de desfoque gaussiano para reduzir ruídos na imagem.
4. **Threshold Adaptativo**: Utiliza um threshold adaptativo para segmentar o objeto do fundo.
5. **Operações Morfológicas**: Aplica operações morfológicas (fechamento e abertura) para limpar a máscara e realçar o objeto.
6. **Criação do Resultado**: Gera uma nova imagem onde o objeto principal é mantido em branco e o fundo é preto.

## Como Usar

Para usar este projeto, você precisará do Python e das bibliotecas necessárias instaladas. Você pode instalar as bibliotecas necessárias com o seguinte comando:

```bash
pip install opencv-python numpy matplotlib
```
## Executando o Código
Clone o repositório:
```bash
git clone https://github.com/Paloma13744/reconhecimentoImagem.git
```
