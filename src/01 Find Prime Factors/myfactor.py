

def get_prime_factors(num, candidate=2):
    ''' list of prime factors = get_prime_factors(x)'''
#    print(f'num={num}  ;  candidate={candidate}')

    prime_factors = []
    if num > 1:
        while num >= candidate:
            if num == candidate:
                # print('==')
                prime_factors.append(candidate)
                break
            elif num % candidate != 0:
                # print('!=0')
                prime_factors = prime_factors + \
                    get_prime_factors(num, candidate+1)
                break
            elif num % candidate == 0:  # candidate is a factor    6%2=3
                #print(f'appending {candidate}')
                prime_factors.append(candidate)              # 2
                num = num // candidate
                #print(f'new number = {num}')
                prime_factors = prime_factors + \
                    get_prime_factors(num)        # 3,2
                break

    return prime_factors


if __name__ == "__main__":
    i = 4
    pf = get_prime_factors(i)
    print(f'{i}: {pf}')

    for i in range(2, 20):
        pf = get_prime_factors(i)
        print(f'{i}: {pf}')
