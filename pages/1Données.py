import pandas as pd
import streamlit as st

# Load the dataset
caracteristiques = pd.read_csv("carcteristiques-2022.csv", sep=';')
lieux = pd.read_csv("lieux-2022.csv", sep=';',low_memory=False)
usagers = pd.read_csv("usagers-2022.csv", sep=';')
vehicules = pd.read_csv("vehicules-2022.csv", sep=';')

# Set up the Streamlit app
st.title("Présentation des données utilisées pour l'analyse")

# Create tabs for different data categories
tab1, tab2, tab3, tab4 = st.tabs(["Caractéristiques", "Lieux", "Usagers", "Véhicules"])

# Caractéristiques tab content
with tab1:
    st.dataframe(caracteristiques)
    
    # Explanation of the 'Caractéristiques' data
    st.write("---")
    st.write(
        """
        ### La rubrique CARACTERISTIQUES
        
        **Num_Acc**  
        Numéro d'identifiant de l’accident.
        
        **jour mois**  
        Jour de l'accident.
        
        **Mois**  
        Mois de l'accident.
        
        **an**  
        Année de l'accident.
        
        **hrmn**  
        Heure et minutes de l'accident.
        
        **lum**  
        Lumière : conditions d’éclairage dans lesquelles l'accident s'est produit :
        1 – Plein jour  
        2 – Crépuscule ou aube  
        3 – Nuit sans éclairage public  
        4 – Nuit avec éclairage public non allumé  
        5 – Nuit avec éclairage public allumé
        
        **dep**  
        Département : Code INSEE (Institut National de la Statistique et des Etudes Economiques) du département (2A Corse-du-Sud – 2B Haute-Corse).
        
        **com**  
        Commune : Le numéro de commune est un code donné par l‘INSEE. Le code est composé du code INSEE du département suivi par 3 chiffres.
        
        **agg**  
        Localisation :
        1 – Hors agglomération  
        2 – En agglomération
        
        **int**  
        Intersection :
        1 – Hors intersection  
        2 – Intersection en X  
        3 – Intersection en T  
        4 – Intersection en Y  
        5 – Intersection à plus de 4 branches  
        6 – Giratoire  
        7 – Place  
        8 – Passage à niveau  
        9 – Autre intersection
        
        **atm**  
        Conditions atmosphériques :
        -1 – Non renseigné  
        1 – Normale  
        2 – Pluie légère  
        3 – Pluie forte  
        4 – Neige - grêle  
        5 – Brouillard - fumée  
        6 – Vent fort - tempête  
        7 – Temps éblouissant  
        8 – Temps couvert  
        9 – Autre
        
        **col**  
        Type de collision :
        -1 – Non renseigné  
        1 – Deux véhicules - frontale  
        2 – Deux véhicules – par l’arrière  
        3 – Deux véhicules – par le coté  
        4 – Trois véhicules et plus – en chaîne  
        5 – Trois véhicules et plus - collisions multiples  
        6 – Autre collision  
        7 – Sans collision
        
        **adr**  
        Adresse postale : variable renseignée pour les accidents survenus en agglomération.
        
        **lat**  
        Latitude
        
        **long**  
        Longitude
        """
    )

