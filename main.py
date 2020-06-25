# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)


###### exercice 01
def makeDico_R6(filename, sep):
  dico = {}
  nbLines = 0
  file = open(filename, "r")
  for line in file:
    nbLines += 1
    dico[line.split(sep)[0]] = line.split(sep)[1]
  print("Création d'un dictionnaire a partir du fichier {} avec {} entrées\n".format(filename, nbLines))
  return dico

###### exercice 02
def verifUrl_B5(url):
  if len(url.split(".")) == 2 and len(url.split(".")[1]) <= 3:
    return True
  else:
    print("url mal formée")
    return False

###### exercice 03
def getTLD_V3(url):
  if verifUrl_B5(url):
    return url.split(".")[1]
  else:
    print("TLD mal formée")
    return False

###### exercice 04


###### exercice 05
    

###### exercice 06


# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09
    

# Zone 3 ## zone pour les tests des fonctions

def main() :
  from re import split
	###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
  print("exercice 00 #######################")
  salutations = exempleHello("Michel")
  print(salutations)
  print(salutations.split(sep=" "))
  
  ###### exercice 01
  print("exercice 01 #######################")
  dicoDNS = makeDico_R6("dns.txt", ",")

	###### exercice 02
  print("exercice 02 #######################")
  print(str(verifUrl_B5("curiousong.fr")) + "\n")

	###### exercice 03
  print("exercice 03 #######################")
  print(str(getTLD_V3("curiousong.fr")) + "\n")

	###### exercice 04
  print("exercice 04 #######################")


	###### exercice 05
  print("exercice 05 #######################")


	###### exercice 06
  print("exercice 06 #######################")

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")


	###### exercice 08
  print("exercice 08 #######################")


	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
	print("main()")
	main()