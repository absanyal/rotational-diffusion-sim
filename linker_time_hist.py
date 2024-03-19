import numpy as np
import matplotlib.pyplot as plt
from modules.distributions import firstpassage, wald
# import scipy.stats as stats

data_raw = np.loadtxt('data/time_data_for_histogram.txt')

data = []

for t in data_raw:
    if (t != 30.0):
        data.append(t)

data = np.array(data)

# print(data)

print("Number of attachements found: {} out of {}".format(len(data), len(data_raw)))

print("{:3.2f} % succesfully attached".format(len(data)/len(data_raw) * 100))

print("Mean: {:.2f}".format(np.mean(data)))
print("Std dev: {:.2f}".format(np.std(data)))

# bins_list = range(int(min(data)) - 1, int(max(data)) + 1)
bins_list = []
bin_val = int(min(data))
while (bin_val < int(max(data)) + 1):
    bins_list.append(bin_val)
    bin_val += 1.0

plt.figure(tight_layout=True)

plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel("Frequency", fontsize=18)

plt.xlim(0, 30)

plt.hist(data, bins=bins_list, histtype='bar', rwidth=0.8,
         color='b', edgecolor='k', density=True, align='left')

############## Plotting the theoretical distribution ####################

theta = 45
theta_rad = np.radians(theta)

Drot_data = np.loadtxt("data/Drot_meas_reduced.dat")
Drot = Drot_data[1]

t_list = np.linspace(0.1, 30, 500)
fp_list = np.zeros(len(t_list))
wald_list = np.zeros(len(t_list))


D_input = 0.06678507142321072

for i in range(len(t_list)):
    fp_list[i] = D_input * firstpassage(D_input * t_list[i], theta_rad)

plt.plot(t_list, fp_list, label=r'First passage $({}\degree)$'.format(
    theta), linestyle="-", color="r")
# plt.plot(t_list, wald_list, label=r'Wald $({}\degree)$'.format(theta), linestyle="--", color="limegreen")

plt.legend()

plt.savefig("plots/time_hist.pdf")
