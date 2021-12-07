import numpy as np
import matplotlib.pyplot as plt


def sol7():
    with open('../data/advent_7.txt') as f:
        data = list(map(int, f.read().split(',')))

    positions = []
    fuel_costs = []

    best_fuel_cost = 10000000000
    best_position = min(data)

    for i in range(min(data), max(data)):
        fuel_cost = 0
        for position in data:
            diff = abs(position - i)
            fuel_cost += ((diff * (diff + 1)) // 2)
        fuel_costs.append(fuel_cost)
        positions.append(i)
        print('Checking Position: {0} with Fuel cost: {1} '.format(i, int(fuel_cost)))
        if fuel_cost < best_fuel_cost:
            best_fuel_cost = fuel_cost
            best_position = i

    print('Best position is: {0} with fuel cost: {1}'.format(best_position, int(best_fuel_cost)))

    fuel_costs = np.array(fuel_costs)
    positions = np.array(positions)

    arrow = dict(
        facecolor="black", width=0.5,
        headwidth=4, shrink=0.1)

    plt.title('Plotting the Fuel Costs against the Positions')
    plt.xlabel('Positions')
    plt.ylabel('Fuel Cost')
    plt.plot(positions, fuel_costs, color='black')
    plt.plot([best_position], [best_fuel_cost], marker="o", label='Optimal value', color='red')
    plt.annotate('Best position: {0}'.format(best_position), xy=(best_position, best_fuel_cost),
                 xytext=[best_position / 2.2, best_fuel_cost * 4], arrowprops=arrow)
    plt.legend()
    plt.show()


sol7()
