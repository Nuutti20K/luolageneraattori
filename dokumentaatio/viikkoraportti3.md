## Viikkoraportti 3

Tällä viikolla viimeistelin Bowyer-Watson algoritmin toimintaa, ja sain sen sellaiseen tilaan, että voin siirtyä lyhimmän virittävän puun löytävään algoritmiin. Lisäksi tein lisää testejä ja laitoin pylintin toimimaan.

Nyt ohjelma on tilassa, jossa se pystyy tekemään Delaunay triangulaation mielivaltaisesta huonelistasta.

Opin tarkemmin hyvän "super trianglen" määrittelystä, sillä todellisuudessa ei riitä että kolmio kattaa kaikki pisteet. Huono kolmio loi tilanteita, jossa algoritmi ei aina trianguloinut uloimmaisia kolmioita oikein.

Vaikeaa tällä viikolla oli kiireellisyys. Tuntuu että ei kerennyt tekemään niin paljon kuin olisin halunnut

Epäselväksi jäi pylintin tuottama viesti:
```bash
Captured stderr while importing pygame.base:
/home/kekknuut/tira-projekti/luolageneraattori/.venv/lib/python3.10/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
```