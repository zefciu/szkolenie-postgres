===================================================
Plan szkolenia z PostgreSQL dla Lasów Państwowych
===================================================

Administracja baz danych – 2 dni
---------------------------------

Dzień 1
""""""""

1. Instalacja PostgreSQL
2. Podstawowa konfiguracja klastra
3. Metody uruchamiania i zatrzymywania serwera
4. Tworzenie i administracja ról, globalne uprawnienia
5. Tworzenie baz danych, tabel, uprawnienia dla baz i tabel
6. Omówienie tabel katalogu
7. Ćwiczenia praktyczne – instalacja i konfiguracja bazy danych według wymagań

Dzień 2
"""""""""

1. Zagadnienia optymalizacji, vacuum, autovacuum, analyze
2. Blokady
3. Backup i odzyskiwanie baz danych
4. Import danych przestrzennych
5. Replikacja i HA, różne konfiguracje
6. Ćwiczenia praktyczne – konfiguracja i testowanie różnych rozwiązań typu HA


Programowanie baz danych – 2 dni
-----------------------------------

Dzień 1
""""""""

1. Podstawowa struktura funkcji PL/pgSQL, 
2. Deklaracje zmiennych, argumenty, aliasy.
3. Wykonywanie zapytań, zapytania bez rezultatu, zapytania dynamiczne
4. Obsługa wyników zapytań
5. Instrukcje sterujące
6. Obsługa błędów
7. Ćwiczenie praktyczne (funkcje obsługujące nested set model)

Dzień 2
""""""""
1. Deklaracje wyzwalaczy
2. Transakcje, kursory
3. Ćwiczenie praktyczne – automatyczne zliczanie relacji
4. Optymalizacja wykonania kodu
5. PL/pgSQL a PostGIS
6. Alternatywy dla PL/pgSQL (Python)
7. Obsługa PostGIS w Pythonie
8. Ćwiczenie praktyczne – prezentacja danych GIS w sieci www

SQL i PostGIS dla analityków – 5 dni
------------------------------------------

Dzień 1
""""""""""

1. Podstawy relacyjnego modelu danych i omówienie terminologii
2. Metody łączenia z bazą danych
3. Proste polecenia SELECT
4. Sortowanie i filtrowanie danych
5. Proste typy danych: tekstowe, numeryczne, czasowe, wyliczeniowe
6. Funkcje operujące na typach danych
7. Złożone typy danych: tablice, XML, hstore, JSON(B)
8. Koncepcja klucza głównego tabeli
9. Podstawy manipulacji danymi
10. Ćwiczenie praktyczne – projekt prostej tabeli zawierającej dane i metadane

Dzień 2
"""""""""""

1. Relacja One-To-Many
2. Relacja Many-To-Many
3. Relacja One-To-One i dziedziczenie
4. Omówienie możliwych klauzuli złączeń
5. Agregacja danych
6. Funkcja WINDOW
7. Operacje na zbiorach
8. Widoki
9. Ćwiczenia praktyczne – projekt bazy danych zawierających powiązane relacjami dane

Dzień 3
""""""""""
1. Podstawy zagadnienia wydajności zapytań
2. Polecenie EXPLAIN jako narzędzie umożliwiające analizę problemów wydajnościowych
3. Użycie indeksów w celu usprawnienia zapytań
4. Wpływ podzapytań na wydajność i metody ich unikania
5. Wykorzystanie operacji na zbiorach do usprawnienia zapytań
6. Więzy integralności
7. Idea transakcyjności bazy danych
8. Ćwiczenia praktyczne – rozwiązywanie problemów z wydajnością lub spójnością zapytań na przykładach

Dzień 4
""""""""""""

1. Wprowadzenie do tematu GIS
2. Import danych GIS do bazy
3. Typy danych geometrycznych i geograficznych
4. Podstawowe funkcje działające na danych GIS
5. Wyświetlanie i eksport danych GIS
6. Ćwiczenia praktyczne – praca z danymi geograficznymi Lasów Państwowych oraz
   Instytutu Badawczego Leśnictwa

Dzień 5
"""""""""""

1. Indeksy przestrzenne i ich zastosowanie
2. Strategie przechowywania danych geograficznych, wykorzystywanie wyzwalaczy
3. Praca z danymi rastrowymi
4. Ćwiczenia praktyczne – praca z danymi rastrowymi Lasów Państwowych oraz
   Instytutu Badawczego Leśnictwa
