import argparse
import math
import numpy as np
import matplotlib.pyplot as plt

def plot(st, ed, t, params, labels):
    for idx in range(len(params)):
        plt.subplot(len(params), 1, idx+1)
        plt.plot(t[st:ed], params[idx][st:ed])
        plt.xlabel("t")
        plt.ylabel(labels[idx])
        plt.yticks([0])
        plt.grid()

def hysteresis(args):
    # Jiles–Atherton model

    H = [0.0]
    delta = [0.0]
    Man = [0.0]
    M = [0.0]

    for i in range(args.Nfirst):
        H.append(H[-1] + args.DeltaH)

    for i in range(args.Ndown):
        H.append(H[-1] - args.DeltaH)

    for i in range(args.Nup):
        H.append(H[-1] + args.DeltaH)

    delta = [0]
    for i in range(len(H) - 1):
        if H[i + 1] > H[i]:
            delta.append(1)
        else:
            delta.append(-1)

    for n in range(args.Nfirst + args.Ndown + args.Nup):
        Man.append(args.Ms*(1/np.tanh((H[n+1]+args.alpha*M[n])/args.a)-args.a/(H[n+1]+args.alpha*M[n])))
        M.append(M[n]+(Man[n+1]-M[n])/(args.k*delta[n]-args.alpha*(Man[n+1]-M[n]))/(1+args.c)*(H[n+1]-H[n])+args.c/(1+args.c)*(Man[n+1]-Man[n]))

    plt.plot(H, M)
    plt.show()

def main(args):
    if args.save:
        plt.figure(figsize=(6,9))
    
    w = 2*math.pi*args.f

    for Hd in range(2,10,2):
        H = [Hd]
        B = [0.0]
        e = [0.0]
        v = [0.0]
        i = [0.0]
        t = [0.0]

        Man = [0.0]
        M = [0.0]
        delta = [0.0]

        for n in range(int(args.T/args.dt)):
            Ha = args.Hm*math.sin(w*args.dt*n)
            H.append(Ha + Hd)
            if H[n + 1] > H[n]:
                delta.append(1)
            else:
                delta.append(-1)
            Man.append(args.Ms*(1/np.tanh((H[n+1]+args.alpha*M[n])/args.a)-args.a/(H[n+1]+args.alpha*M[n])))
            M.append(M[n]+(Man[n+1]-M[n])/(args.k*delta[n]-args.alpha*(Man[n+1]-M[n]))/(1+args.c)*(H[n+1]-H[n])+args.c/(1+args.c)*(Man[n+1]-Man[n]))
            B.append(args.mu0*M[n])
            e.append(-args.N*args.S*(B[n+1]-B[n])/args.dt)
            v.append(abs(e[n]))
            i.append(i[n]+args.dt*(v[n]-args.Rf*i[n])/args.Lf)
            t.append(args.dt*n)
        plot(args.st, args.ed, t,
            [H,B,e,v,i],
            ["H", "B", "E", "Er", "If"])

    if args.save:
        plt.savefig("fig/res.jpg", dpi=300, bbox_inches='tight')
    else:
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Params')
    parser.add_argument('--dt', type=float, default=0.0001) # s
    parser.add_argument('--T', type=float, default=1) # s
    parser.add_argument('--f', type=int, default=60) # Hz

    # transformer
    parser.add_argument('--mu0', type=float, default=4 * np.pi * 1e-7) # H/m
    parser.add_argument('--a', type=float, default=1) # A/m
    parser.add_argument('--alpha', type=float, default=1e-5)
    parser.add_argument('--c', type=float, default=0.1)
    parser.add_argument('--k', type=float, default=1) # A/m
    parser.add_argument('--Ms', type=float, default=1e5) # A/m

    parser.add_argument('--Hm', type=float, default=5) # A/m
    parser.add_argument('--S', type=float, default=1)
    parser.add_argument('--N', type=float, default=1)

    parser.add_argument('--Lf', type=float, default=1) # H
    parser.add_argument('--Rf', type=float, default=1) # Ohm

    parser.add_argument('--st', type=float, default=-500)
    parser.add_argument('--ed', type=float, default=-1)

    # hysteresis plot
    parser.add_argument('--DeltaH', type=float, default=0.001)
    parser.add_argument('--Nfirst', type=float, default=10000)
    parser.add_argument('--Ndown', type=float, default=20000)
    parser.add_argument('--Nup', type=float, default=20000)

    # flag
    parser.add_argument('--norm', action='store_true')
    parser.add_argument('--hysteresis', action='store_true')
    parser.add_argument('--save', action='store_true')

    args = parser.parse_args()
    
    if(args.hysteresis):
        hysteresis(args)
    else:
        main(args)
