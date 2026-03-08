# Analyse des ventes

# 1. Objectif
Projet d'analyse de donnees réalisé en Python pour étudier les ventes d'une entreprise imaginaire.  
Il permet de calculer le chiffre d'affaires, d'analyser les ventes par produit et par mois et aussi de visualiser les données avec des graphiques.

# 2.Description
- Lecture des données à partir d'un fichier CSV (`ventes.csv`) contenant :  
  1.   `date` : date de la vente  
  2.  `produit` : nom du produit qui a été vendu  
  3.  `prix` : prix du produit en unité
  4  `quantite` : quantite vendue  

1.  Nettoyage et transformation des données :  
  - Conversion des dates  
  - Calcul du chiffre d'affaire (`revenu`)  
  - colonne `mois` qui va nous permettre d' analyser les ventes par mois  

2.  Analyse statistique :  
  - Chiffre d'affaires total  
  - Revenu par produit  
  - Revenu par mois  

3. Visualisations :  
  - Histograme du revenu par produit  
  - Camembert du revenu par produit  
  - Courbe d'evolut   du revenu par mois  

4. Interface interactive :  
  - Permet de filtrer les ventes pour un produit spécifique et d'afficher ses ventes détaillées avec un graphique.


