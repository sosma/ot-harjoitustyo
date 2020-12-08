<h1>Sana peli apustaja ohjelma</h1>

Ohjelman avulla on mahdollista saada nopeasti apua hirsipuu ja sanapala pelien voittamiseen. Ohjelmaan voi käyttää millä tahansa kielellä jolle käyttäjällä on tietokanta, mutta mukana tulee suomen ja englanninkieliset versiot

## Python versio
Ohjelma toimii ainakin 3.6.10 ja sitä uudemmilla python versiolla

## Käyttöliittymät
Ohjelmaa on testattu vain linux käyttöliittymällä

## Asennus

asenna riippuvuudet  komennolla
```
python3 -m pipenv install
```

käynnistä ohjelma ajamalla
```
python3 -m pipenv run start
```

## Komentorivitoiminnot

 ohjelman ajtetaan komennolla
```
python3 -m pipenv run start
```
ohjelman testataan komennolla
```
python3 -m pipenv run test
```

testikattavuus saadaan komennolla
```
python3 -m pipenv run coverage
```
tämän jälkeen raportin voi generoida komennolla
```
python3 -m pipenv run coverage-report
```

ohjelman koodin laadun tarkastus
```
python3 -m pipenv run lint
```

## dokumentaatio

[käyttöohje](dokumentaatio/kayttoohje.md)

[arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[määrittelydokumentti](dokumentaatio/maaritteludokumentti.md)

[testausdokumentti](dokumentaatio/testausdokumentti.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.txt)
