# Verkkokauppa

Sovellus on yksinkertainen verkossa toimiva kauppapaikka, jossa henkilöt voivat myydä ja ostaa tavaraa. Sovellus löytyy osoitteesta https://thawing-stream-99805.herokuapp.com/


### Kuinka testata
Rekistöröi itsellesi ainakin pari käyttäjää ja listaa tavaraa myyntiin sekä tilaa listaamiasi tavaroita. Käyttäjä ei näe omia listauksiaan myynnissä. Tilattu tuote näkyy profiilin osiossa active orders, kunnes tuotteen myyjä lähettää tilauksen osiosta pending orders. Kun tilaus on lähetetty siirtyy se ostajan profiilissa osioon bought items ja myyjän profiilissa osioon sold items. Myyjä näkee listaamansa tuotteet, joita ei ole tilattu osiossa unsold items.

### Käyttäjä

- voi ostaa tuotteita
- voi myydä tuotteita
- voi hakea tuotteita sovelluksesta
- voi käsitellä tuotteidensa tilauksia
- näkee oman tilaushistoriansa
- pystyy perumaan tilauksen, jos sitä ei ole vielä käsitelty
- voi poistaa listaamiaan tuotteita myynnistä 


## Tietokantataulut
- käyttäjä
- tuote (samalla tuotteella (esim Super Mario 64) voi olla usea listaus, joissa on eri hinta ja myyjä)
- listaus (tuote, myyjä, hinta, kuvaus)
- tägi (auttaa tuotteiden haussa)
- listaus-tägi (liitostaulu)
- tilaus (ostaja ja listaus)
- valmistaja (tuotteen valmistaja esim. Nintendo) 



