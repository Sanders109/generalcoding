import numpy as np


def material(L, w, I, E, n):
    x = np.arange(0, L, n)
    Y = np.zeros(n, m)
    for i in range(len(x)):
        if 0 <= x[i] < L/3:
            for m in range(len(E)):
                Y[i][m] = ((w*x[i])/(8*L*E[m]*I))*(((L**2+L*x[i])/3)+((L*x[i]**2)/27)
                                                   * (9*x[i]-19*L)-((56*L**2)/243)-((2*(L**3)*x[i])/3))
        if L/3 < x[i] < L:
            for m in range(len(E)):
                Y[i][m] = (((w*(x[i]-L))/(54*L*E[m]*I)) *
                           ((L**4)/36+(x/2)*(x[i]*L**2-2*L**3)))

    return x, Y
