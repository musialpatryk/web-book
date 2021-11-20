# Webbook

## Info
Każda zmiana to nowy Branch - NIE DODAJEMY DO MAINA!!!

### Poradniki:
- https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc

# Konfiguracja:

## Tworzenie środowiska
1. utwórz folder dla projektu
2. w folderze wykonaj komendę(`python.py`/`python3` - w zależności od zmiennych środowiskowych):
   - `python -m venv venv`
3. Aktywuj wirtualne środowisko (po poprawnej aktywacji powinien pojawić się napis `venv` na początku lini komend):
   - Linux: `source venv/bin/activate` 
   - Windows: `./venv/bin/activate`.
4. Zainstaluj zależności - `pip install -r requirments.txt`.
5. Sklonuj projekt z gita w miejscu utworzonego folderu.
   - file -> settings -> Python Interpreter - wybierz odpowiedni interpreter
   - w zakładce "Edit configuration" w polu Script path ustaw ściężkę na plik manage.py a w Parameters "runserver" <br>
   - gdyby coś wam się przypomniało to dodajcie, bo nie pamiętam czy używaliśmy jeszcze jakiś komend <br><br>
6. Dodaj dane do bazy danych - patrz "Tworzenie bazy danych od zera"

### Przydatne komendy:
- `python manage.py migrate` - tworzenie migracji, tworzy nowe tabele w bazie
- `python manage.py createsuperuser` - tworzy nowego super użytkownika
- `python manage.py loaddata fixtures/fixture_name` - dodaje do bazy danych dane z wskazanego pliku
- `python ./commands/run-fixtures.py` - dodaje początkowe dane na podstawie danych z folderu `fixtures/`
- `pip freeze > requirments.txt` - zapisanie zainstalowanych paczek do pliku `requirments.txt` 
- `python manage.py shell < commands/clear.py` - czyści bazę danych autorów, książek i userów

# Tworzenie bazy danych od zera:
- `python manage.py migrate`
- `./commands/run-fixtures.sh`

### Admin user
W ramach fixtures'ów dodwany jest użytkownik:
```
Login: admin
Hasło: admin
Grupy: 'viewers', 'admin'
```