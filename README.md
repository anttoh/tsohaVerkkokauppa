# Verkkokauppa

Sovellus on yksinkertainen verkossa toimiva kauppapaikka, jossa henkilöt voivat myydä ja ostaa tavaraa. Sovellus löytyy osoitteesta https://thawing-stream-99805.herokuapp.com/

## Sovelluksen nykyinen tilanne (4.10)
Sovelluksen ulkoasu on vielä hyvin alkeellinen. Sovelluksen koodikin on vielä refaktorointia vaille.
### Kuinka testata
Rekistöröi itsellesi ainakin pari käyttäjää ja listaa tavaraa myyntiin sekä tilaa listaamiasi tavaroita.

## Käyttäjätyypit
### Ylläpitäjä (TODO)
- voi poistaa listauksia
- voi poistaa käyttäjiä

### Käyttäjä

- voi ostaa tuotteita
- voi myydä tuotteita
- voi hakea tuotteita sovelluksesta
- voi käsitellä tuotteidensa tilauksia
- näkee oman tilaushistoriansa
- pystyy perumaan tilauksen, jos sitä ei ole vielä käsitelty
- voi poistaa listaamiaan tuotteita myynnistä (TODO)


## Tietokantataulut
- käyttäjä
- tuote (samalla tuotteella (esim Super Mario 64) voi olla usea listaus, joissa on eri hinta ja myyjä)
- listaus (tuote, myyjä, hinta ja tägit, joiden avulla tuotetta voi hakea)
- tilaus (ostaja ja listaus)
- valmistaja (tuotteen valmistaja esim. Nintendo) 



