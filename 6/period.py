import asyncio
import time

async def period_task():
    start_time = time.time() #сохраняем текущее время в переменную
    while time.time() - start_time < 20: #цикл который работаает 20 сек.
        print(f" Задача выполнена в {time.strftime('%H:%M:%S')}") 
        await asyncio.sleep(2) #пауза на 2 сек.
    print(" Периодическая задача завершена.")

if __name__ == '__main__':
    asyncio.run(period_task())