with tab2:
    st.dataframe(lieux)
    st.write("---")
    st.markdown(
        """
        ### Rubrique LIEUX

    - **Num_Acc**: Identifiant de l’accident identique à celui du fichier "rubrique CARACTERISTIQUES" repris dans l’accident.
    - **catr**: Catégorie de route :
        - 1 – Autoroute
        - 2 – Route nationale
        - 3 – Route Départementale
        - 4 – Voie Communales
        - 5 – Hors réseau public
        - 6 – Parc de stationnement ouvert à la circulation publique
        - 7 – Routes de métropole urbaine
        - 9 – autre
    - **voie**: Numéro de la route.
    - **V1**: Indice numérique du numéro de route (exemple : 2 bis, 3 ter etc.).
    - **V2**: Lettre indice alphanumérique de la route.
    - **circ**: Régime de circulation :
        - -1 – Non renseigné
        - 1 – A sens unique
        - 2 – Bidirectionnelle
        - 3 – A chaussées séparées
        - 4 – Avec voies d’affectation variable
    - **nbv**: Nombre total de voies de circulation.
    - **vosp**: Signale l’existence d’une voie réservée, indépendamment du fait que l’accident ait lieu ou non sur cette voie.
        - -1 – Non renseigné
        - 0 – Sans objet
        - 1 – Piste cyclable
        - 2 – Bande cyclable
        - 3 – Voie réservée
    - **prof**: Profil en long décrit la déclivité de la route à l'endroit de l'accident :
        - -1 – Non renseigné
        - 1 – Plat
        - 2 – Pente
        - 3 – Sommet de côte
        - 4 – Bas de côte
    - **pr**: Numéro du PR de rattachement (numéro de la borne amont). La valeur -1 signifie que le PR n’est pas renseigné.
    - **pr1**: Distance en mètres au PR (par rapport à la borne amont). La valeur -1 signifie que le PR n’est pas renseigné.
    - **plan**: Tracé en plan :
        - -1 – Non renseigné
        - 1 – Partie rectiligne
        - 2 – En courbe à gauche
        - 3 – En courbe à droite
        - 4 – En « S »
    - **lartpc**: Largeur du terre-plein central (TPC) s'il existe (en m).
    - **larrout**: Largeur de la chaussée affectée à la circulation des véhicules ne sont pas compris les bandes d'arrêt d'urgence, les TPC et les places de stationnement (en m).
    - **surf**: Etat de la surface :
        - -1 – Non renseigné
        - 1 – Normale
        - 2 – Mouillée
        - 3 – Flaques
        - 4 – Inondée
        - 5 – Enneigée
        - 6 – Boue
        - 7 – Verglacée
        - 8 – Corps gras – huile
        - 9 – Autre
    - **infra**: Aménagement - Infrastructure :
        - -1 – Non renseigné
        - 0 – Aucun
        - 1 – Souterrain - tunnel
        - 2 – Pont - autopont
        - 3 – Bretelle d’échangeur ou de raccordement
        - 4 – Voie ferrée
        - 5 – Carrefour aménagé
        - 6 – Zone piétonne
        - 7 – Zone de péage
        - 8 – Chantier
        - 9 – Autres
    - **situ**: Situation de l’accident :
        - -1 – Non renseigné
        - 0 – Aucun
        - 1 – Sur chaussée
        - 2 – Sur bande d’arrêt d’urgence
        - 3 – Sur accotement
        - 4 – Sur trottoir
        - 5 – Sur piste cyclable
        - 6 – Sur autre voie spéciale
        - 8 – Autres
    - **vma**: Vitesse maximale autorisée sur le lieu et au moment de l’accident.
    """
    )

