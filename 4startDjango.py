# python -m venv ll_env - создаем venv
# python3 -m venv --upgrade-deps fashion_venv - допом апгрейдим пип
#
# source ll_env/bin/activate - active venv
#
# deactivate - deact venv
#
# pip install django
#
# django-admin.py startproject learning_log . -creation django project
#
# python manage.py migrate -creation DB
#
# python manage.py runserver -view project

# python manage.py startapp learning_logs -создать инфраструктуру, необходимую для построения приложения

# str1 = '\\dixy.local\dax\Bank\GPB\Выписки\2022\2022.11'
# str2 = '\\dixy.local\dax\Bank\GPB\Выписки\2022\2022.11'
#
# if str1 == str2:
#     print(True)
#
# python manage.py makemigrations
# python manage.py migrate
