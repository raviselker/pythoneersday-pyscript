import matplotlib.pyplot as plt

figure_el = Element("figure")

fig, _ = plt.subplots()
figure_el.write(fig)
