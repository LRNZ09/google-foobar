from fractions import *

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(l):
    return reduce(lambda x, y: lcm(x, y), l)

def matmult(a,b):
    zip_b = zip(*b)

    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

def transpose_matrix(m):
    t = []

    for r in range(len(m)):
        t_row = []

        for c in range(len(m[r])):
            if c == r:
                t_row.append(m[r][c])
            else:
                t_row.append(m[c][r])

        t.append(t_row)

    return t

def get_matrix_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def get_matrix_determinant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0

    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*get_matrix_determinant(get_matrix_minor(m,0,c))

    return determinant

def get_matrix_inverse(m):
    determinant = get_matrix_determinant(m)

    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []

    for r in range(len(m)):
        cofactor_row = []

        for c in range(len(m)):
            minor = get_matrix_minor(m,r,c)
            cofactor_row.append(((-1) ** (r + c)) * get_matrix_determinant(minor))

        cofactors.append(cofactor_row)

    cofactors = transpose_matrix(cofactors)

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant

    return cofactors

def solution(m):
    if len(m) == 1:
        return [1, 1]

    abso = []
    nabso = []

    for ind, val in enumerate(m):
        if sum(val) == 0:
            abso.append(ind)
        else:
            nabso.append(ind)

    if len(abso) == 1:
        return [1, 1]

    order = abso + nabso

    lim_m = []
    n = 0

    for i in abso:
        lim_m.append(m[i])
        lim_m[n][n] = 1
        n += 1

    for i in nabso:
        m_temp, lim_temp = [], []

        for n in order:
            m_temp.append(m[i][n])

        for ind, val in enumerate(m_temp):
            lim_temp.append(Fraction(val, sum(m_temp) ))

        lim_m.append(lim_temp)

    i_list, r_list, q_list = [], [], []

    for p in range(len(abso),len(lim_m)):
        r_list.append(lim_m[p][:len(abso)])
        q_list.append(lim_m[p][len(abso):])

    for u in range(0, len(q_list)):
        i_temp = [0] * len(q_list)
        i_temp[u] = 1
        i_list.append(i_temp)

    i_q_list = []

    for p in range(0, len(i_list)):
        i_q_temp = []

        for o in range(0, len(i_list[0])):
            i_q_temp.append(i_list[p][o]-q_list[p][o])

        i_q_list.append(i_q_temp)

    inverse_matrix = get_matrix_inverse(i_q_list)

    fr = matmult(inverse_matrix, r_list)

    alm = []
    for i in fr[0]:
        alm.append([i.numerator, i.denominator])

    lcm1 = lcmm([i[1] for i in alm])

    ende = [ (lcm1/i[1]) * i[0] for i in alm ]
    return ende + [lcm1]
