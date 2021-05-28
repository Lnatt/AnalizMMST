import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl


def Create_Table():
    df = pd.DataFrame({'Name': ['Ivan', 'Ignat', 'Anna', 'Yulia', 'Stas'],
                       'City': ['Azov', 'Bataysk', 'Rostov-na-Donu', 'Rostov-na-Donu', 'Rostov-na-Donu'],
                       'Ege ball': [277, 265, 254, 252, 243],
                       'Avg_ball': [4.65, 5.0, 4.05, 3, 2.87],
                       'End learn': [1, 1, 1, 1, 0],
                       'Medal': [1, 0, 0, 1, 0]})
    df.to_excel('./test.xlsx')


def Print_Table():  # Вывод таблицы
    print(pd.read_excel('./test.xlsx'))


def Avg_Ege():  # Среднее значение баллов по Егэ и график с результатами
    k = (pd.read_excel('./test.xlsx', usecols=[3]))
    print("Среднее значение балла ЕГЭ ", k.mean())
    ege_ball = pd.read_excel('./test.xlsx', usecols=[3])
    print(ege_ball)
    x = np.arange(len(ege_ball))
    plt.plot(x, ege_ball)
    plt.show()

def City(): #Статистика по городам
    city = pd.read_excel('./test.xlsx', usecols=[2], header=None)
    print(city.value_counts())
    labels = city.value_counts().array
    values = city.value_counts().values
    colors = ['yellow', 'green', 'red', 'blue']
    plt.pie(values, labels=labels, colors=colors)
    plt.axis('equal')
    plt.show()

    #values = city.value_counts().values
    #index = city.value_counts().values.flat
    #plt.bar(index, values)
    #plt.show()

def End_learn(): # Зависимость окончания университета от баллов ЕГЭ
    end_learn = pd.read_excel('./test.xlsx', usecols=[5])
    ege_end = pd.read_excel('./test.xlsx', usecols=[3])
    p1 = (end_learn.to_string(index=False, header=None))
    p2 = (ege_end.to_string(index=False, header=None))
    print(type(p1))
    p11 = p1.split() #преобразуем в лист чтобы брать мин и макс
    p22 = p2.split() #преобразуем в лист чтобы брать мин и макс
    print(type(p11))
    print(type(p22))
    print(p22)
    print(p11)
    x1 = int(min(p22))
    x2 = int(max(p22))
    print(type(x1))
    interval = np.arange(x1, x2)
    print(interval)
    plt.plot(interval)
    plt.show()

def Create_Window():
    window = tk.Tk()
    window.geometry('400x400')
    window.title("AnalizMMST")

    btn1 = tk.Button(window, text="Вывести таблицу", command=Print_Table)  # Вывод таблицы
    btn1.grid(column=1, row=0)
    btn2 = tk.Button(window, text="Средний балл ЕГЭ", command=Avg_Ege)  # Средний балл егэ
    btn2.grid(column=2, row=0)
    btn2 = tk.Button(window, text="Город", command=City)  # Статистика поступающих по городам
    btn2.grid(column=3, row=0)
    btn2 = tk.Button(window, text="Осилили", command=End_learn)  # Окончание университета, зависимость от егэ
    btn2.grid(column=4, row=0)

    window.mainloop()


def main():
    Create_Table()
    Print_Table()
    Create_Window()

if __name__ == "__main__":
    main()
