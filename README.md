# moutain-peaks

## installation
(python 3.6.6, pip and sqlite3 were already installed)

<ul>
  <li>python -m pip install Django</li>
  <li>django-admin startproject apirest</li>
  <li>python manage.py startapp peaks</li>
  <li>python manage.py migrate</li>
  <li>python manage.py makemigrations peaks</li>
  <li>python manage.py migrate</li>
  <li>python manage.py createsuperuser</li>
  <li>.mode csv; .separator ";"; .import peaks_location.csv peaks_peaklocation;</li>
</ul>

## execution

<ul>
  <li>python manage.py runserver</li>
</ul>