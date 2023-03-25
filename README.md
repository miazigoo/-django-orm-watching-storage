# Пульт охраны банка
Показывает сотрудников с активными карточками-пропусками, кто в хранилище на данный момент и все визиты по карточке-пропуску
### Как пользоваться
Подразумевается, что Python у вас установлен :
1. Скачать скрипт
2. Установить requirements.txt, введя в консоли 
```buildoutcfg
pip install requirements.txt
```
3. Создать файл `.env` 
4. В файле `.env` записать данные для подключения к БД:

 ```buildoutcfg
DB_ENGINE=YOUR_DB_ENGINE
DB_HOST=YOUR_DB_HOST
DB_PORT=YOUR_DB_PORT_int
DB_NAME=YOUR_DB_NAME
DB_USER=YOUR_DB_USER
DB_PASSWORD=YOUR_DB_PASSWORD
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=BOOL (true or false)
```
5. Запустить файл введя в консоли
```buildoutcfg
python manage.py runserver
```

Для изменения времени подозрительных визитов в файле `passcard_info_view.py` необходимо указать нужное кол-во в минутах 
```py
'is_strange': visit.is_visit_long(minutes=60)
```
Зайти на сайт можно по адресу [127.0.0.1:8000](http://127.0.0.1:8000)
* Приятного пользования

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).