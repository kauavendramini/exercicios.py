import tkinter as tk

# Função para clicar nos botões
def clicar(valor):
    entrada.insert(tk.END, valor)

# Função para calcular resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para limpar
def limpar():
    entrada.delete(0, tk.END)

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

# Campo de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 20), justify="right")
entrada.pack(pady=10)

# Frame para botões
frame = tk.Frame(janela)
frame.pack()

# Botões
botoes = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

linha = 0
coluna = 0

for botao in botoes:
    if botao == "=":
        tk.Button(frame, text=botao, width=5, height=2, font=("Arial", 14),
                  command=calcular).grid(row=linha, column=coluna)
    else:
        tk.Button(frame, text=botao, width=5, height=2, font=("Arial", 14),
                  command=lambda b=botao: clicar(b)).grid(row=linha, column=coluna)

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Botão limpar
tk.Button(janela, text="C", width=20, height=2, command=limpar).pack(pady=10)

janela.mainloop()