# Verkkokauppa

Sovellus on verkossa toimiva kauppapaikka, jossa henkilöt ja yritykset voivat myydä ja ostaa tavaraa. Sovellus löytyy osoitteesta https://thawing-stream-99805.herokuapp.com/

## Käyttäjätyypit
### Ylläpitäjä
- voi poistaa epäilyttäviä listauksia (myytäviä tuotteita)
- voi poistaa epäityäviä myyjiä, jolloin kaikki myyjän tuotteet poistuvat myynnistä
- voi lisätä uusia tuotekategorioita sovellukseen
- voi merkitä myyjän(käyttäjän) luotettavaksi (esim. tunnettu yritys)
- voi estää käyttäjää toimimasta jommassakummassa tai molemmissa rooleissa (ostaja ja myyjä)
- voi poistaa käyttäjän

### Käyttäjä
Käyttäjä voi toimia kahdessa roolissa, ostajana tai myyjänä, ja rooleja voi vaihtaa.

#### Ostajana
- voi ostaa tuotteita
- voi arvioida ostamiaan tuotteitta
- voi arvioida ostamiensa tuotteiden myyjää
- voi ilmoittaa listauksen epäilyttäväksi
- voi ilmoittaa myyjän epäilyttäväksi
- voi hakea tuotteita sovelluksesta
- voi selata myyjän listauksia
- näkee oman tilaushistoriansa
- pystyy seuraamaan tilauksiaan (esim. tilaus käsittelyssä tai tilaus matkalla)
- pystyy perumaan tilauksen, jos sitä ei ole vielä käsitelty.

#### Myyjänä
- voi listata tuotteita myyntiin
- voi poistaa listaamiaan tuotteita myynnistä
- voi muuttaa listattujen tuotteidensa hintaa, tuotekuvausta jne.
- käsittelee tuotteidensa tilauksia
- voi tarkastella tuotteidensa myyntihistoriaa

## Tietokantataulut
- käyttäjä
- tuote (samalla tuotteella (esim Pokemon Sword) voi olla usea listaus, joissa on eri hinta ja myyjä)
- listaus (tuote, myyjä ja hinta)
- tilaus (ostaja ja listaus)
- valmistaja (tuotteen valmistaja esim. Nintendo) 
- kategoria (kategoriloilla voi olla yläkategoria, jonka avulla voidaan luoda kategoriahiearkia esim. null <- kodinkone <- pesukone <- päältätäytettävä pesukone. Jos yläkategoria on null, niin tuotteella ei ole yläkategoriaa)


