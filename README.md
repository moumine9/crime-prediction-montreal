#Predictions de crimes villes de montreal.

## Introduction
L'analyse des données criminelles semble être la prochaine étape vers laquelle évolueront les services de protections des civils (police, gendarmie, pompiers, ambulances). Le volume des données, la qualité des données et les performacnes de calcul permettent aisément de coordonner les efforts de deploiements de ces forces de protection. Dans notre travail, nous avons essayé de démontrer qu'il é ait possible que la police 'arrive plus rapidement sur les lieux q'une pizza commandée'.

### Approche theorique.

Dans un premier temps, nous nous devons de faire une série d'analyses du dataset founi. Ainsi, nous avons produit les rapport suivants : 
- Analyse spatiale de la criminalité à Montreal : Ici
- Analyse temporelle de la criminalité à Montréal : ici
- Analyse statistique du dataset (qui sera utile pour la génération des réseaux de neuronnes.)

Pour arriver à nos fins, nous allons proposer une approche hétèrogene étant donné la nature variée des questions à répondre :

 - Prédiction du nombre de crimes à montreal : Là aussi, nous allons utiliser une double approche :
    - Utilisation de FbProphet, la librairie de Facebook pour les Time-Series-Prediction
    - Un RNN customisé avec Keras.

- Tentative de catégorisation des crimes : nous allons utiliser plusieurs approches :
    - TreeClassifier pour predire le crime susceptible d'arriver en fonction des parametres.