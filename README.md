 Projet_IA
Ce projet est constitué de trois scripts principaux qui collaborent pour permettre l'enregistrement, l'entraînement et la reconnaissance de personnes à l'aide de leur visage. Voici une description détaillée de leur fonctionnement :

1. main.py
Le script main.py est utilisé pour créer les données nécessaires à l'entraînement du classifieur et préparer la reconnaissance des visages. Son fonctionnement s'organise en plusieurs étapes :

Enregistrement vidéo
La fonction main_interface enregistre une vidéo de la personne souhaitant s'enregistrer. Des consignes précises sont données pour obtenir des angles variés du visage. Les images extraites de la vidéo sont sauvegardées dans un dossier portant le nom de la personne.

Détection et recadrage des personnes
La fonction detectPeople (de la bibliothèque pyppbox) identifie et recadre la personne sur chaque image extraite, ne conservant que le corps dans un dossier nommé "cropped_body".

Alignement et redimensionnement des visages
Le script align_dataset_mtcnn.py est ensuite exécuté pour détecter uniquement le visage de la personne sur les images recadrées. Les visages détectés sont redimensionnés pour avoir des dimensions uniformes, ce qui facilite l'entraînement.

Entraînement du classifieur
Enfin, la fonction create_model_pkl (issue de l'exemple example_11_reid_classifier.py de pyppbox) est utilisée pour entraîner un classifieur sur l'ensemble des visages disponibles. Le modèle généré est sauvegardé sous la forme d’un fichier .pkl.

À la fin de ce processus, le classifieur est prêt à reconnaître les visages des personnes enregistrées.

2. demo.py
Le script demo.py est utilisé pour effectuer la reconnaissance en temps réel à l'aide de la caméra. Voici comment il fonctionne :

Activation de la caméra
La caméra est activée pour capturer des images en direct.

Détection et suivi des personnes
Les fonctions detectPeople, trackPeople et reidPeople (de pyppbox) sont utilisées pour détecter, suivre et ré-identifier les personnes présentes dans le champ de la caméra.

Reconnaissance des personnes
Les visages détectés sont comparés au modèle entraîné pour identifier les personnes en temps réel à l'aide du classifieur.

3. run_main.py
Le script run_main.py agit comme un gestionnaire d'exécution pour orchestrer demo.py et main.py. Voici son fonctionnement :

Lancement de la reconnaissance
Le script commence par exécuter demo.py pour effectuer la reconnaissance en continu.

Ajout d'une nouvelle personne
Si une nouvelle personne souhaite être ajoutée, il lui suffit d'appuyer sur Entrée. Cela interrompt demo.py, puis lance main.py pour enregistrer la vidéo, extraire les visages et réentraîner le classifieur avec cette nouvelle personne.

Reprise de la reconnaissance
Une fois l'entraînement terminé, le script relance demo.py pour continuer la reconnaissance avec le classifieur mis à jour.

Ce processus est répété indéfiniment, permettant d'ajouter facilement de nouvelles personnes tout en maintenant la reconnaissance active. 