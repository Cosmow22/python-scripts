### Ce petit programme approxime le nombre racine carrée de deux, avec une fraction continue.

![text](https://wikimedia.org/api/rest_v1/media/math/render/svg/ca4ab91f7230c79170b56a5c7fd4a0cc0500b730)

# Observations
- la profondeur de la fonction récursive est limitée à 999 alors que la fonction avec la boucle while n'est limitée qu'à la mémoire de l'ordinateur
- la fonction récursive est de manière générale moins précise que la fonction avec la boucle while, il y a 1 ou deux décimales de différences entre les deux résultats (par rapport à la référence ``GOAL``)
- la fonction récursive est plus lente que la fonction avec la boucle while, surtout quand la profondeur augmente