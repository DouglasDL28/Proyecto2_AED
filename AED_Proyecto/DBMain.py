# coding=utf-8
from neo4j import GraphDatabase
from Database import Database
from Classes.Career import *
import tkinter as tk

uri = "bolt://localhost:7687"

driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
db = Database("bolt://localhost:7687", "neo4j","password")

faculty = "Facultad prueba"
career_name = "Prueba"
course = "Ciencias Sociales"
role_model = "Sigmund Freud"
activity = "Leer"

db.createCareer(faculty, career_name, course, role_model, activity)

result = db.getAllType(self, nodeType)


root = tk.Tk()
root.geometry('600x600')
root.title("UVG - Recomendacion de Carreras")

preguntas_dict = {0: ["Matemática", "Respuesta 1.2", "Respuesta 1.3", "Respuesta 1.4"],
                  1: ["Elon Musk", "Respuesta 2.2", "Respuesta 2.3", "Respuesta 2.4"],
                  2: ["Programa", "Respuesta 3.2", "Respuesta 3.3", "Respuesta 3.4"]}

preguntas_list = ["Pregunta 1", "Pregunta 2", "Pregunta 3"]

res = []
answers_list = []

index = tk.IntVar()
resp_var = tk.StringVar()

global final_txt
final_txt = tk.Label(text="")
final_txt.place(x=120, y=250)

global label
label = tk.Label(text=preguntas_list[0])
label.place(x=100, y=150)

global radio1
radio1 = tk.Radiobutton(state='disabled', text=preguntas_dict[0][0], variable=resp_var, value=preguntas_dict[0][0])
radio1.place(x=100, y=200)

global radio2
radio2 = tk.Radiobutton(state='disabled', text=preguntas_dict[0][1], variable=resp_var, value=preguntas_dict[0][1])
radio2.place(x=100, y=250)

global radio3
radio3 = tk.Radiobutton(state='disabled', text=preguntas_dict[0][2], variable=resp_var, value=preguntas_dict[0][2])
radio3.place(x=100, y=300)

global radio4
radio4 = tk.Radiobutton(state='disabled', text=preguntas_dict[0][3], variable=resp_var, value=preguntas_dict[0][3])
radio4.place(x=100, y=350)


def print_():
    if resp_var.get() != "":
        index.set(index.get() + 1)
        print(index.get())
        answers_list.append(resp_var.get())
        print(resp_var.get())
        resp_var.set("")
        if index.get() < 3:
            radio1['text'] = preguntas_dict[index.get()][0]
            radio2['text'] = preguntas_dict[index.get()][1]
            radio3['text'] = preguntas_dict[index.get()][2]
            radio4['text'] = preguntas_dict[index.get()][3]
            label['text'] = preguntas_list[index.get()]
            radio1['value'] = preguntas_dict[index.get()][0]
            radio2['value'] = preguntas_dict[index.get()][1]
            radio3['value'] = preguntas_dict[index.get()][2]
            radio4['value'] = preguntas_dict[index.get()][3]
        else:
            radio1.destroy()
            radio2.destroy()
            radio3.destroy()
            radio4.destroy()
            label.destroy()
            next_.destroy()
            end_.place(x=200, y=450)
            end_['bg'] = 'black'
            final_txt['text'] = "Ya no hay más preguntas, haca clic para ver sus resultados"
            print("Ya no hay mas preguntas")


def recommend_():
    res = []
    query = db.recommend(answers_list[0], answers_list[1], answers_list[2])
    for record in query:
        res.append(Career(record[0]["nombre"], record[0]["facultad"]))
    final = ""
    for rec in res:
        final = rec.name
    final_txt['text'] = final
    end_['text'] = "Salir"
    end_['command'] = exit_
    print(answers_list)


def exit_():
    exit()


def start_():
    radio1.config(state='normal')
    radio2.config(state='normal')
    radio3.config(state='normal')
    radio4.config(state='normal')
    next_.config(state='normal')
    starts_.destroy()


label_0 = tk.Label(text="Escoja una de las respuestas a la pregunta", font="arial 14")
label_0.place(x=70, y=50)

next_ = tk.Button(state='disabled', text="Siguiente", width=15, bg='black', fg='white', command=print_)
next_.place(x=350, y=450)

starts_ = tk.Button(text="Iniciar", width=15, bg='black', fg='white', command=start_)
starts_.place(x=200, y=450)

end_ = tk.Button(text="Ver resultados", width=15, bg='white', fg='white', command=recommend_)
end_.place(x=-50, y=-50)

root.mainloop()
