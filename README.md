# electronics_chain

    Сеть по продаже электроники

# Cтек

     Django-4.2.1, Python 3.10.7, postgres (PostgreSQL) 14.6 (Homebrew)

# Запуск проекта

    python manage.py startapp to_do_list
    ./manage.py startapp core electronics_chain/core
    ./manage.py startapp base electronics_chain/base
    ./manage.py startapp factory electronics_chain/factory
    ./manage.py startapp retailer electronics_chain/retailer
    ./manage.py startapp individual_entrepreneur electronics_chain/individual_entrepreneur

# Миграции

    ./manage.py makemigrations -name 'Name of action in magration'- создаем миграции
    ./manage.py migrate - накатываем миграции

# Create Superuser

    python manage.py createsuperuser

