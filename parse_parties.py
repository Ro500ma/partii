import requests  # Импорт библиотеки для HTTP-запросов
from bs4 import BeautifulSoup  # Импорт библиотеки для парсинга HTML

parties = []  # Создаем пустой список для хранения данных о партиях

# URL целевой страницы
url = "https://minjust.gov.ru/ru/pages/politicheskie-partii/"
# Заголовки для HTTP-запроса (имитация браузера)
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/127.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

try:
    # Отправка GET-запроса к сайту с таймаутом 10 секунд
    response = requests.get(url, headers=headers, timeout=10)
except requests.exceptions.RequestException as e:
    # Обработка ошибок сети/запроса
    print(e)

# Создание объекта BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Поиск первого нумерованного списка (тег <ol>) на странице
list = soup.find('ol')

# Поиск всех элементов списка (тегов <li>) внутри найденного списка
list_items = list.find_all('li')

# Цикл по каждому элементу списка
for item in list_items:
    # Поиск ссылки (<a>) внутри текущего элемента списка
    link_tag = item.find('a')
    
    # Извлечение значения атрибута href (ссылки)
    tag_url = link_tag.get('href')
    
    # Проверка наличия ссылки
    if tag_url:
        # Если ссылка уже абсолютная (начинается с http)
        if tag_url.startswith('http'):
            item_url = tag_url  # Используем как есть
        else:
            # Иначе делаем абсолютной, добавляя базовый URL
            item_url = "https://minjust.gov.ru" + tag_url
    else:
        # Если ссылки нет, устанавливаем None
        item_url = None
    
    # Извлечение текста ссылки (название партии)
    # .strip() - удаление пробелов по краям
    # .replace('\xa0', ' ') - замена неразрывных пробелов на обычные
    party_name = link_tag.get_text().strip().replace('\xa0', ' ')
    
    # Добавление словаря с данными партии в список
    parties.append({
        "name": party_name,      # Название партии
        "doc_url": item_url      # Ссылка на документ (или None)
    })

# Вывод всех собранных данных в консоль
print(parties)
