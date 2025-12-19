# Парсер Политических Партий Минюста РФ

Парсер официального списка **политических партий России** с сайта Министерства юстиции РФ.

## 🎯 Что извлекает программа
Для **каждой партии**:
- ✅ **Название** партии
- ✅ **Ссылка** на страницу/документ партии

## 📡 Источник данных
**Официальный сайт Минюста РФ**:
https://minjust.gov.ru/ru/pages/politicheskie-partii/

1. requests отправляет HTTP GET-запрос
URL = "https://minjust.gov.ru/ru/pages/politicheskie-partii/"

response = requests.get(URL, headers=headers)

2. Получаем HTML-код страницы

html_content = response.text

3. BeautifulSoup парсит HTML в дерево объектов

soup = BeautifulSoup(html_content, 'html.parser')

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий
git clone https://github.com/yourusername/parse-parties.git

cd partii

### 2. Установите виртуальное окружение
**Windows:**
python -m venv partii_venv

partii_venv\Scripts\activate

**macOS/Linux:**
python3 -m venv partii_venv

source partii_venv/bin/activate

### 3. Установите зависимости
pip install -r requirements.txt

### 4. Запустите парсер
python parse_parties.py

результат выводится в консоль (список словарей)