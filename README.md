# Verkkokauppa

Sovellus on verkossa toimiva kauppapaikka, jossa henkilöt voivat myydä ja ostaa tavaraa. Sovellus löytyy osoitteesta https://thawing-stream-99805.herokuapp.com/

## Sovelluksen nykyinen tilanne (20.9)
Sovelluksen tuotteiden hakutoimintoja ei ole vielä toteutettu, vaan kaikki tuotteet ovat yhtenä listana. Myöskään tuotteiden ja myyjien arviointi ei ole vielä mahdollista. Sovelluksen ulkoasu on vielä hyvin alkeellinen. Sovelluksen koodikin on vielä refaktorointia vaille.
### Kuinka testata
Rekistöröi itsellesi käyttä/käyttäjiä ja listaa tavaraa myyntiin sekä tilaa listaamiasi tavaroita.

## Käyttäjätyypit
### Ylläpitäjä (TODO)
- voi poistaa listauksia
- voi poistaa käyttäjiä
- voi lisätä uusia tuotekategorioita sovellukseen

### Käyttäjä

- voi ostaa tuotteita
- voi myydä tuotteita
- voi käsitellä tuotteidensa tilauksia
- näkee oman tilaushistoriansa
- pystyy seuraamaan tilauksiaan (esim. tilaus käsittelyssä tai tilaus matkalla)
- pystyy perumaan tilauksen, jos sitä ei ole vielä käsitelty (TODO)
- voi poistaa listaamiaan tuotteita myynnistä (TODO)
- voi arvioida ostamiaan tuotteitta (TODO)
- voi arvioida ostamiensa tuotteiden myyjää (TODO)
- voi ilmoittaa listauksen epäilyttäväksi (TODO)
- voi ilmoittaa myyjän epäilyttäväksi (TODO)
- voi hakea tuotteita sovelluksesta (TODO)
- voi selata myyjän listauksia (TODO)

## Tietokantataulut
- käyttäjä
- tuote (samalla tuotteella (esim Super Mario 64) voi olla usea listaus, joissa on eri hinta ja myyjä)
- listaus (tuote, myyjä ja hinta)
- tilaus (ostaja ja listaus)
- valmistaja (tuotteen valmistaja esim. Nintendo) 
- kategoria (kategoriloilla voi olla yläkategoria, jonka avulla voidaan luoda kategoriahiearkia esim. null <- kodinkone <- pesukone <- päältätäytettävä pesukone. Jos yläkategoria on null, niin tuotteella ei ole yläkategoriaa)


