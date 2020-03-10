import copy

def MoverCero(matrizN, EdoFinal, listaEdos, x, y, indice):
	newList=copy.deepcopy(listaEdos)
	for i in range (3):
		if (Comparar(matrizN, EdoFinal)==False and validacion(y-1)):
			newList=copy.deepcopy(newList)
			
			copyM=copy.deepcopy(matrizN)
			copyx=copy.deepcopy(x)
			copyy=copy.deepcopy(y)
			Izquierda(copyM, x, y)
			#for i in range (len(newList)):
			#		Imprimir(newList[i])		
			if (visitado(copyM, newList)==False):
				print("Izquierda")
				matrizN = copy.deepcopy(newList[indice])
				x, y=localizarC(matrizN)
				Izquierda(matrizN, x, y)
				Imprimir(matrizN)
				newList.append(matrizN)

			
		if(Comparar(matrizN, EdoFinal)==False and validacion(x-1) ):
			newList=copy.deepcopy(newList)

			copyM=copy.deepcopy(matrizN)
			copyx=copy.deepcopy(x)
			copyy=copy.deepcopy(y)
			Arriba(copyM, x, y)
			#for i in range (len(newList)):
			#		Imprimir(newList[i])		
			if (visitado(copyM, newList)==False):
				print("Arriba")
				matrizN = copy.deepcopy(newList[indice])
				x, y=localizarC(matrizN)
				Arriba(matrizN, x, y)
				Imprimir(matrizN)
				newList.append(matrizN)

						
			
			
		if(Comparar(matrizN, EdoFinal)==False and validacion(y+1) ):
			newList=copy.deepcopy(newList)
#
			copyM=copy.deepcopy(matrizN)
			copyx=copy.deepcopy(x)
			copyy=copy.deepcopy(y)
			Derecha(copyM, x, y)
			#for i in range (len(newList)):
			#		Imprimir(newList[i])		
			if (visitado(copyM, newList)==False):
				#print(visitado(copyM, newList))
				print("Derecha")
				matrizN = copy.deepcopy(newList[indice])
				x, y=localizarC(matrizN)
				Derecha(matrizN, x, y)
				Imprimir(matrizN)
				newList.append(matrizN)
				
#
		if(Comparar(matrizN, EdoFinal)==False and validacion(x+1)):
			newList=copy.deepcopy(newList)
#
			copyM=copy.deepcopy(matrizN)
			copyx=copy.deepcopy(x)
			copyy=copy.deepcopy(y)
			Abajo(copyM, x, y)
			#for i in range (len(newList)):
			#		Imprimir(newList[i])		
			if (visitado(copyM, newList)==False):
				print("Abajo")
				matrizN = copy.deepcopy(newList[indice])
				x, y=localizarC(matrizN)
				Abajo(matrizN, x, y)
				Imprimir(matrizN)
				newList.append(matrizN)
				
				#for i in range (len(newList)):
				#	Imprimir(newList[i])					
			if(visitado(matrizN, newList)==True):
				print("entra")
				indice+=1
				matrizN = copy.deepcopy(newList[indice])
				x, y=localizarC(matrizN)
				
	return x, y, newList

def localizarC(matrizN):
	for i in range (3):
		a=matrizN[i][0:3]
		if (0 in a):
			y=a.index(0)
			x=i
	return x, y

def Izquierda(matrizN, x, y):	
		
	cero=matrizN[x][y]
	Nizquierda=matrizN[x][y-1]

	matrizN[x][y]=Nizquierda
	matrizN[x][y-1]=cero
	x=x
	y=y-1

	

def Arriba(matrizN, x, y):
	cero=matrizN[x][y]
	Narriba=matrizN[x-1][y]
	matrizN[x][y]=Narriba
	matrizN[x-1][y]=cero
	x=x-1
	y=y
	
	

def Derecha(matrizN, x, y):
		
	cero=matrizN[x][y]
	Nderecha=matrizN[x][y+1]

	matrizN[x][y]=Nderecha
	matrizN[x][y+1]=cero
	x=x
	y=y+1
	
	

def Abajo(matrizN, x, y):
	
	cero=matrizN[x][y]
	Nabajo=matrizN[x+1][y]

	matrizN[x][y]=Nabajo
	matrizN[x+1][y]=cero
	x=x+1
	y=y
	
	

def validacion(num): #para saber antes de mover, que no se salga de los limites de la matriz
	if num<0 or num>2:
		return False
	else:
		return True

def visitado(matrizN, newList):# para saber si ya fue visitado ese Estado
	if (matrizN in newList):
		return True
	else:
		return False

def Comparar(matrizN, EdoFinal):#para checar en cada Estado si ya ha llegado al final
	if (matrizN==EdoFinal):
		return True
	else:
		return False

def Imprimir(mat):
	for i in range (3):
		print(mat[i][0:3])
	print("\n")



matrizN=[[5,2,4],
		 [3,0,1],
		 [8,7,6]]

EdoFinal=[[1,2,3],
		  [4,5,6],
		  [7,8,0]]

listaEdos=[]

#son las coordenadas del cero
x=0
y=1

listaEdos.append(matrizN)
x,y,p=MoverCero(matrizN, EdoFinal, listaEdos, x, y, 0)

#en p se guarda la lista de estados
#for i in range (len(p)):
#	Imprimir(p[i])

#if (EdoFinal==auxiliar):
#	print("True")
#else:
#	print("False")
#
#for i in range (3):
#	print(EdoFinal[i][0:3])


