import numpy as np
import matplotlib.pyplot as plt

# Définir la fonction f(x) pour un effet poisson
def f(x):
    return np.sin(x) * np.exp(1 - np.abs(x))


# Définir l'intervalle de x
x = np.linspace(0, 10, 200)

# Dessiner la courbe
plt.plot(x, f(x))

# Ajouter un titre et des étiquettes d'axes
plt.title("Courbe en forme de poisson")
plt.xlabel("x")
plt.ylabel("f(x)")

# Afficher le graphique
plt.show()
