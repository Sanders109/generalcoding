import numpy as np


def deflection(q, h, E, nu, TOL):
    D = ((E*h**3)/(12*(1-nu**2);

    a=q/(64*(np.pi**5)*D);
    summn=0;
    k=0
    space=np.linspace(1, 199, 2)

    for i in space
        b=(((-1)**((i-5)/2))*(4*i*np.pi*np.sinh(2*i*np.pi)+4*cosh(2*m*pi)))/(m ^ 5*(exp(-2*m*pi)-exp(2*m*pi) ^ 2;
        k=k + 1;
        sumn=sumn + b;
        if b < TOL:
            break

    y=a*sumn;
