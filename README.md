# SF_test_project
API для системы опросов пользователей.

test/ - создание теста(опроса) POST

{
    "test_name": "test_1"
    "date_start": "2021-02-09T23:00:58Z",
    "date_end": "2021-02-09T23:00:58Z",
    "test_description": "Описание"
}

test/<int:pk>/ - удаление, изменение опроса PUT DELETE

##################################################################################

question/ создание вопроса к тесту. POST

{
    "id": 1,
    "test": 1,
    "question_text": "Вопрос",
    "question_type": "one"
} 

*тип вопроса (one - можно выбрать только один вариан, multiple - можно выбрать несколько вариантов ответа, text - один вариант ответ)

question/<int:pk>/ - удалить, изменить вопрос PUT DELETE

######################################################################################

answer/ - добавить ответ, вывести все ответы пользователя. POST, GET.
{
    "id": 1,
    "user_id": 1,
    "test": 1,
    "question": 1,
    "choice": 1,
    "choice_text": "Ответ"
}
answer/<int:pk>/ удалить ответ пользователя. DELETE.
answer/ivew/<int:user_id>/ отображение ответов ананимного пользователя.

###################################################################################

choice/ - добавить ответ на вопрос(заготовка) POST

{
    "id": 1,
    "question": 1,
    "choice_text": "Ответ"
}

choice/<int:pk>/ удалить и изменить заготовленный ответ. PUTE, DELETE.


Инструкция по разворачиванию приложения (локально):

Создать виртуальное окружение:
~ $ python3 -m venv env
~ $ source env/bin/activate
~ $ python -m pip install -r requirements.txt
~ $ python manage.py migrate
~ $ python manage.py createsuperuser
~ $ python manage.py runserver
