print "/n## O ##n/"
 print "-----------"
 print "Suma de"
 print "---------"
 def melacomplican_1 (x, n, m):
 	if x == (n + m):
 		print ("%s es resultado de la suma de %s + %s") % (x, n, m)
 	elif n == (m + x):
 		print ("%s es resultado de la suma de $s + %s") % (n, m, x)
 	else:
 		print ("%s es producto de la suma de %s + %s") % (m, n, x)
 x = input ("Ingrese un primer numero: ")
 n = input ("Ingrese un segundo numero: ")
 m = input ("Ingrese un tercer numero: ")
 melacomplican_1 (x, n, m)