with tab3:
    st.dataframe(usagers)
    st.write("---")
    st.markdown(
    """
    ### Rubrique USAGERS

    - **Num_Acc**: Identifiant de l’accident identique à celui du fichier "rubrique CARACTERISTIQUES" repris pour chacun des usagers décrits impliqués dans l’accident.
    - **id_usager**: Identifiant unique de l’usager (y compris les piétons qui sont rattachés aux véhicules qui les ont heurtés) – Code numérique.
    - **id_vehicule**: Identifiant unique du véhicule repris pour chacun des usagers occupant ce véhicule (y compris les piétons qui sont rattachés aux véhicules qui les ont heurtés) – Code numérique.
    - **num_Veh**: Identifiant du véhicule repris pour chacun des usagers occupant ce véhicule (y compris les piétons qui sont rattachés aux véhicules qui les ont heurtés) – Code alphanumérique.
    - **place**: Permet de situer la place occupée dans le véhicule par l'usager au moment de l'accident. Le détail est donné par l’illustration ci-dessous :
        - 10 – Piéton (non applicable)
    - **catu**: Catégorie d'usager :
        - 1 – Conducteur
        - 2 – Passager
        - 3 – Piéton
    - **grav**: Gravité de blessure de l'usager, les usagers accidentés sont classés en trois catégories de victimes plus les indemnes :
        - 1 – Indemne
        - 2 – Tué
        - 3 – Blessé hospitalisé
        - 4 – Blessé léger
    - **sexe**: Sexe de l'usager :
        - 1 – Masculin
        - 2 – Féminin
    - **An_nais**: Année de naissance de l'usager.
    - **trajet**: Motif du déplacement au moment de l’accident :
        - -1 – Non renseigné
        - 0 – Non renseigné
        - 1 – Domicile – travail
        - 2 – Domicile – école
        - 3 – Courses – achats
        - 4 – Utilisation professionnelle
        - 5 – Promenade – loisirs
        - 9 – Autre
    - **secu1**, **secu2**, **secu3**: Le renseignement du caractère indique la présence et l’utilisation de l’équipement de sécurité :
        - -1 – Non renseigné
        - 0 – Aucun équipement
        - 1 – Ceinture
        - 2 – Casque
        - 3 – Dispositif enfants
        - 4 – Gilet réfléchissant
        - 5 – Airbag (2RM/3RM)
        - 6 – Gants (2RM/3RM)
        - 7 – Gants + Airbag (2RM/3RM)
        - 8 – Non déterminable
        - 9 – Autre
    - **locp**: Localisation du piéton :
        - -1 – Non renseigné
        - 0 – Sans objet
        - Sur chaussée :
            - 1 – A + 50 m du passage piéton
            - 2 – A – 50 m du passage piéton
        - Sur passage piéton :
            - 3 – Sans signalisation lumineuse
            - 4 – Avec signalisation lumineuse
        - Divers :
            - 5 – Sur trottoir
            - 6 – Sur accotement
            - 7 – Sur refuge ou BAU
            - 8 – Sur contre allée
            - 9 – Inconnue
    - **actp**: Action du piéton :
        - -1 – Non renseigné
        - Se déplaçant
            - 0 – Non renseigné ou sans objet
            - 1 – Sens véhicule heurtant
            - 2 – Sens inverse du véhicule
        - Divers
            - 3 – Traversant
            - 4 – Masqué
            - 5 – Jouant – courant
            - 6 – Avec animal
            - 9 – Autre
        - A – Monte/descend du véhicule
        - B – Inconnue
    - **etatp**: Cette variable permet de préciser si le piéton accidenté était seul ou non :
        - -1 – Non renseigné
        - 1 – Seul
        - 2 – Accompagné
        - 3 – En groupe
        """

        )
    
