# luolageneraattori

Matopelissä on tarkoitus ohjata matoa ja kerätä pellettejä. Aina kun mato syö pelletin sen kokonaispituus kasvaa, ja kun mato törmää itseensä tai seinään, peli loppuu.

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/testausdokumentti.md)

### Viikkoraportit

- [Viikkoraportti 1](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraporrti1.md)
- [Viikkoraportti 2](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraporrti2.md)

## Asennus
Tarvittavat riippuvuudet asennetaan komennolla:
```bash
poetry install
```
## Komentorivitoiminnot
Peli käynnistetään komennolla:
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