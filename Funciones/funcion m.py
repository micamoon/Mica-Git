print "/n## M ##n/ "
print "------------"
 print "Rangos"
 print "------"
 def rang_o (x):
 	l1 = 4
 	l2 = 6
 	print "Rango 4,5,6"
 	if x < 4:
 		print " El numero que has ingresado se encuentra a la IZQUIERDA del rango", x
 	elif x > 6:
		print "El numero que has ingresado se encuentra a la DERECHA del rango", x
 	else:
 		print "El numero que has ingresado se encuentra DENTRO del rango"

 x = input ("Ingrese un numero:(0 a 9)")
 rang_o (x)