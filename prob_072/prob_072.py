def main():
    N = 1000000
    phi = range(N+1)
    for i in range(2,N+1):
        if phi[i] == i:
            phi[i] -= 1
            for j in range(2,N/i+1):
                k = i*j
                phi[k] = phi[k]*(i-1)/i
    print sum(phi) - 1


if __name__ == '__main__':
    main()
