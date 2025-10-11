# luolageneraattori

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/testausdokumentti.md)

### Viikkoraportit

- [Viikkoraportti 1](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportit/viikkoraportti1.md)
- [Viikkoraportti 2](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportit/viikkoraportti2.md)
- [Viikkoraportti 3](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportit/viikkoraportti3.md)
- [Viikkoraportti 4](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportit/viikkoraportti4.md)
- [Viikkoraportti 5](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportit/viikkoraportti5.md)
- [Viikkoraportti 5](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportit/viikkoraportti6.md)

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
Ohjelmalle syötetään numeronäppäimillä luku väliltä 3 - 400. Kun hyväksytty luku on valittu, enter-näppäimellä ohjelma arpoo syötetyn määrän huoneita ja generoi huoneiden välille reitit. Välilyönnillä saa näkymään huoneiden välisen triangulaation (punaiset viivat) ja triangulaatiosta lyhimmän virittävän puun (siniset viivat).