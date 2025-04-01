"""
Задача 3: Загрузка нескольких ссылок с asyncio.gather().
Напишите async-функцию fetch_data(url), которая принимает адрес сайта и имитирует его загрузку,
await asyncio.sleep(от 1 до 3 секунд).
Дополнительно: Запустите fetch_data() для списка сайтов параллельно, используя asyncio.gather().
"""
import asyncio
import time
import random


async def fetch_data(url):
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    return f"Данные с {url} загружены за {delay} сек."

async def main():
    start_time = time.time()

    urls = ["https://site1.com", "https://site2.com", "https://site3.com", "https://site4.com"]
    tasks = [fetch_data(url) for url in urls]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} секунд.")

if __name__ == "__main__":
    asyncio.run(main())
