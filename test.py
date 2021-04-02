dict_test = {
	1:'alice',
	2:'charlie',
	3:'bob'
}

def greeting(key):
	print('hello %s' %dict_test[key])


def saisie_livre():
	nbr_livre = 0
	Dlivre={}
	while(nbr_livre < 2):
		ISSBN=int(input('donner ISSBN:'))
		titre=input('donner le titre:')
		auteur=input('donner le nom de lauteur:')
		date=input('donner la date dedition:')
		maison=input('donner la maison dedition:')
		nbxp=int(input('donner le nombre dexemplaires:'))
		nbr_livre+=1
		Dlivre={'ISSBN':ISSBN, 'titre':titre, 'auteur':auteur, 'date':date, 'maison':maison, 'nbxp':nbxp}
	f1=open('livress.txt', 'a')
	f1.write(str(Dlivre['ISSBN']) + ';' + Dlivre['titre'] + ';' + Dlivre['auteur'] + ';' + Dlivre['date'] + ';' + Dlivre['maison'] + ';' + str(Dlivre['nbxp']) + '\n')
	f1.close()
	return(Dlivre)


dic = saisie_livre()
print(dic)
val = saisie_livre().values()
print(val)
