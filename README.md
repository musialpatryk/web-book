# Webbook
BookWeb to serwis internetowy pozwalający poznawać nowe książki oraz je recenzować.

#### Funkcjonalności:
- przeglądanie książek,
- zgłaszanie nowych książek,
- dodawanie recenzji książek,
- przeglądanie recenzji książek,
- przeglądanie autorów.

# Konfiguracja:

## Tworzenie środowiska
1. Utwórz folder dla projektu
2. W folderze wykonaj komendę(`python.py`/`python3` - w zależności od zmiennych środowiskowych):
   - `python -m venv venv`
3. Aktywuj wirtualne środowisko (po poprawnej aktywacji powinien pojawić się napis `venv` na początku lini komend):
   - Linux: `source venv/bin/activate` 
   - Windows: `./venv/bin/activate`.
4. Zainstaluj zależności - `pip install -r requirments.txt`.
5. Sklonuj projekt z gita w miejscu utworzonego folderu.
6. Dodaj dane do bazy danych - patrz "Tworzenie bazy danych od zera"

## Tworzenie bazy danych od zera:
- `python manage.py migrate`
- `python ./commands/run-fixtures.py`
- `python manage.py shell < commands/randomize-images.py` lub alternatywnie `python manage.py shell` i `exec(open('commands/randomize-images.py').read())`

## Przydatne komendy:
- `python manage.py migrate` - tworzenie migracji, tworzy nowe tabele w bazie
- `python manage.py createsuperuser` - tworzy nowego super użytkownika
- `python manage.py loaddata fixtures/fixture_name` - dodaje do bazy danych dane z wskazanego pliku
- `python ./commands/run-fixtures.py` - dodaje początkowe dane na podstawie danych z folderu `fixtures/`
- `pip freeze > requirments.txt` - zapisanie zainstalowanych paczek do pliku `requirments.txt` 
- `python manage.py shell < commands/clear.py` - czyści bazę danych autorów, książek i userów
- `python manage.py runsslserver` - Uruchamia serwer https (wymagane do niektórych dod. funkcjonalności)
- `python commands/resize-images.py` - Ujednolica rozmiar zdjęć (nadpisuje oryginały)
- `python manage.py shell < commands/randomize-images.py` - Losuje zdjęcia z domyślnych dla danych z fixtures'ów

## Użytkownicy
W ramach fixtures'ów dodawani są użytkownicy:

```
Login: admin
Hasło: admin
Grupy: 'admin'
```

```
Login: viewer
Hasło: viewer
Grupy: 'viewer'
```

```
Login: user
Hasło: user
Grupy: brak
```

## Dane do fixtures'ów
Książki wraz z autorami zostały wygenerowane za pomocą [przygotowanej aplikacji]((https://github.com/musialpatryk/web-book-fixtures-generator)) pobierającej dane z Google Book Api i formatującej dane w formacie odpowiadającym potrzebnym fixturesom.

## Gmail Account
- Login: djangoProjectWeb@gmail.com
- Pass: B3dzi3Pi3c?