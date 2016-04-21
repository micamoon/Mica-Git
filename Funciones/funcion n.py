print "/n## N ##n/"
 print "-----------"
 print "Pies y Pulgadas"
 print "----------------"
 def conver_mpp (x):
 	pu = 39.37
 	pi = 3.28
 	xc = (x * pu)
 	xi = (x * pi)
 	print "El metro ingresado equivale a pulgadas: ", xc 
 	print "Y a pies: ", xi
 x = input ("Ingrese una medida: ") 
 conver_mpp (x)