Collecte des Données
=====================

Dans cette section, nous décrivons le processus de collecte et de création des données utilisées dans le projet. Étant donné les biais identifiés dans les jeux de données existants, un jeu de données synthétique a été généré pour répondre aux besoins spécifiques du projet.

Contexte
--------

La disponibilité de jeux de données fiables est cruciale pour l’entraînement des modèles d’apprentissage automatique. Cependant, en travaillant avec des datasets réels, plusieurs biais et limitations ont été constatés :

- Problèmes de qualité des données : certaines variables étaient mal renseignées ou manquantes.
- Biais dans la population : les datasets réels présentaient un manque de représentativité de certaines tranches d’âge et niveaux d’entraînement.
- Coût et accessibilité : certaines données provenant de bases de recherche sportive n’étaient pas accessibles ou étaient protégées par des restrictions légales.

Pour pallier ces limitations, nous avons opté pour une approche de **génération de données synthétiques** basée sur des études et analyses fiables.

Génération des Données Synthétiques
-----------------------------------

Les données synthétiques ont été créées à partir de distributions statistiques et d'hypothèses dérivées d'études scientifiques et de données existantes. Ces données permettent d'étudier les facteurs prédictifs des blessures musculaires, notamment dans le contexte du football, où ce type de blessure est l’un des plus critiques. 

**Variable Target**

La variable cible (*target*) est **binaire** et contient deux valeurs possibles :

- **1 :** Le joueur présente un risque de blessure musculaire.
- **0 :** Le joueur ne présente aucun risque de blessure musculaire.

Cette variable cible a été définie sur la base des conclusions de plusieurs études et documents fiables, qui montrent que certains facteurs (tels que l’historique de blessures musculaires ou des charges d’entraînement excessives) augmentent considérablement le risque. En particulier, les blessures musculaires sont une des préoccupations majeures dans le domaine du football, en raison de leur fréquence et de leur impact sur les performances des joueurs.

**Features Utilisées**

Voici les **features** principales incluses dans le jeu de données et leur pertinence dans le contexte de l’étude sur les blessures musculaires :

1. **Âge** :
   - Variable continue exprimée en années.
   - Impact potentiel sur le risque de blessure dû à la diminution de la récupération musculaire avec l'âge.

2. **Fatigue (%)** :
   - Mesure de la fatigue subjective exprimée en pourcentage (de 0 % à 100 %).
   - Déterminée à partir d’études sur la performance physique et la charge cumulée.

3. **Minutes jouées** :
   - Total des minutes jouées lors des compétitions.
   - Indicateur direct de la charge d'activité physique.

4. **Heures d’entraînement** :
   - Nombre d'heures d’entraînement.
   - Variable continue influençant les niveaux de fatigue et les risques musculaires.

5. **Historique des blessures musculaires** :
   - Variable binaire ou catégorielle indiquant des blessures musculaires récentes.
   - Facteur prédictif clé dans les études sur la prévention des blessures, les joueurs ayant déjà souffert de telles blessures étant souvent plus vulnérables.

6. **Contact physique (oui/non)** :
   - Variable binaire indiquant si l’athlète est impliqué dans des activités à contact physique élevé.
   - Ce facteur est essentiel, car les sports impliquant des contacts physiques augmentent les risques de blessure musculaire.

En résumé, ces variables ont été sélectionnées en fonction de leur pertinence scientifique et de leur contribution à prédire la variable cible. Ce choix garantit une meilleure compréhension et une analyse fiable des facteurs influençant les blessures musculaires.


..
    Visualisation des Données Générées   (comment la visualiser)
    ----------------------------------

    Pour valider la cohérence des données, plusieurs techniques de visualisation ont été utilisées:

    - Distribution des âges et des heures d’entraînement : **seaborn** a permis de générer des histogrammes pour vérifier que les valeurs suivent les attentes définies.
    - Matrice de corrélation : pour s’assurer de la pertinence des relations entre les variables générées.
    - Validation croisée : en utilisant des échantillons de validation synthétique.

Avantages des Données Synthétiques
-----------------------------------

L’utilisation des données synthétiques présente plusieurs avantages :

- **Absence de contraintes légales** : pas de restrictions associées aux données réelles.
- **Contrôle total sur les variables** : génération des données en fonction des hypothèses et des besoins spécifiques du projet.
- **Équilibrage des classes** : réduction des biais en équilibrant les observations avec et sans blessures.

---

Pour des détails sur le prétraitement des données, passez à la section suivante :source:`preprocessing`.
