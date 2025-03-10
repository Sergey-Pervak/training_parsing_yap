import datetime
from time import sleep

# Импортируйте библиотеку requests_cache.
import requests_cache

# TIME_API_URL = 'http://worldtimeapi.org/api/'
TIME_API_URL = 'https://timeapi.io/api/'

if __name__ == '__main__':
    # Создайте сессию, кеширующую результаты загрузки страниц.
    session = requests_cache.CachedSession()
    # Уточнение местоположения.
    # vostok_url = TIME_API_URL + 'timezone/Antarctica/Vostok'
    vostok_url = TIME_API_URL + 'timezone/zone?timeZone=Antarctica/Vostok'
    # Загружаем текущее время станции "Восток" пять раз.
    for iteration in range(5):
        # После третьей загрузки — очистка кеша.
        if iteration > 2:
            # Очистите кеш.
            session.cache.clear()
        # Загрузите веб-страницу из переменной vostok_url,
        # используя созданную сессию.
        response = session.get(vostok_url)
        # Ответ от сервера приходит в формате JSON,
        # поэтому нужно преобразовать его методом .json(),
        # чтобы дальше работа велась с данными, как со словарём.
        data = response.json()
        # Получение текущего времени на станции "Восток".
        # result = data.get('datetime')
        result = data.get('currentLocalTime')
        # Печать номера итерации и текущего времени.
        print(iteration, result)
        # Пауза на одну секунду.
        sleep(1)
    # Получение часового пояса.
    # utc_offset = data.get('utc_offset')
    standardutc_offset = data.get('standardUtcOffset')
    utc_offset = standardutc_offset.get('seconds')
    print_utc_offset = datetime.timedelta(seconds=utc_offset)
    # Печать часового пояса.
    print('Часовой пояс антарктической станции «Восток»:', print_utc_offset)
