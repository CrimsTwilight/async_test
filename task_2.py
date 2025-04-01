"""
Задача 2: Параллельное выполнение с create_task().
Возьмите download_data() из первой задачи, но теперь запустите её дважды параллельно,
используя asyncio.create_task().
Дополнительно: Посчитайте, сколько времени теперь выполняется программа.
"""
import asyncio
import time


async def download_data():
    await asyncio.sleep(3)
    return "Данные загружены"

async def main():
    start_time = time.time()

    task1 = asyncio.create_task(download_data())
    task2 = asyncio.create_task(download_data())

    result1 = await task1
    print(result1)

    result2 = await task2
    print(result2)

    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time:.2f} секунд.")

if __name__ == "__main__":
    asyncio.run(main())
