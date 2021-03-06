from cProfile import label
import matplotlib.pyplot as plt

#Binomial Graphs
#Execucio de 100 grafs per a cada probabilitat
xAxis = [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95]
grafo20 = [0,0,0.05,0.46,0.75,0.95,0.98,1,1,1,1,1,1,1,1,1,1,1,1,1]
grafo60 = [0,0.1,0.92,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
grafo100 = [0,0.48,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
grafo1000 = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
grafo5000 = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
plt.plot(xAxis, grafo20, label = "20")
plt.plot(xAxis, grafo60, label = "60")
plt.plot(xAxis, grafo100, label = "100")
plt.plot(xAxis, grafo1000, label = "1000")
plt.plot(xAxis, grafo5000, label = "5000")
plt.legend()
plt.title("Binomial Graph Generator Connectivity")
plt.xlabel("Probability binomial")
plt.ylabel("Ratio connectivity")
plt.show()