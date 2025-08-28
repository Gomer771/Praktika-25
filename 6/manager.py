import multiprocessing
import random
import string

def multi_process(shared_dict, process_num):
    for _ in range(5):  #каждый процесс добавляет 5 записей
        key = f"key_{process_num}_{random.randint(1, 100)}" #создание уникального ключа
        value = ''.join(random.choices(string.ascii_letters, k=6)) #генерируем случайную строку
        shared_dict[key] = value #добавлям пару в общий словарь
        print(f"[Процесс {process_num}] - {key}: {value}")
        
def main():
    with multiprocessing.Manager() as manager: #cоздаём менеджер
        shared_dict = manager.dict() #общий словарь для всех процессов
        processes = [] #пустой список

#запуск 10 процесссов
        for i in range(10):
            p = multiprocessing.Process(target=multi_process, args=(shared_dict, i+1))
            processes.append(p)
            p.start()

#ожидаем завершения всех процессов
        for p in processes:
            p.join()

if __name__ == '__main__':
    main()
