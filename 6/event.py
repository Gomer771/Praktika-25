import threading
import time

start_event = threading.Event()

#создаём потоки
def worker(thread_num):
    print(f"[Поток {thread_num}] готов")
    start_event.wait() #поток приостанавлиается и ожидает
    print(f"[Поток {thread_num}] начал работу")
    time.sleep(1)

def main():
    threads = [] #пустой список для хранения объектов потоков
    for i in range(10): #цикл для создания 10 потоков
        t = threading.Thread(target=worker, args=(i+1,)) #создаём поток
        threads.append(t)
        t.start()

    time.sleep(2)  #поток ждёт 2 секунды 
    print("Все потоки начинают работу")
    start_event.set()

#ожидаем завершения всех потоков
    for t in threads:
        t.join()
    print(" Все потоки завершили работу.")

if __name__ == '__main__':
    main()
