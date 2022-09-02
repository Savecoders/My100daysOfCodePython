
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

yearDataOne = [2016, 2017, 2018, 2019, 2020, 2021]
rankingOne = [46, 42, 41, 47, 30, 21]

yearDataTwo = [2016, 2017, 2018, 2019, 2020, 2021]
rankingTwo = [45, 46, 47, 48, 50, 51]

# create graphic data

plt.plot(yearDataOne, rankingOne, marker='o',
         linestyle='--', color='g', label='Country One')

plt.plot(yearDataTwo, rankingTwo, marker='o',
         linestyle='--', color='g', label='Country One')


plt.xlabel('Year')
plt.ylabel('Rank ')
plt.title('Year vs Rank')
plt.legend(loc='lower right')


fig
