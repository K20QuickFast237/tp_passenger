#python 3.9.10
import copy

#creer un bus
listeBus = {}
bus = {
    'num'           : 'XX 000 XX',
    'taille'        : 70,
    'chargeMax'     : 1000,
    'listePassagers': [],
    'placesOccupees': 0, 
    'charge'        : 0
}

def create_Bus():
    newBus = copy.deepcopy(bus)
    print('\n Creation guidee d\'un bus')
    newBus['num'] = input('Quel est le numero du bus? (exemple LT 333 DG): ').upper() #think about uppercase the input
    newBus['taille'] = int(input('Ce bus prend combien de places? (exemple 70): '))
    newBus['chargeMax'] = input('Ce bus peut acceuillir combien de kg en soute? (exemple 1000): ')
    listeBus[newBus['num']] = newBus
    print('Vous avez ajoute le bus: \n',newBus,' a votre flotte.')

#creer un passager
listePassagers = {}
passager = {
    'cni'        : '*********',   # 9 digits
    'nom'        : 'NA',
    'poidBagage' : 0.0,
#    'numSiege'   : '**'
}

def create_Passager():
    newPassager = copy.deepcopy(passager)
    print('\n Creation guidee d\'un passager')
    newPassager['cni'] = input('Quel est son numero de cni? (exemple 114850326): ')
    newPassager['nom'] = input('Comment s\'appelle t-il? (exemple Sadio Mane): ')
    newPassager['poidBagage'] = float(input('Combien de kg font ses bagages? (exemple 0): '))
    print('Vous avez ajoute le passager ',newPassager,'.')
    newPassager['numSiege'] = '**'
    listePassagers[newPassager['cni']] = newPassager

#ajouter un passager a un bus   
# actualiser la liste des passagers du bus en question dans la liste des bus, 
# actualiser le nombre de places occupees pour le bus en question dans la liste des bus, et 
# attribuer un numero de siege a ce passager dans la liste des passagers
def add_Passenger_To_Bus():
    print('\n Ajout de passager a un bus')
    bus = input('Entrez le numero du bus auquel ajouter le passager? (Exemple LT 333 DG): ').upper()
    if listeBus.get(bus):
        passager = input('Quel est le numero de cni du passager a ajouter? (exemple 114850326): ')
        if listePassagers.get(passager):
            listeBus[bus]['listePassagers'].append(passager)
            listeBus[bus]['placesOccupees']+=1
            listePassagers[passager]['numSiege'] = len(listeBus[bus]['listePassagers'])
            nom = listePassagers[passager]['nom']
            siege = listePassagers[passager]['numSiege']
            print(f'{nom} est le passager n\'{siege} du bus {bus}.')
        else:
            print('Veuillez d\'abord creer ce passager.')
    else:
        print('Vous n\'avez pas ce bus dans votre flotte.')
    #print(listeBus)
    #print(listePassagers)

#nombre de places dispo dans bus
def places_Dispo_Dans_Bus(bus):
    if listeBus.get(bus):
        designedBus = listeBus[bus]
        places = designedBus['taille'] - designedBus['placesOccupees'] - 1      #place du conducteur
        print(f'Le Bus numero "{bus}" a {places} places disponibles.')
    else:
        print('Vous n\'avez pas ce bus dans votre flotte.')

#nombre de kg reserve
#Additionner les masses des bagages de ses passagers.
def Kilos_Reserve_Dans_Bus(bus):
    if listeBus.get(bus):
        designedBus = listeBus[bus]
        kilos = 0
        for x in designedBus['listePassagers']:
            #aller dans la liste des passager et recuperer le poid de bagage du passager 'x' correspondant
            kilos += listePassagers[x]['poidBagage']    
        print(f'Le Bus numero "{bus}" a deja {kilos}kg de bagages en soutte.')
    else:
        print('Vous n\'avez pas ce bus dans votre flotte.')

#retirer un passager d'un bus
#retirer le numero du passager dans la liste des passagers du bus
#actualiser le nombre de places disponibles dans le bus
#retirer le numero de siege au passager
def retirer_Passager(bus):
    if listeBus.get(bus):
        designedBus = listeBus[bus]
        passager = input('Quel est le numero de cni du passager a retirer? (exemple 114850326): ')
        designedBus['listePassagers'].remove(passager)
        listeBus[bus]['placesOccupees']-=1
        listePassagers[passager]['numSiege'] = '**'
    else:
        print('Vous n\'avez pas ce bus dans votre flotte.')

