import multiprocessing
import random
import string

def multi_process(shared_dict, process_num):
    for _ in range(5): #цикл с 5-ю итерациями
        line = ''.join(random.choices(string.ascii_letters, k=6)) #генирируем случайную строку из 6 букв 
        print(f" Процесс: {line}")

def main():
    with multiprocessing.Manager() as manager: #cоздаём менеджер
        shared_dict = manager.dict() #общий словарь для всех процессов
        processes = [] #пустой список

#запуск 5 процесссов
        for i in range(5):
            p = multiprocessing.Process(target=multi_process, args=(shared_dict, i+1))
            processes.append(p)
            p.start()

#ожидаем завершения всех процессов
        for p in processes:
            p.join()

if __name__ == '__main__':
    main()
