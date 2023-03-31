# Функционал по отправке причины отклонения регулирования зазора 

## Дима - это для тебя:
1. В app/templates/reject есть файлы .html
2. В app/static/style.css есть стили
3. Меню навигации в index.html

### Задачи:
- По нажатию по одному из пункто навигации, он должен как-то выделяться среди других (веделение согласно брендбуку РАЗУМА)
- Если на пункте меню УВЕДОМЛЕНИЯ висит класс **.have-notification** это значит, что у него должна быть **href="/reject-form"**, иначе **href="/notification-journal"**

### Файловая структура:

    .
    |-- app
    |   |-- README.md
    |   |-- __init__.py
    |   |-- __pycache__
    |   |   |-- __init__.cpython-310.pyc
    |   |   `-- config.cpython-310.pyc
    |   |-- config.py
    |   |-- main_bp
    |   |   |-- __init__.py
    |   |   |-- __pycache__
    |   |   |   |-- __init__.cpython-310.pyc
    |   |   |   `-- views.cpython-310.pyc
    |   |   `-- views.py
    |   |-- static
    |   |   |-- Sign_green.png
    |   |   `-- style.css
    |   `-- templates
    |       `-- reject
    |           |-- index.html
    |           |-- notification_journal.html
    |           `-- reject_form.html
    |-- app.log
    |-- app.py
    |-- docs
    |   `-- technical_task.txt
    |-- project_tree.txt
    `-- requirements.txt

    8 directories, 19 files
