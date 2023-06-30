from tkinter import *
root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.janela()
        self.dados()
        root.mainloop()

    def janela(self):
        self.root.title("Calcular a Velocidade Média")
        self.root.configure(background='sky blue')
        self.root.geometry("300x200")
        self.root.resizable(False, False)

    def dados(self):
        # Criação da label e entrada do Espaço
        self.espaco = DoubleVar()
        self.lb_espaco = Label(text="Espaço (em KM)",
                               bg='#dfe3ee', fg='#107db2')
        self.lb_espaco.place(relx=0.05, rely=0.05)
        self.espaco_entry = Entry(textvariable=self.espaco)
        self.espaco_entry.place(relx=0.5, rely=0.05, relwidth=0.25)
        # Criação da label e entrada do Número
        self.tempo = DoubleVar()
        self.lb_tempo = Label(text="Tempo (em horas)",
                              bg='#dfe3ee', fg='#107db2')
        self.lb_tempo.place(relx=0.05, rely=0.2)
        self.tempo_entry = Entry(textvariable=self.tempo)
        self.tempo_entry.place(relx=0.5, rely=0.2, relwidth=0.25)

        # Butão
        self.bt_calcular1 = Button(text="Calcular", bd=2,
                                   bg='#107db2', fg='white',
                                   font=('verdana', 8, 'bold'),
                                   command=self.butaoclick1)

        self.bt_calcular1.place(relx=0.35, rely=0.6,
                                relwidth=0.2, relheight=0.15)
        # Resultado
        self.velocidade1 = StringVar()
        self.resultado1 = Label(textvariable=self.velocidade1)
        self.lb_resultado = Label(
            text="Velocidade Média (km/h)", bg='#dfe3ee', fg='#107db2')
        self.lb_resultado.place(relx=0.05, rely=0.4)

        self.resultado1 = Label(textvariable=self.velocidade1)
        self.resultado1.place(relx=0.55, rely=0.4, relwidth=0.2)

    def butaoclick1(self):
        e = self.espaco.get()
        t = self.tempo.get()
        velocidade = round((e/t), 2)
        return self.velocidade1.set(velocidade)


Application()
