# Verkkokauppa

Sovellus on yksinkertainen verkossa toimiva kauppapaikka, jossa henkilöt voivat myydä ja ostaa tavaraa. Sovellus löytyy osoitteesta https://thawing-stream-99805.herokuapp.com/


### Kuinka testata
Rekistöröi itsellesi ainakin kaksi käyttäjää, joista toinen toimii myyjänä ja toinen ostajana. Ensiksi listaa tavaraa myyntiin myyjänä. Tämän jälkeen tilaa jokin myynnissä olevista tuotteista ostajana. Lopuksi vielä lähetä tilattu tuote myyjänä.

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



