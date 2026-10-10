# Bienvenue
Ce projet a pour but de proposer des jeux optimisés en espace, via des programmes et des outils pour facilité et optimisés l’espace de stockage ainsi que la RAM. Tel que draw qui permet l'affichage d'interface (utilisé dans la main et sitting), en évitant la répétition de code.

**Jusqu’à 8 jeux** sont disponible et compatible avec la main, il est possible de crée ses propres jeux (voir section **Participé**).

## Installation

Vous trouverai tous les programmes sur mon compte Numworks ([tmarie](https://my.numworks.com/python/tmarie "https://my.numworks.com/python/tmarie")).

Les jeux proposés par ce projet ne peuvent pas être exécutés directement dans l'émulateur web, ils requièrent tous des variables données par le programme [main.py](https://my.numworks.com/python/tmarie/main "https://my.numworks.com/python/tmarie/main") qui ne peut être import par l'émulateur.

Main ainsi que certains jeux requièrent eux-mêmes [draw.py](https://my.numworks.com/python/tmarie/draw "https://my.numworks.com/python/tmarie/draw"), qui est utilisé pour l'interface.

Après avoir installé ces deux dépendances sur votre calculatrice, vous pourrez installer n'importe lequel de ces jeux ci-dessous compatibles avec main.

- [morpion](https://my.numworks.com/python/tmarie/morpion "https://my.numworks.com/python/tmarie/morpion")
- [demineur](https://my.numworks.com/python/tmarie/demineur "https://my.numworks.com/python/tmarie/demineur")
- [pong](https://my.numworks.com/python/tmarie/pong "https://my.numworks.com/python/tmarie/pong")
- [snake](https://my.numworks.com/python/tmarie/snake "https://my.numworks.com/python/tmarie/snake")
- [arkanoid](https://my.numworks.com/python/tmarie/arkanoid "https://my.numworks.com/python/tmarie/arkanoid")
- [cookie_clicker](https://my.numworks.com/python/tmarie/cookie_clicker "https://my.numworks.com/python/tmarie/cookie_clicker")
- [space_invader](https://my.numworks.com/python/tmarie/space_invader "https://my.numworks.com/python/tmarie/space_invader")
- [course_voiture](https://my.numworks.com/python/tmarie/course_voiture "https://my.numworks.com/python/tmarie/course_voiture")

## Utilisation

Par la suite, vous n'aurez plus qu'à exécuter main sur votre calculatrice, celui-ci va automatiquement détecter les jeux installés et vous proposé de les exécuter.

Les jeux n'utilise pas tous les même touche, voici les touches générale :
- 'ok' sélectionner.
- '\v\' les flèches directionnelles pour naviguer.
- '' pour modifier les valeurs.
- 'ok' ou '<=' pour retourné au main.

Démineur :
- 'ok' drapeau.
- 'EXE' dévoilé.

## Participé ?

Si vous souhaitez participer en ajoutant un jeu ou en proposant des modifications via un fork de mon repositorie Github, voici quelque précision sur mon code pour mieux exploiter les outils mis à disposition et des conseils.

Pour créer de nouveaux jeux :

1. Ajoutez le nom de votre programme au Main dans la liste à la ligne 13, main ne teste que les programmes dont il connaît l'existence.
2. Ajouter une fonction nommée load (utile, pour que main le trouve) qui retournant soit des paramètre à ajouter dans setting ou rien.
```python
def load():
return ['nom','detail', ['choix 1','choix 2', ...], 'constante', n_default] | None

# constante : le texte à saisir pour récupérer la valeur choisie avec setting.varSelected('variable')
# n_default : numéro du choix par default dans la liste des choix
```
3. Main exécute la fonction launch() quand on choisie un programme, votre programme doit etre executé via launch et prendre en paramètre les différents paramètres donnés dans main.
```python
def launch(c=None,para=None,setting=None,sc=None,click=None):
# votre programme...
```
4. Pour proposer à l'utilisateur de revenir au main, faite un retourn pour arrêter le programme pendant l'exécution si keydown(17) et pressé. [mapping des touches de la calculatrice](https://tiplanet.org/forum/viewtopic.php?f=100&t=26294 "https://tiplanet.org/forum/viewtopic.php?f=100&t=26294")
```python
from ion import keydown
...
def launch(c=None,para=None,setting=None,sc=None,click=None):
...
while True:
if keydown(17):return
...
```
5. Si vous ajoutez un jeu via un fork, merci de préciser si besoin les touche de votre jeu dans le README.
6. Le but étant que les jeux ne prennent pas trop de place, je vous conseil de mettre l'indentation à 2 puisque c'est ce qui prend le plus de place.

Je reste ouvert à toute proposition de modification ou même de conseil, en espérant que mon projet vous amuse autant que moi.