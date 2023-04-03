# Bachelorproefonderzoek : 

Middelbare scholieren van het derde graad met dyslexie ondersteunen bij het lezen van wetenschappelijke artikelen via tekstvereenvoudiging.

* Klik [hier](verslag/output/CluyseDylan-BPvoorstel.pdf) om naar het onderzoeksvoorstel te gaan.
* Klik [hier](verslag/output/CluyseDylanBP.pdf) om naar de bachelorproef te gaan.

Onder voorbehoud:
* Klik [hier](verslag/poster) om naar de poster te gaan.

## Prototype

Het prototype kan op [deze aparte GitHub repository](https://github.com/Dyashen/text-simplification-tool) terug worden gevonden. Daarnaast is er een Dockerfile beschikbaar dat de omgeving klaarzet.

## TODO

* Klik [hier](feedback-todo/todo.md) om naar de huidige taken te gaan.

## Feedback

* Klik [hier](feedback-todo/feedback-promotor.md) om het proces achter de communicatie en gekregen feedback op te volgen.


## Werking Docker-container

Voer het volgende commando in:

```cmd
docker build -t text-simplification .
sudo docker run -it -p 5000:5000 -d text-simplification
```
