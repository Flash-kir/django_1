# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

[Демка сайта](http://flashkir.pythonanywhere.com/).

## Настройки и запуск

* Скачайте код
* Войдите в консоль
* Перейдите в каталог проекта с файлом `manage.py`
* Создайте файл `.env`, заполните переменные:

```bash
SECRET_KEY='django-insecure-s7#fku+@)ra%vqy........*()uyp__%rla*3'
DEBUG=False
ALLOWED_HOSTS=127.0.0.1:8000,127.0.0.1,*.pythonanywhere.com
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
```

* Установите пакеты:

```bash
$ pip install -r requirements.txt
```

* Создайте пользователя БД:

```bash
$ python manage.py createsuperuser
```

* Выполните миграции БД:

```bash
$ python manage.py migrate
```

* Откройте в браузере

В качестве веб-сервера можно использовать что угодно. Например, подойдёт даже самый простой встроенный в Python веб-сервер:

```bash
$ python manage.py runserver
```

## Источники данных, заполнение БД

Фронтенд получает данные в [формате GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON). Все поля здесь стандартные, кроме `properties`. Внутри `properties` лежат специфичные для проекта данные:

* `title` — название локации
* `placeId` — уникальный идентификатор локации, строка или число
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важно лишь чтобы оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый `placeId`, то значит это одно и то же место.

```javascript
<script id='places-geojson' type='application/json'>
  {
    'type': 'FeatureCollection',
    'features': [
      {
        'type': 'Feature',
        'geometry': {
          'type': 'Point',
          'coordinates': [37.62, 55.793676]
        },
        'properties': {
          // Специфичные для этого сайта данные
          'title': 'Легенды Москвы',
          'placeId': 'moscow_legends',
          'detailsUrl': './places/moscow_legends.json'
        }
      },
      // ...
    ]
  }
</script>
```
Адреса в поле `detailsUrl` c подробными сведениями о локации. Каждый раз, когда пользователь выбирает локацию на карте, JS код отправляет запрос на сервер и получает картинки, текст и прочую информацию об объекте. Формат ответа сервера такой:

```javascript
{
    'title': 'Экскурсионный проект «Крыши24.рф»',
    'imgs': [
        'https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg',
        'https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg',
        'https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg',
    ],
    'description_short': 'Хотите увидеть Москву с высоты птичьего полёта?',
    'description_long': '<p>Проект «Крыши24.рф» проводит экскурсии ...</p>',
    'coordinates': {
        'lat': 55.753676,
        'lng': 37.64
    }
}
```

Заполнить данные можно через [панель администра](https://flashkir.pythonanywhere.com/admin/), либо с помощью консольной команды вида:

```bash
$ python manage.py load_place http://адрес/файла.json
```

если название места и координаты будут найдены в БД, то выведется сообщение:

```bash
$ python manage.py load_place 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%20%C2%AB%D0%9A%D1%80%D1%8B%D1%88%D0%B824.%D1%80%D1%84%C2%BB.json'
place Экскурсионный проект «Крыши24.рф» allready exist
```

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com/).