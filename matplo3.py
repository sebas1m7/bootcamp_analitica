import matplotlib.pyplot as mlp

edades=[20,21,24,39,22,34,33,19,45,37,27]
mlp.hist(edades, bins=5, color="darkblue", edgecolor="white")
mlp.title("Rango de edades")
mlp.xlabel("Edades rango")
mlp.ylabel("Distribucion de edades")
#mlp.grid(True,color="gray")
mlp.show()