﻿# playwright-tests

Для запуска должен быть установлен python 3.X.X и pip
1. Подтянуть зависимости
pip install -r requirements.txt
2. Установить браузер для запуска тестов
playwright install для скачивания браузеров плея

P.S. По умолчанию тесты запускаются в headless режиме, для запуска тестов
в отображаемом окне браузера добавить флаг --headed

**Запуск тестов** 

pytest base_test.py

**Генерация отчета**

Отчет заранее сгенерирован, запусить в браузере index.html из allure-report



Главная страница:
https://stage.skies.land/

**Кейсы:**
1. Открыть главную страницу, залогиниться
перейти на страницу проектов по кнопке Проекты
ввести в поле поиск “привет”
в результатах поиска должен быть один проект и один пост
перейти на проект

2. Открыть главную страницу, залогиниться
На главной в разделе популярные проекты должно быть 6 проектов
перейти на первый из них, проверить наличие разделов Об авторе, Блог и Сообщество Автора проекта, а также наличие кнопки Поддерживать
на странице проекта перейти в раздел Блог и оставить коментарий на последний пост, проверить отображение
нажать кнопку поддержать, проверить переход на страницу поддержки

3. Открыть главную страницу, залогиниться
На главной в разделе популярные проекты
перейти на первый из них
на странице проекта нажать кнопку Отслеживать (звездочка), должна изменить стиль
перейти по кнопке избранные проекты на этой же странице и проверить что проект там появился
удалить его из закладок (нажать звездочку)

4. сформировать отчет,
5. возможность интеграции CI,
6. предложения что можно улучшить

фреймворк по выбору, код на github, инструкции по запуску

Что улучшить
1. Добавить со стороны разработки id или флаги за которые можно цепляться
при написании локаторов
2. Попробовать ассинхронные методы, параллельность тестов
3. Порефачить фикстуры
4. Вынести креды в переменные окружения ci/cd
5. Улучшить локаторы, сделать более универсальными и точными
6. Убрать явные ожидания(тесты в добавлении в избранное пример)
7. Сделать подробнее отчет, добавить вложения
8. Добавить логирование для тестов


**Баги:**

    1. При отправке комментария, он не добавляется в реальном времени, нужно перегружать страницу
    2. При удалении проекта из Избранные проекты, состояние кнопки не изменяется.
    Проект удаляется, но при переходе на главную страницу проекта, кнопка Добавить в
    избранное имеет стиль добавленного проекта.
    3. При нажатии 2 раза на добавление в избранное, ошибка с сервером
    4. Сообщество Автора проекта это что вообще?)) (посмотрите локаторы в веб инспекторе)
