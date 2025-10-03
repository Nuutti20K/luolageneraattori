# Toteutusdokumentti

## Yleisrakenne
Projetin src kansiossa on seuraavat tiedostot:
- bowyer_watson moduuli käsittelee huoneiden triangulaation ja etsii kaikki potentiaaliset reitit huoneiden välillä
- prims moduuli etsii trianguloiduista verkosta lyhyimmän virittävän puun
- objects moduuli sisältää algoritmien toimintaan käytettyjä objekteja, eli Room, Vertex, Edge ja Triangle
- randomize generoi annetun määrän satunnaisia huoneita
- renderer käsittelee huoneiden ja polkujen piirtämisen
- index käsittelee sovelluksen käynnistyksen ja syötteiden käsittelyn (syötteiden käsittely tarkoitus siirtää gameloop moduuliin)
- tests kansio sisältää sovelluksen yksikkötestit

## Ongelmia 
- Jos kaikki pisteet sijoittuvat suoralle, niin Bowyer-Watson algoritmi ei osaa löytää huoneiden välille reittejä.

## Aikavaativuudet
Bowyer-Watson algoritmin aikavaativuus tällä toteutuksella on O(n^2)
Primmin algoritmin aikavaativuus käyttäen vierekkyys matriisia on O(n^2)

## Laajat kielimallit
laajoja kielimalleja ei ole käytetty projektin aikana.

## Lähteitä
käytettyjä lähteitä: 
- https://brandewinder.com/2025/03/05/delaunay-super-triangle/
- https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/
- https://en.wikipedia.org/wiki/Circumcircle#Circumcenter_coordinates
- https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm
- https://vazgriz.com/119/procedurally-generated-dungeons/
- https://www.w3schools.com/dsa/dsa_algo_mst_prim.php
