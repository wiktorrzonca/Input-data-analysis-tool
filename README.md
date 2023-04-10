# Input-data-analysis-tool
Main file - marketdata.json
1. Glownym plikiem jest marketdata.json a nie contoption.json   -- done
2. Z glownego pliku powinno sie odczyczytac nazwy datasetow znajdujace sie w ['datasets'] -- done
3. Metoda get_individual_data_sets() zwraca slownik w postaci {nazwa-pliku : czy-istnieje} -- done
4. Wyrzucilem tez klase z maina bo to nie java!!!!

5. Pliki trader_cds_price.json i contiption.json to te mniejsze pliki opisujace poszczegolne pliki .csv
6. Mysle ze najlepiej byloby utworzyc jakas klase DDA_File ktora bedzie reprezentowac te mniejsze pliki
   w niej dac jakies pole listy w ktorej beda obiekty klas DDA_column
7. DDA-column powinno reprezentowac poszczegolne kolumny opisane w tych mini plikach .json czyli miec pola typu
    type, description itd.
8. Z tego co patrzylem to wiekszosc kolumn typu Int, Double, String maja tyle samo pol ale takie Date ma jedno dodatkowe 
    pole format. To trzeba uwzglednic
