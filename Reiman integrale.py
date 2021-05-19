#programmable by Belhaj Ayman (JS5)
import matplotlib.pyplot as plt
import numpy as np
def get_sequence_trap_down(f,a,b,n):
    x = [a+i*((b-a)/n) for i in range(0,n+1)]
    y = [f(a+i*((b-a)/n)) for i in range(0,n+1)]
    return (x[:len(x)-1],y[:len(y)-1])
def get_sequence_trap_up(f,a,b,n):
    x = [a+i*((b-a)/n) for i in range(0,n+1)]
    y = [f(a+(i+1)*((b-a)/n)) for i in range(0,n+1)]
    return (x[:len(x)-1],y[:len(y)-1])
def R(f,a,b,n):
    x =0
    for i in range(0,n):
        x+=f(a+i*((b-a)/n))
    return ((b-a)/n)*x
def T(f,a,b,n):
    x =0
    for i in range(1,n+1):
        x+=f(a+i*((b-a)/n))
    return ((b-a)/n)*x
def repre(f,a,b,frame,second):
    n=1
    for i in range(1,frame+1):
        x1,y1=get_sequence_trap_up(f,a,b,n)
        x2,y2=get_sequence_trap_down(f,a,b,n)
        plt.bar(x1,y1,color='blue',align='edge',width=(b-a)/n,ec='black',label='Reiman Up')
        plt.bar(x2,y2,color='yellow',align='edge',width=(b-a)/n,ec='black',label='Reiman Down')
        o=np.linspace(a,b,100)
        plt.plot(o,f(o),color='red',label='f')
        plt.legend()
        plt.title(r'$'+str(R(f,a,b,n))+' < \int_{}^{} f  \,dx \ <'+str(T(f,a,b,n))+' $')
        plt.pause(second)
        n+=1
        if i <frame:
            plt.clf()
    plt.show()
print(repre(lambda x :np.exp(x),-2,1,50,0.1))
#print(repre(lambda x :np.log(x)+1,1,10,10,0.1))