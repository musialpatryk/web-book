# web-book-api

Przygotowanie środowiska:
- utwórz folder
- w folderze wykonaj komendę python -m venv venv (python/py - w zależności od zmiennych środowiskowych)
- aktywuj venv (Linux: source venv/bin/activate; Windows: ./venv/bin/activate)
  (po poprawnej aktywacji powinien pojawić się napis "venv" na początku lini komend)
- zainstaluj django - pip install django
- zainstaluj rest'a - pip install djangorestframework
- ściągamy projekt z gita i wrzucamy go do utworzonego folderu
- file -> settings -> Python Interpreter - wybierz odpowiedni interpreter
- w zakładce "Edit configuration" w polu Script path ustaw ściężkę na plik manage.py a w Parameters "runserver"
<br>
- gdyby coś wam się przypomniało to dodajcie, bo nie pamiętam czy jeszcze jakiś komend używaliśmy
<br>
<br>
- python manage.py migrate - tworzenie migracji, tworzy nowe tabele w bazie (w przypadku nowego projektu)
- python manage.py createsuperuser - tworzy nowego użytkownika (w przypadku nowego projektu)
<br>
Obecnie stworzony user: admin / admin
