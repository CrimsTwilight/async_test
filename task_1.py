"""
Задача 1: Простая асинхронная функция.
Напишите async-функцию download_data(), которая ждёт 3 секунды (await asyncio.sleep(3))
и затем возвращает "Данные загружены".
Дополнительно: Вызовите её дважды, но без create_task().
Посчитайте, сколько времени выполняется программа.
"""
import asyncio
import time


async def download_data():
    await asyncio.sleep(3)
    return "Данные загружены"

async def main():
    start_time = time.time()

    result1 = await download_data()
    print(result1)

    result2 = await download_data()
    print(result2)

    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time:.2f} секунд.")

if __name__ == "__main__":
    asyncio.run(main())
