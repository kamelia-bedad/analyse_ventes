import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys


# Charger les donnees
data = pd.read_csv(r"C:\Users\kamel\OneDrive\Documents\Cours\analyse_ventes\data\ventes.csv")

# Nettoyer les donneess 
data["date"] = pd.to_datetime(data["date"])
data["revenu"] = data["prix"] * data["quantite"]
data["mois"] = data["date"].dt.to_period("M")  #mois

# stat globale
total_revenu = data["revenu"].sum()
print("Chiffre d'affaires total :", total_revenu)

ventes_produit = data.groupby("produit")["revenu"].sum()
print("\nRevenu par produit :\n", ventes_produit)

ventes_mois = data.groupby("mois")["revenu"].sum()
print("\nRevenu par mois :\n", ventes_mois)

# Graph
sns.set(style="whitegrid")

# Revenu par produit
plt.figure(figsize=(6,4))
sns.barplot(x=ventes_produit.index, y=ventes_produit.values, palette="Blues_d")
plt.title("revenu par produit")
plt.xlabel("produit")
plt.ylabel("Revenu")
plt.tight_layout()
plt.show()

# camember du revenu par produit
plt.figure(figsize=(6,6))
plt.pie(ventes_produit.values, labels=ventes_produit.index, autopct="%1.1f%%", startangle=140)
plt.title("Répartition du revenu par produit")
plt.show()

# revenu par mois 
plt.figure(figsize=(6,4))
sns.lineplot(x=ventes_mois.index.astype(str), y=ventes_mois.values, marker="o")
plt.title("Évolution du revenu par mois")
plt.xlabel("Mois")
plt.ylabel("Revenu")
plt.tight_layout()
plt.show()

# interface 
produit_choisi = input("Tape le nom d'un produit pour voir ses ventes détaillées (ou ENTER pour passer) : ").strip()
if produit_choisi:
    if produit_choisi in data["produit"].unique():
        detail_produit = data[data["produit"] == produit_choisi]
        print(f"\nVentes détaillées pour {produit_choisi} :\n", detail_produit)
        # Graphique du produit choisi
        ventes_par_date = detail_produit.groupby("date")["revenu"].sum()
        plt.figure(figsize=(6,4))
        sns.lineplot(x=ventes_par_date.index, y=ventes_par_date.values, marker="o")
        plt.title(f"Évolution des ventes de {produit_choisi}")
        plt.xlabel("Date")
        plt.ylabel("Revenu")
        plt.tight_layout()
        plt.show()
    else:
        print("Produit non trouvé dans le dataset.")