# savoir si un bus peut acceuillir les passagers venant d'un autre bus

#afficher la liste des passagers d'un bus
#parcourir la liste des passagers du bus en question et afficher leur informations recuperrees dans la liste des passagers.
def affiche_Passagers_Du_Bus(bus):
    if listeBus.get(bus):
        designedBus = listeBus[bus]
        print(f'\nListe des passagers du Bus numero "{bus}":')
        for x in designedBus['listePassagers']:   
            print(listePassagers[x])
    else:
        print('Vous n\'avez pas ce bus dans votre flotte.')

#afficher l'ensemble des passagers de la flotte
def affiche_passagers_flotte():
    print('\n Passagers de la flotte groupe par bus: ')
    for key in listeBus:
        affiche_Passagers_Du_Bus(key)

#savoir si un passager est enregistre sur un bus, le cas echeant, afficher les details du bus
def etat_Passager(bus):
    if listeBus.get(bus):
        passager = input('Quel est le numero de cni du passager a verifier? (exemple 114850326): ')
        if listePassagers.get(passager):
            print(f'Il s\'agit bien d\'un passager du bus {bus} \n {listePassagers[passager]}')
        else:
            print('Veuillez d\'abord creer ce passager.')
    else:
        print('Vous n\'avez pas ce bus dans votre flotte.')

#Main Menu
while True:
    print('''
    ********************************************************************
    ***********   BUS TRAVEL COMPANY MANAGEMENT BY RESTART   ***********
    **********                   MAIN MENU                    **********
    ********  (Enter the item number to select or [0] to exit)  ********
    *****       1- Create a bus                                    *****
    *****       2- Create a passenger                              *****
    *****       3- Add a passenger to a bus                        *****
    *****       4- Get the remaining free places in a bus          *****
    *****       5- Get the lugage(s) weight(in kg) in a bus        *****
    *****       6- Remove a passenger to a bus                     *****
    *****       7- Know if a bus can get passengers from an other one **
    *****       8- Show the passengers list of a bus               *****
    *****       9- Show the global list of passengers              *****
    *****      10- Test if a passenger is in a bus and show        *****
                    passenger details   ''')
    option = int(input('Make your choice: '))

    if (option == 0):
        break
    elif (option == 1):
        create_Bus()
        input('Press Enter to continue')
    elif(option == 2):
        create_Passager()
        input('Press Enter to continue')
    elif(option == 3):
        add_Passenger_To_Bus()
        input('Press Enter to continue')
    elif(option == 4):
        print('\n')
        bus = input('De quel bus voulez-vous les places ? (Exemple LT 333 DG): ').upper()
        places_Dispo_Dans_Bus(bus)
        input('Press Enter to continue')
    elif(option == 5):
        print('\n')
        bus = input('De quel bus voulez-vous le poid des bagages en soutte ? (Exemple LT 333 DG): ').upper()
        Kilos_Reserve_Dans_Bus(bus)
        input('Press Enter to continue')
    elif(option == 6):
        print('\n')
        bus = input('De quel bus voulez-vous retirer un passager ? (Exemple LT 333 DG): ').upper()
        retirer_Passager(bus)
        input('Press Enter to continue')
    elif(option == 7):
        print('\n')
        pass
        input('Press Enter to continue')
    elif(option == 8):
        print('\n')
        bus = input('De quel bus voulez-vous avoir la liste de passagers ? (Exemple LT 333 DG): ').upper()
        affiche_Passagers_Du_Bus(bus)
        input('Press Enter to continue')    
    elif(option == 9):
        print('\n')
        affiche_passagers_flotte()
        input('Press Enter to continue')    
    elif(option == 10):
        print('\n')
        bus = input('Dans quel bus voulez-vous verifier l\'enregistrement du passagers ? (Exemple LT 333 DG): ').upper()
        etat_Passager(bus)
        input('Press Enter to continue')    
    else:
        print('choix Invalide!')