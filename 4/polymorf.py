#вариант 5


import pandas as pd

class DataProcessor:
    def __init__(self, file):
        self.file = file

     #загружаем csv    
    def load_data(self):
        self.data = pd.read_csv(self.file)

        #разделяем по столбцу "Место оплаты"
        minsk_df = self.data[self.data['Место оплаты'] == 'Минск']
        regions_df = self.data[self.data['Место оплаты'] != 'Минск']

        #сохраненяем в отдельные файлы
        minsk_df.to_csv('minsk.csv', index=False)
        regions_df.to_csv('ne minsk.csv', index=False)

    def remove_duplicates(self, column_name):
        if self.data is None:
            print("Нет данных")
            return

        #количества дубликатов
        initial_count = len(self.data)
        self.data.drop_duplicates(subset=[column_name], inplace=True)
        final_count = len(self.data)
        removed = initial_count - final_count

        print(f"Количество удалённых дубликатов по столбцу '{column_name}': {removed}")

