mat = {
    1: [1, 2, 3],
    2: [4, 5, 6],
    3: [7, 8, 9]
   
}

matrx_01 = mat[1]
matrx_02 = mat[2]
matrx_03 = mat[3]
l1, l2, l3, = matrx_01[0], matrx_02[1], matrx_03[2]
primary= [l1,l2,l3]
l4, l5, l6 = matrx_01[2], matrx_02[1], matrx_03[0]
secondary=[l4,l5,l6]
diffrence = sum(primary) - sum(secondary)
print(diffrence)