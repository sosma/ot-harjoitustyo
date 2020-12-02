<h1>Sana peli apustaja ohjelma</h1>

## Käyttöohjeet
ohjelman käynnistys
```
python3 -m pipenv start
```
ohjelmassa valitaan aluksi mitä tietokantaa käytetään tekstipohjaisella käyttöliittymällä. käyttäjä voi valita joko "src/resources/sanat.txt" joka sisältää suomenkieliset sanat tai "src/resources/words.txt" joka sisältää englanninkieliset sanat. käyttäjä voi myös käyttää mitä tahansa haluamaansa sanastoa, missä on yksi sana per rivi, tällöin kirjoitat tähän vaan polun sanatiedostoosi.

tämän jälkeen käyttäjä voi halutessaan lisää tietokantaan yhden sanan, jos huomaa siellä puutoksen, jos ei halua lisätä sanoja, painetaan vain enter

tämän jälkeen päästään graafiseen käyttöliittymään.
ohjelmasta pääsee koittamaan sanojenhakuohjelmaa painamalla word snack nappia. tämän jälkeen kun painaa näytöltä ja alkaa kirjoittamaan tulee kirjoitettu merkkijono näytölle. Kun on kirjoittanut haluamansa kirjaimet näytölle, painamalla enter näppäintä hakee ohjelma sanat. Uuden merkkijonon kirjoittamisen voi aloittaa painamalla hiirellä näytöstä. Vasemmassa yläkulmassa olevasta napista pääsee takaisin menu näkemään. Jos yrittää hakea yli kuudella kirjaimella merkkijonoja, voi suoritusaika olla todella pitkä, meidän onneksi sanapala-peliä varten ei tarvitse hakea tätä pidempiä merkkijonoja

ohjelman testaus
```
python3 -m pipenv test
```

ohjelman koodin laadun tarkastus
```
python3 -m pipenv lint
```

## Kurssiprojekti
[määrittelydokumentti](dokumentaatio/maaritteludokumentti.md)

[arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.txt)
