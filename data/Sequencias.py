num_bits = int(input("Informe numero de entradas: "))
total_seq = (2**num_bits)
sequencia = []
comb = []

x = 0
while x < total_seq:
    v_bin = format(x, 'b')  #type str
    v_bin_real = list(v_bin) #type list

    aux = 0
    while aux < (num_bits - len(v_bin)):
        v_bin_real.insert(0, '0')
        aux += 1
   
    valor = 'b'
    for i in v_bin_real:
        valor = valor + i
    valor = valor[1:]
    sequencia.append(valor)

    y = 0
    tam_bin = len(sequencia[y])
    while y < tam_bin:
        binario = sequencia[x]
        if binario[y] == '0':
            b = binario
            prox_bin_list = list(b)
            prox_bin_list[y] = '1'

            prox_valor = 'b'
            for j in prox_bin_list:
               prox_valor = prox_valor + j

            prox_valor_sb = prox_valor[1:]
            comb.append(prox_valor_sb)
        else:
            b = binario
            prox_bin_list = list(b)
            prox_bin_list[y] = '0'

            prox_valor = 'b'
            for j in prox_bin_list:
               prox_valor = prox_valor + j

            prox_valor_sb = prox_valor[1:]
            comb.append(prox_valor_sb)

        y += 1
    x += 1
    
print("A sequencia eh:", sequencia)
print('As combinações são:', comb)

data = open("data.txt", "a")

k = 0
l = 0

data.write("bits_")
data.write(str(num_bits))
data.write(" = [\n")

while k < len(sequencia):
    int_comb = 0
    while l < len(comb):
        if int_comb < num_bits:
            aux1 = int(sequencia[k], 2) + 1
            aux2 = int(comb[l], 2) + 1

            data.write("(")
            data.write(str(aux1))
            data.write(",")
            data.write(str(aux2))
            data.write(",1, True)\n")
            l += 1
        else:
            break
        int_comb += 1
    k += 1
data.write("]\n\n")
