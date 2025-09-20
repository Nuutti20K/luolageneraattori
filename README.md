# luolageneraattori

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/testausdokumentti.md)

### Viikkoraportit

- [Viikkoraportti 1](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportti1.md)
- [Viikkoraportti 2](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportti2.md)
- [Viikkoraportti 3](https://github.com/Nuutti20K/luolageneraattori/blob/master/dokumentaatio/viikkoraportti3.md)

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
Pylint ajetaan komennolla:
```bash
poetry run invoke lint
```