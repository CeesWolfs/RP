import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from matplotlib import rc

# Exercise one
w = 1.0
Q = np.inf
m = 1.0
F = 1.0

rc('text', usetex=True)
linestyles = ['-', '--', '-.', ':']
initial = [0,0]
t_start = 0
t_end = 20

def solvr(Y, t):
    return [Y[1], -w*w*Y[0]-(w/Q)*Y[1]+F*np.cos(w*t)/m]
def ex1():
    a_t = np.arange(t_start, t_end, 0.01)
    asol = integrate.odeint(solvr, initial, a_t)
    plt.plot(a_t, asol[:,0], label=r'$Q = \infty$')
    plt.xlabel("t (s)")
    plt.ylabel("x(t) (m)")
    #plt.ylim(-5000, 5000)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(-3,3))
    plt.legend()
    plt.show()

#exercise two    
    
def plot2(Q):
    plt.figure()
    i = 0
    for T in (.1,1,10):
        def solvr(Y, t):
            if(t>T):
                return [Y[1], -w*w*Y[0]-(w/Q)*Y[1]]
            return [Y[1], -w*w*Y[0]-(w/Q)*Y[1]+F*np.cos(w*t)/m]
        a_t = np.arange(t_start, t_end, 0.01)
        asol = integrate.odeint(solvr, initial, a_t)
        plt.plot(a_t, asol[:,0], label="T = "+str(T),linestyle=linestyles[i])
        plt.title(r'$Q = \infty$') if Q == np.inf else plt.title(r'$Q = $'+str(Q))
        plt.xlabel("t (s)")
        plt.ylabel("x(t) (m)")
        plt.ticklabel_format(style='sci', axis='y', scilimits=(-3,3))
        plt.legend()
        i += 1
        plt.savefig("ex2Q="+str(Q)+".pdf")

def ex2():
    for Q in (-1,1,np.inf):
            plot2(Q)
    
#exercise three    
    
def plot3(Q):
    plt.figure()
    i = 0
    for T in (.1,1,10):
        def solvr(Y, t):
            if(t>T):
                return [Y[1], -w*w*Y[0]-(w/Q)*Y[1]]
            return [Y[1], -w*w*Y[0]-(w/Q)*Y[1]+F*t*(T-t)/(m*T*T)]
        a_t = np.arange(t_start, t_end, 0.01)
        asol = integrate.odeint(solvr, initial, a_t)
        plt.plot(a_t, asol[:,0], label="T = "+str(T), linestyle=linestyles[i])
        plt.xlabel("t (s)")
        plt.ylabel("x(t) (m)")
        plt.title(r'$Q = \infty$') if Q == np.inf else plt.title(r'$Q = $'+str(Q))
        plt.legend()
        plt.ticklabel_format(style='sci', axis='y', scilimits=(-3,3))
        i+=1
        plt.savefig("ex3Q="+str(Q)+".pdf")

def ex3():
    for Q in (-1,1,np.inf):
            plot3(Q)
def main():
    ex1()
        

if __name__ == '__main__':
    main()