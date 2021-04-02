import matplotlib.pyplot as plt

def saisie_livre():
	Dlivre={}
	nbr_livres = 0
	
	while nbr_livres < 1:
		nbr_livres=int(input('donner un nombre de livres superieur ou egale a 10:'))
		
	while nbr_livres > 0:
		ISSBN=int(input('donner ISSBN:'))
		titre=input('donner le titre:')
		auteur=input('donner le nom de lauteur:')
		date=input('donner la date dedition:')
		maison=input('donner la maison dedition:')
		nbxp=int(input('donner le nombre dexemplaires:'))
		
		nbr_livres=nbr_livres-1
		
		Dlivre={'ISSBN':ISSBN, 'titre':titre, 'auteur':auteur, 'date':date, 'maison':maison, 'nbxp':nbxp}
		f1=open('livres.txt', 'a')
		f1.write(str(Dlivre['ISSBN']) + ';' + Dlivre['titre'] + ';' + Dlivre['auteur'] + ';' + Dlivre['date'] + ';' + Dlivre['maison'] + ';' + str(Dlivre['nbxp']) + '\n')
		f1.close()
		f2=open('nbrlivres.txt','a')
		f2.write(str(Dlivre['ISSBN']) + ';' + str(Dlivre['nbxp']) + '\n')
		f2.close()
		
	return(Dlivre)

def saisie_adherent():
	Dadherent={}
	
	CIN=int(input('donner CIN:'))
	nom=input('donner le nom:')
	prenom=input('donner le prenom:')
	age=int(input('donner lage:'))
	num_tel=int(input('donner le numero de telephone:'))
	
	Dadherent[CIN]={}
	Dadherent[CIN]=(nom, prenom, age, num_tel)
	
	f2=open('adherent.txt','a')
	for CIN in Dadherent.keys():
		f2.write(str(CIN) + ';' + Dadherent[CIN][0] + ';' + Dadherent[CIN][1] + ';' + str(Dadherent[CIN][2]) + ';' + str(Dadherent[CIN][3]) + '\n')
	f2.close()

def emprunt_livre():
	CIN_list=[]
	ISSBN_list=[]
	
	f1=open('livres.txt','r')
	f2=open('adherent.txt','r')
	f3=open('emprunt.txt','a')
	CIN=int(input('donner CIN:'))
	ISSBN=int(input('donner ISSBN:'))
	date_emprunt = input('donner la date demprunt:')
	nbr_jour = int(input('donner le nombre de jours:'))
	
	x = 0
	contenu = ''
	
	for ligne1 in f1:
		l1 = ligne1.split(';')
		ISSBN_list.append(l1[0])
	f1.close()
	for ligne2 in f2:
		l2 = ligne2.split(';')
		CIN_list.append(l2[0])
	f2.close()

	for i in ISSBN_list:
		for j in CIN_list:
			if (int(i) == ISSBN) and (int(j) == CIN):
				f3.write(str(CIN) + ';' + str(ISSBN) + ';' + date_emprunt + ';' + str(nbr_jour) + '\n')
			f1=open('livres.txt','r')
			for ligne2 in f1:
				l2 = ligne2.split(';')
				if int(l2[0]) == ISSBN:
					x = int(l2[5]) - 1
					contenu = l2[0] + ';' + l2[1] + ';' + l2[2] + ';' + l2[3] + ';' +l2[4] + ';' + str(x) + '\n'
			f1.close()
			
	f1=open('livres.txt','r')
	lignes = f1.readlines()
	f1.close()
	
	if x < 0:
		print('pas de livres\n')
	else:
		for n in range (len(lignes)):
			if str(ISSBN) in lignes[n]:
				lignes[n] = contenu
				f1=open('livres.txt','w')
				f1.writelines(lignes)
				f1.close()

			
def rendu_livre():
	CIN_list=[]
	ISSBN_list=[]
	
	f1=open('livres.txt','r')
	f2=open('adherent.txt','r')

	CIN=int(input('donner CIN:'))
	ISSBN=int(input('donner ISSBN:'))
	date_emprunt = input('donner la date demprunt:')
	nbr_jour = int(input('donner le nombre de jours:'))
	date_rendu = input('donner la date de rendu:')

	for ligne1 in f1:
		l1 = ligne1.split(';')
		ISSBN_list.append(l1[0])
	f1.close()
	for ligne2 in f2:
		l2 = ligne2.split(';')
		CIN_list.append(l2[0])
	f2.close()

	for i in ISSBN_list:
		for j in CIN_list:
			if (int(i) == ISSBN) and (int(j) == CIN):
				f1=open('livres.txt','r')
				for ligne2 in f1:
					l2 = ligne2.split(';')
					print(int(l2[0]))
					if int(l2[0]) == ISSBN:
						x = int(l2[5]) + 1
						contenu = l2[0] + ';' + l2[1] + ';' + l2[2] + ';' + l2[3] + ';' +l2[4] + ';' + str(x) + '\n'
				f1.close()
				f1=open('livres.txt','r')
				lignes = f1.readlines()
				f1.close
				for n in range (len(lignes)):
					if str(ISSBN) in lignes[n]:
						lignes[n] = contenu
				f1=open('livres.txt','w')
				f1.writelines(lignes)
				f1.close()

def statistique_livre():
        nbr_emprunt = 0
        emprunt = []
        liste_ISSBN = []
        liste_exemplaire = []
        l_ISSBN = []
        l_exemplaire = []
        
        f1=open('livres.txt','r')
        f2=open('livres.txt','r')
        f3=open('nbrlivres.txt','r')
        
        for ligne1 in f1:
                ISSBN = ligne1.split(';')
                liste_ISSBN.append(ISSBN[0])
        for ligne2 in f2:
                nbr_xp = ligne2.split(';')
                liste_exemplaire.append(int(nbr_xp[5]))
        for lignes in f3:
                l=lignes.split(';')
                l_ISSBN.append(l[0])
                l_exemplaire.append(int(l[1]))
                
        for i in range(0,len(liste_ISSBN)):
                if liste_ISSBN[i] == l_ISSBN[i]:
                       emprunt.append(l_exemplaire[i]-liste_exemplaire[i])
                
        f1.close()
        f2.close()
        f3.close()
        plt.plot(emprunt,l_ISSBN)
        plt.show()

        

			
print(saisie_livre())
#saisie_adherent()
#emprunt_livre()
#rendu_livre()
#saisie_livre().keys()

x = 1
while(x!=0):
	x = int(input("1-creer liste des livres \n2-creer la liste des adherents \n3- creer le fichier emprunt.txt \n4-rendre livre \n5-statistique d'emprunt\n0-quitter"))
	if x == 1:
		saisie_livre()
	elif x == 2:
		saisie_adherent()
	elif x == 3:
		emprunt_livre()
	elif x == 4:
		rendu_livre()
	elif x == 5:
		statistique_livre()
