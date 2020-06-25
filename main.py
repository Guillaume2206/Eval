# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)


###### exercice 01
def makeDico_R6(nomFichier, sep):
  dico = {}
  nbLines = 0
  file = open(nomFichier, "r")
  for line in file:
    nbLines += 1
    dico[line.split(sep)[0]] = line.split(sep)[1]
  print("Création d'un dictionnaire a partir du fichier {} avec {} entrées\n".format(nomFichier, nbLines))
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
def VerifTLD_M1(tldOk,tld):
  result = False
  for i in tldOk:
    if tld == i:
      result = True
  if result == False:
    print("TLD absente")
  return result

###### exercice 05
def ipVerifFormat_Z6(adresseIp):
  result = True
  if adresseIp.count(".") == 3:
    for i in range(0,len(adresseIp.split("."))):
      if int(adresseIp.split(".")[i]) < 0 or int(adresseIp.split(".")[i]) > 255:
        print("champ d’adresse incorrect")
        result = False
  else:
    print("nombre de champs incorrect")
    result =  False
  return result

###### exercice 06
def makeTLD_W5(dico):
  listTLD = []
  nbTLD = 0
  for elem in dico:
    if listTLD.count(elem.split(".")[1]) == 0:
      listTLD.append(elem.split(".")[1])
      nbTLD += 1
  print("Creation d'une liste de TLD comprenant {} entrees".format(nbTLD))
  return listTLD

# Zone 2 ## zone pour les classes
###### exercice 07
class serveurDns_U8:
  __dns = {}
  def __init__(self, resolDns):
    self.__dns = resolDns

###### exercice 08
  def resolDNS_I3(self, url):
    if verifUrl_B5(url):
      for elem in self.__dns:
        if elem == url:
          return url
        else:
          print("url introuvable")
          return False
    else:
      print("erreur de format de l’url")
      return False

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
  print(str(VerifTLD_M1(["io","de","com","fr"],"fr")) + "\n")

	###### exercice 05
  print("exercice 05 #######################")
  print(str(ipVerifFormat_Z6("192.168.2.1")) + "\n")

	###### exercice 06
  print("exercice 06 #######################")
  print(str(makeTLD_W5(dicoDNS)) + "\n")
	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")
  serverDNS = serveurDns_U8(dicoDNS)

	###### exercice 08
  print("exercice 08 #######################")
  serverDNS.

	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
	print("main()")
	main()