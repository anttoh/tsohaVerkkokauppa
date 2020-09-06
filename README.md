# Verkkokauppa

Sovellus on verkossa toimiva kauppapaikka, jossa henkilöt ja yritykset voivat myydä ja ostaa tavaraa. Sovellus tuo myyjät ja ostajat yhteen. Samalla sähköpostilla voi luoda yhden ostaja-tilin sekä yhden myyjä-tilin. Tilit luodaan erikseen, eikä molempia ole pakko luoda.

## Käyttäjätyypit
### Ylläpitäjä
- voi poistaa epäilyttäviä listauksia (myytäviä tuotteita)
- voi poistaa epäityäviä myyjiä, jolloin kaikki myyjän tuotteet poistuvat myynnistä
- voi lisätä uusia tuotekategorioita sovellukseen
- voi merkitä myyjän luotettavaksi (esim. tunnettu yritys)

### Ostaja
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

### Myyjä
- voi listata tuotteita myyntiin
- voi poistaa listaamiaan tuotteita myynnistä
- voi muuttaa listattujen tuotteidensa hintaa, tuotekuvausta jne.
- käsittelee tuotteidensa tilauksia
- voi tarkastella tuotteidensa myyntihistoriaa

## Tietokantataulut
- myyjä
- ostaja
- tuote (samalla tuotteella (esim Pokemon Sword) voi olla usea listaus, joissa on eri hinta ja myyjä)
- listaus (tuote, myyjä ja hinta)
- tilaus (ostaja ja listaus)
- valmistaja (tuotteen valmistaja esim. Nintendo) 
- kategoria (esim. kodinkoneet)
- alakategoria (esim. pesukoneet)
- ala-alakategoria (esim. päältä täytettävät pesukoneet)


