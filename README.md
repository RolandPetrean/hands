# hands
## main.py / mp.py
Aici este programul propriu-zis. Daca rulezi `main.py`, vei putea alege daca sa folosesti o camera virtuala sau o fereastra deschisa de OpenCV. Cand apare o mana pe ecran, aceasta va fi incadrata intr-un dreptunghi, si daca faci vreun semn pentru care este antrenat modelul din `model/`, il va recunoaste!
## modelul
In folder-ul `model/`, veti gasi un program de antrenare si un model deja antrenat (in `trained/`) cu urmatoarele semne:
1. PACE (✌️)
2. CHILL (semnul ala de suni pe cineva)
3. PISTOL (mai trebuie sa zic?)
4. OK (serios, e evident)

Totusi, modelul pe care l-am antrenat eu nu merge foarte bine (are multe greseli), pentru ca am acumulat doar vreo 600 de semne. 

Daca vreti sa antrenati un model, intrati pe modul OpenCV si apasati numere de la `0-9`. Semnul care apare pe ecran la acel moment va fi inregistrat cu ID-ul numarului apasat.

## exemple
![pace](https://i.ibb.co/xXwbwY0/image.png)
![chill](https://i.ibb.co/Nrd6Cqq/image.png)
![pistol](https://i.ibb.co/JRK9dRJ/image.png)