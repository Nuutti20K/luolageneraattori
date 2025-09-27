# luolageneraattori

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/testausdokumentti.md)

### Viikkoraportit

- [Viikkoraportti 1](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportti1.md)
- [Viikkoraportti 2](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportti2.md)
- [Viikkoraportti 3](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportti3.md)
- [Viikkoraportti 3](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportti4.md)

## Asennus
Tarvittavat riippuvuudet asennetaan komennolla:
```bash
poetry install
```
## Komentorivitoiminnot
Ohjelma käynnistetään komennolla:
```bash
poetry run invoke start
```
Testit tehdään komennolla: 
```bash
poetry run invoke test
```
Kattavuusraportin saa komennolla: 
```bash
poetry run invoke coverage-report
```
Pylint ajetaan komennolla:
```bash
poetry run invoke lint
```

## Käyttöohjeet
Ohjelmalle syötetään numeronäppäimillä luku väliltä 3 - 400. Kun hyväksytty luku on valittu, enter-näppäimellä ohjelma arpoo syötetyn määrän huoneita ja trianguloi huoneiden väliset yhteydet (punaiset viivat) ja etsii näistä yhteyksistä lyhimmän virittävän puun (siniset viivat).