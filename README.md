# Input-data-analysis-tool
Main file - marketdata.json
1. Glownym plikiem jest marketdata.json a nie contoption.json   -- done
2. Z glownego pliku powinno sie odczyczytac nazwy datasetow znajdujace sie w ['datasets'] -- done
3. Metoda get_individual_data_sets() zwraca slownik w postaci {nazwa-pliku : czy-istnieje} -- done
4. Wyrzucilem tez klase z maina bo to nie java!!!!

5. Pliki trader_cds_price.json i contiption.json to te mniejsze pliki opisujace poszczegolne pliki .csv
6. Mysle ze najlepiej byloby utworzyc jakas klase DDA_File ktora bedzie reprezentowac te mniejsze pliki
   w niej dac jakies pole listy w ktorej beda obiekty klas DDA_column --done
7. DDA-column powinno reprezentowac poszczegolne kolumny opisane w tych mini plikach .json czyli miec pola typu
    type, description itd. --done
8. Z tego co patrzylem to wiekszosc kolumn typu Int, Double, String maja tyle samo pol ale takie Date ma jedno dodatkowe 
    pole format. To trzeba uwzglednic

Jan zmiany
1. Zrobiłem klase DDA_file do mniejszych plików dda, ma atrybuje nazwa, path oraz słownik column tych co są w tym pliku
2. Klasa DDA_column to klasa pojedynczej kolumny
3. W main na razie jest ze gdy plik się zgadza z tym co jest w tym glownym jsonie to jest dodawany do slownika, gdzie {file_nake : DDA_file}, a w obiekcie DDA_file jest slownik na kolejne obiekty kolumn