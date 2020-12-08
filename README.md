<h1>Sana peli apustaja ohjelma</h1>

## Ohjelman alustus
pipenv asentaa tällä tarvittavat kirjastot, tämä pitää ajaa vain kerran
```
python3 -m pipenv install
```


## Käyttöohjeet

ohjelman käynnistys
```
python3 -m pipenv run start
```
ohjelmassa valitaan aluksi mitä tietokantaa käytetään tekstipohjaisella käyttöliittymällä. käyttäjä voi valita joko "src/resources/sanat.txt" joka sisältää suomenkieliset sanat tai "src/resources/words.txt" joka sisältää englanninkieliset sanat. käyttäjä voi myös käyttää mitä tahansa haluamaansa sanastoa, missä on yksi sana per rivi, tällöin kirjoitat tähän vaan polun sanatiedostoosi.

tämän jälkeen käyttäjä voi halutessaan lisää tietokantaan yhden sanan, jos huomaa siellä puutoksen, jos ei halua lisätä sanoja, painetaan vain enter

tämän jälkeen päästään graafiseen käyttöliittymään.

# menu
ohjelman menusta pääsee joko sanapala tai hirsipuu ohjelmaan painaan niihin viittaavaa nappia. quit napilla pääsee pois ohjelmasta.

# sanapala näkymä
kun painaa mistä vain kohtaa näytöltä ja alkaa kirjoittamaan tulee kirjoitettu merkkijono näytölle. Kun on kirjoittanut haluamansa kirjaimet näytölle, painamalla enter näppäintä hakee ohjelma sanat. Uuden merkkijonon kirjoittamisen voi aloittaa painamalla hiirellä mistä tahansa kohtaa näytöllä. Vasemmassa yläkulmassa olevasta napista pääsee takaisin menu näkemään. Jos yrittää hakea yli kuudella kirjaimella merkkijonoja, voi suoritusaika olla todella pitkä, meidän onneksi sanapala-peliä varten ei tarvitse hakea tätä pidempiä merkkijonoja

# hirsipuu näkymä
hirsipuu näkymässä aloitetaan kirjoittamalla sanassa olevien kirjainten määrä. Tämän jälkeen painamalla enter näppäintä ohjelma arvaa sanalle kirjaimen. Sitten käyttäjä painaa niistä kohdista johoin kirjain kuuluu jolloin ne korvaantuu arvatulla merkillä. Jos kirjain ei ole sanassa tai käyttäjä on painanut jo kaikki siihen menevät kirjaimet tulee käyttäjän painaa uudestaan enter näppäintä päästäkseen eteenpäin

ohjelman testaus
```
python3 -m pipenv run test
```

ohjelman koodin laadun tarkastus
```
python3 -m pipenv run lint
```

## Kurssiprojekti
[määrittelydokumentti](dokumentaatio/maaritteludokumentti.md)

[arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.txt)
