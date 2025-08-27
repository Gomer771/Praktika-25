import pandas as pd
import matplotlib.pyplot as plt

class Players:
    def __init__(self, file):
        self.file = file
        self.data = None #переменная для датафрейма

#загружаем csv файл и ловим ошибки 
    def load_data(self):
        try:
            self.data = pd.read_csv(self.file)
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

#проверяем загруженны ли данные
    def data_check(self):
        if self.data is None:
            print("Данные не загружены.")
            return

    #группируем по стране и считаем количество игроков
        country_counts = self.data['country'].value_counts()

    #строим диаграмму
        plt.figure(figsize=(8, 8)) #создаём квадратное поле со сторонами 8
        plt.pie(
            country_counts.values, #размеры секторов
            labels=country_counts.index, #названия стран
            autopct='%1.0f%%', #формат отображения процентов
            colors=['blue', 'green', 'red', 'gold', 'orange', 'purple', 'yellow', 'black', 'pink'] #цвета секторов
        )
        plt.title('Количество игроков PS') #заголовок
        plt.show() #вывод 

