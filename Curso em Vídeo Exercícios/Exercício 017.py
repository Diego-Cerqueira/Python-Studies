from math import hypot as h
cat_oposto = float(input('Digite o catoto oposto:'))
cat_adj = float(input('Digite o cateto adjacente:'))
hipotenusa = h(cat_adj, cat_oposto)
print ('A hipoteunusa vai medir {:.3f}'.format(hipotenusa))