with tab4:
    st.dataframe(vehicules)
    st.write("---")
    st.markdown(
     """
    ### Rubrique VÉHICULES

    - **Num_Acc**: Identifiant de l’accident identique à celui du fichier "rubrique CARACTERISTIQUES" repris pour chacun des véhicules décrits impliqués dans l’accident.
    - **id_vehicule**: Identifiant unique du véhicule repris pour chacun des usagers occupant ce véhicule (y compris les piétons qui sont rattachés aux véhicules qui les ont heurtés) – Code numérique.
    - **Num_Veh**: Identifiant du véhicule repris pour chacun des usagers occupant ce véhicule (y compris les piétons qui sont rattachés aux véhicules qui les ont heurtés) – Code alphanumérique.
    - **senc**: Sens de circulation :
        - -1 – Non renseigné
        - 0 – Inconnu
        - 1 – PK ou PR ou numéro d’adresse postale croissant
        - 2 – PK ou PR ou numéro d’adresse postale décroissant
        - 3 – Absence de repère
    - **catv**: Catégorie du véhicule :
        - 00 – Indéterminable
        - 01 – Bicyclette
        - 02 – Cyclomoteur <50cm3
        - 03 – Voiturette (Quadricycle à moteur carrossé) (anciennement "voiturette ou tricycle à moteur")
        - 04 – Référence inutilisée depuis 2006 (scooter immatriculé)
        - 05 – Référence inutilisée depuis 2006 (motocyclette)
        - 06 – Référence inutilisée depuis 2006 (side-car)
        - 07 – VL seul
        - 08 – Référence inutilisée depuis 2006 (VL + caravane)
        - 09 – Référence inutilisée depuis 2006 (VL + remorque)
        - 10 – VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)
        - 11 – Référence inutilisée depuis 2006 (VU (10) + caravane)
        - 12 – Référence inutilisée depuis 2006 (VU (10) + remorque)
        - 13 – PL seul 3,5T <PTCA <= 7,5T
        - 14 – PL seul > 7,5T
        - 15 – PL > 3,5T + remorque
        - 16 – Tracteur routier seul
        - 17 – Tracteur routier + semi-remorque
        - 18 – Référence inutilisée depuis 2006 (transport en commun)
        - 19 – Référence inutilisée depuis 2006 (tramway)
        - 20 – Engin spécial
        - 21 – Tracteur agricole
        - 30 – Scooter < 50 cm3
        - 31 – Motocyclette > 50 cm3 et <= 125 cm3
        - 32 – Scooter > 50 cm3 et <= 125 cm3
        - 33 – Motocyclette > 125 cm3
        - 34 – Scooter > 125 cm3
        - 35 – Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)
        - 36 – Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)
        - 37 – Autobus
        - 38 – Autocar
        - 39 – Train
        - 40 – Tramway
        - 41 – 3RM <= 50 cm3
        - 42 – 3RM > 50 cm3 <= 125 cm3
        - 43 – 3RM > 125 cm3
        - 50 – EDP à moteur
        - 60 – EDP sans moteur
        - 80 – VAE
        - 99 – Autre véhicule
    - **obs**: Obstacle fixe heurté :
        - -1 – Non renseigné
        - 0 – Sans objet
        - 1 – Véhicule en stationnement
        - 2 – Arbre
        - 3 – Glissière métallique
        - 4 – Glissière béton
        - 5 – Autre glissière
        - 6 – Bâtiment, mur, pile de pont
        - 7 – Support de signalisation verticale ou poste d’appel d’urgence
        - 8 – Poteau
        - 9 – Mobilier urbain
        - 10 – Parapet
        - 11 – Ilot, refuge, borne haute
        - 12 – Bordure de trottoir
        - 13 – Fossé, talus, paroi rocheuse
        - 14 – Autre obstacle fixe sur chaussée
        - 15 – Autre obstacle fixe sur trottoir ou accotement
        - 16 – Sortie de chaussée sans obstacle
        - 17 – Buse – tête d’aqueduc
    - **obsm**: Obstacle mobile heurté :
        - -1 – Non renseigné
        - 0 – Aucun
        - 1 – Piéton
        - 2 – Véhicule
        - 4 – Véhicule sur rail
        - 5 – Animal domestique
        - 6 – Animal sauvage
        - 9 – Autre
    - **choc**: Point de choc initial :
        - -1 – Non renseigné
        - 0 – Aucun
        - 1 – Avant
        - 2 – Avant droit
        - 3 – Avant gauche
        - 4 – Arrière
        - 5 – Arrière droit
        - 6 – Arrière gauche
        - 7 – Côté droit
        - 8 – Côté gauche
        - 9 – Chocs multiples (tonneaux)
    - **manv**: Manoeuvre principale avant l’accident :
        - -1 – Non renseigné
        - 0 – Inconnue
        - 1 – Sans changement de direction
        - 2 – Même sens, même file
        - 3 – Entre 2 files
        - 4 – En marche arrière
        - 5 – A contresens
        - 6 – En franchissant le terre-plein central
        - 7 – Dans le couloir bus, dans le même sens
        - 8 – Dans le couloir bus, dans le sens inverse
        - 9 – En s’insérant
        - 10 – En faisant demi-tour sur la chaussée
        - 11 – Changeant de file à gauche
        - 12 – Changeant de file à droite
        - 13 – Déporté vers la gauche
        - 14 – Déporté vers la droite
        - 15 – Tournant à gauche
        - 16 – Tournant à droite
        - 17 – Dépassant vers la gauche
        - 18 – Dépassant vers la droite
        - 19 – Traversant la chaussée
        - 20 – Manoeuvre de stationnement
        - 21 – Manoeuvre d’évitement
        - 22 – Ouverture de porte
        - 23 – Arrêté (hors stationnement)
        - 24 – En stationnement (avec occupants)
        - 25 – Circulant sur trottoir
        - 26 – Autres manoeuvres
    - **motor**: Type de motorisation du véhicule :
        - -1 – Non renseigné
        - 0 – Inconnue
        - 1 – Hydrocarbures
        - 2 – Hybride électrique
        - 3 – Electrique
        - 4 – Hydrogène
        - 5 – Humaine
        - 6 – Autre
    - **occutc**: Nombre d’occupants dans le transport en commun.

     """
    )

