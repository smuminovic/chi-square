import csv
import numpy as np
from scipy.stats import chi2_contingency

#import ukupnih podataka
with open('podaci_poviseni_HR.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC))
#import podataka za vjezabanje
with open('vjezbanje_poviseni_HR.csv', newline='') as csvfile:
    data_vjezbanje = list(csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC))

MI = data[0]
HR = data[1]
MI_vjezbanje = data_vjezbanje[0]
HR_vjezbanje = data_vjezbanje[1]

#trazenje srednje vrijednosti vježbanja
max_mean_MI = 0;
max_mean_HR = 0;
for i in range(0, len(MI_vjezbanje)):
    max_mean_MI = MI_vjezbanje[i] + max_mean_MI;
    max_mean_HR = HR_vjezbanje[i] + max_mean_HR;
max_mean_MI = max_mean_MI/len(MI_vjezbanje)
max_mean_HR = max_mean_HR/len(HR_vjezbanje)

#moving average
def moving_avg(x, n):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[n:] - cumsum[:-n]) / float(n)
n = 5
MI = moving_avg(MI, n)


#podjela u kategorije
MI_kat = [0, 0, 0, 0, 0, 0];
HR_kat = [0, 0, 0, 0, 0, 0];
for i in range(0, len(MI)):
    if MI[i] >= max_mean_MI*0.95:
        MI_kat[0] = MI_kat[0] + 1;
    elif (MI[i] >= max_mean_MI*0.85) and (MI[i] < max_mean_MI*0.95):
        MI_kat[1] = MI_kat[1] + 1;
    elif (MI[i] >= max_mean_MI*0.75) and (MI[i] < max_mean_MI*0.85):
        MI_kat[2] = MI_kat[2] + 1;
    elif (MI[i] >= max_mean_MI*0.65) and (MI[i] < max_mean_MI*0.75):
        MI_kat[3] = MI_kat[3] + 1;
    elif (MI[i] >= max_mean_MI*0.55) and (MI[i] < max_mean_MI*0.65):
        MI_kat[4] = MI_kat[4] + 1;
    else:
        MI_kat[5] = MI_kat[5] + 1;

for i in range(0, len(HR)):
    if HR[i] >= max_mean_HR*0.95:
        HR_kat[0] = HR_kat[0] + 1;
    elif (HR[i] >= max_mean_HR*0.85) and (HR[i] < max_mean_HR*0.95):
        HR_kat[1] = HR_kat[1] + 1;
    elif (HR[i] >= max_mean_HR*0.75) and (HR[i] < max_mean_HR*0.85):
        HR_kat[2] = HR_kat[2] + 1;
    elif (HR[i] >= max_mean_HR*0.65) and (HR[i] < max_mean_HR*0.75):
        HR_kat[3] = HR_kat[3] + 1;
    elif (HR[i] >= max_mean_HR*0.55) and (HR[i] < max_mean_HR*0.65):
        HR_kat[4] = HR_kat[4] + 1;
    else:
        HR_kat[5] = HR_kat[5] + 1;

#chi square test
data = [MI_kat, HR_kat]
stat, p, dof, expected = chi2_contingency(data)
alpha = 0.05
print("stat value is " + str(stat))
print("p value is " + str(p))
print("dof value is " + str(dof))
print("expected value is " + str(expected))
if p <= alpha:
    print('Zavisni. (Odbija se nulta hipoteza).')
else:
    print('Nezavisni. (Prihvata se nulta hipoteza).')
