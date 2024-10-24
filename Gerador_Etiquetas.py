import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog  # Importa filedialog para escolher o local de salvamento
from ttkbootstrap import Style
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color

# Função para gerar o PDF
def gerar_etiqueta(nome, quantidade, empresa, layout):
    try:
        # Abre uma janela para escolher o local e o nome do arquivo
        arquivo_saida = filedialog.asksaveasfilename(
            defaultextension=".pdf", 
            filetypes=[("PDF files", "*.pdf")], 
            title="Salvar Etiqueta Como"
        )
        if not arquivo_saida:  # Se o usuário cancelar a operação
            return
        
        if layout == "A4 Inteira":
            c = canvas.Canvas(arquivo_saida, pagesize=landscape(A4))
            largura_pagina, altura_pagina = landscape(A4)
            largura_imagem = 250 * 2.83465
            altura_imagem = 110 * 2.83465
            posicao_x_imagem = (largura_pagina - largura_imagem) / 2
            etiquetas_por_pagina = 1
            largura_etiqueta = largura_pagina
            altura_etiqueta = altura_pagina
            cor_fonte = Color(0.447, 0.451, 0.459)

            x = 0  
            y = altura_pagina - altura_etiqueta  
            texto_y_offset = 56.69

            c.setFont("Helvetica-Bold", 48)
            c.setFillColor(cor_fonte)

            conteudo = f"CONTÉM {quantidade} unid".upper() if quantidade else ""
            nome_produto = nome.upper()
            nome_empresa = empresa.upper()

            if conteudo:
                c.drawCentredString(largura_etiqueta / 2 + x, y + altura_etiqueta - texto_y_offset, conteudo)
            c.drawCentredString(largura_etiqueta / 2 + x, y + altura_etiqueta - texto_y_offset - 60, nome_produto)
            c.drawCentredString(largura_etiqueta / 2 + x, y + altura_etiqueta - texto_y_offset - 120, nome_empresa)

            c.drawImage("img/dados.jpg", posicao_x_imagem, y + 10, width=largura_imagem, height=altura_imagem)

        elif layout == "1/2 A4 (Duas etiquetas)":
            c = canvas.Canvas(arquivo_saida, pagesize=A4)
            largura_pagina, altura_pagina = A4  
            largura_etiqueta = largura_pagina  
            altura_etiqueta = altura_pagina / 2  
            etiquetas_por_pagina = 2  
            cor_fonte = Color(0.447, 0.451, 0.459)

            for i in range(etiquetas_por_pagina):
                x = 0  
                y = altura_pagina - altura_etiqueta * (i + 1)
                texto_y_offset = 40  

                c.setFont("Helvetica-Bold", 36)
                c.setFillColor(cor_fonte)

                conteudo = f"CONTÉM {quantidade} unid".upper() if quantidade else ""
                nome_produto = nome.upper()
                nome_empresa = empresa.upper()

                if conteudo:
                    c.drawCentredString(largura_etiqueta / 2 + x, y + altura_etiqueta - texto_y_offset, conteudo)
                c.drawCentredString(largura_etiqueta / 2 + x, y + altura_etiqueta - texto_y_offset - 40, nome_produto)
                c.drawCentredString(largura_etiqueta / 2 + x, y + altura_etiqueta - texto_y_offset - 80, nome_empresa)

                largura_imagem = 200 * 2.83465
                altura_imagem = (largura_imagem * 110) / 250  
                posicao_x_imagem = (largura_etiqueta - largura_imagem) / 2  
                c.drawImage("img/dados.jpg", posicao_x_imagem, y + 10, width=largura_imagem, height=altura_imagem)

        else:
            c = canvas.Canvas(arquivo_saida, pagesize=landscape(A4))
            largura_pagina, altura_pagina = landscape(A4)  
            largura_etiqueta = largura_pagina / 2  
            altura_etiqueta = altura_pagina / 2  
            cor_fonte = Color(0.447, 0.451, 0.459)

            for i in range(4):
                x = (i % 2) * largura_etiqueta  
                y = altura_pagina - altura_etiqueta * (i // 2 + 1)  
                texto_y_offset = 20 * 2.83465  

                c.setFont("Helvetica-Bold", 20)  
                c.setFillColor(cor_fonte)  

                conteudo = f"CONTÉM {quantidade} unid".upper() if quantidade else ""
                nome_produto = nome.upper()
                nome_empresa = empresa.upper()

                if conteudo:
                    c.drawCentredString(x + largura_etiqueta / 2, y + altura_etiqueta - texto_y_offset, conteudo)
                c.drawCentredString(x + largura_etiqueta / 2, y + altura_etiqueta - texto_y_offset - 20, nome_produto)
                c.drawCentredString(x + largura_etiqueta / 2, y + altura_etiqueta - texto_y_offset - 40, nome_empresa)

                largura_imagem = 125 * 2.83465
                altura_imagem = 55 * 2.83465
                posicao_x_imagem = x + (largura_etiqueta - largura_imagem) / 2  
                c.drawImage("img/dados.jpg", posicao_x_imagem, y + 10, width=largura_imagem, height=altura_imagem)

        c.save()
        messagebox.showinfo("Sucesso", "Etiqueta gerada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função chamada pelo botão
def gerar_pdf():
    nome = entry_nome.get().upper()
    quantidade = entry_quantidade.get().strip()  
    empresa = entry_empresa.get().upper()
    layout = combo_layout.get()

    if nome and empresa:
        gerar_etiqueta(nome, quantidade, empresa, layout)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos corretamente.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Etiquetas")

# Estilo moderno
style = Style(theme="flatly")

# Entrada para o nome do produto
ttk.Label(root, text="Nome do Produto:").grid(column=0, row=0, padx=10, pady=10)
entry_nome = ttk.Entry(root)
entry_nome.grid(column=1, row=0, padx=10, pady=10)

# Entrada para a quantidade
ttk.Label(root, text="Quantidade:").grid(column=0, row=1, padx=10, pady=10)
entry_quantidade = ttk.Entry(root)
entry_quantidade.grid(column=1, row=1, padx=10, pady=10)

# Entrada para o nome da empresa
ttk.Label(root, text="Nome da Empresa:").grid(column=0, row=2, padx=10, pady=10)
entry_empresa = ttk.Entry(root)
entry_empresa.grid(column=1, row=2, padx=10, pady=10)

# Combo box para seleção do layout
ttk.Label(root, text="Layout:").grid(column=0, row=3, padx=10, pady=10)
combo_layout = ttk.Combobox(root, values=["A4 Inteira", "1/2 A4 (Duas etiquetas)", "1/4 A4 (Quatro etiquetas)"], state="readonly")
combo_layout.grid(column=1, row=3, padx=10, pady=10)
combo_layout.current(0)  # Define o layout padrão

# Botão para gerar o PDF
btn_gerar = ttk.Button(root, text="Gerar Etiqueta", command=gerar_pdf)
btn_gerar.grid(column=0, row=4, columnspan=2, padx=10, pady=20)

# Iniciar a interface gráfica
root.mainloop()
