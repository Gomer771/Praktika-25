from polymorf import DataProcessor

def main():
    file = 'data.csv'  
    processor = DataProcessor(file)

    processor.load_data()
    processor.split_by_location()
    processor.remove_duplicates('Участники гражданского оборота')

if __name__ == '__main__':
    main()
