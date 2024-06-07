import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
# Load the dataset
caracteristiques = pd.read_csv("carcteristiques-2022.csv", sep=';')
lieux = pd.read_csv("lieux-2022.csv", sep=';',low_memory=False)
usagers = pd.read_csv("usagers-2022.csv", sep=';')
vehicules = pd.read_csv("vehicules-2022.csv", sep=';')

# Set up the Streamlit app
st.title("Visualisations de l'application")

# Create tabs for different data categories
tab1, tab2, tab3, tab4 = st.tabs(["Caractéristiques", "Lieux", "Usagers", "Véhicules"])

with tab1:
    # Calculer les 10 départements avec le plus d'accidents
    classement_departements_accidentogenes = caracteristiques.groupby('dep')['dep'].count().sort_values(ascending=False).head(10)
    x = classement_departements_accidentogenes.index
    y = classement_departements_accidentogenes.values
    
    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Numéro de département")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Classement des 10 départements les plus accidentogènes")
    
    # Afficher le graphique dans l'application Streamlit
    st.pyplot(fig)

    st.write("---")

    # Calculer les 10 départements avec le moins d'accidents
    classement_departements_peu_accidentogenes = caracteristiques.groupby('dep')['dep'].count().sort_values().head(10)
    x = classement_departements_peu_accidentogenes.index
    y = classement_departements_peu_accidentogenes.values
    
    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Numéro de département")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Classement des 10 départements les moins accidentogènes")
    
    # Afficher le graphique dans l'application Streamlit
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour la luminosité
    lumiere = {
    1: "Plein jour",
    2: "Crépuscule ou aube",
    3: "Nuit sans éclairage public",
    4: "Nuit avec éclairage public non allumé",
    5: "Nuit avec éclairage public allumé"
}

    # Ajouter une colonne 'luminosite' en utilisant la correspondance du dictionnaire
    caracteristiques['luminosite'] = caracteristiques['lum'].map(lumiere)

    # Calculer le nombre d'accidents par type de luminosité
    accident_par_luminosite = caracteristiques.groupby('luminosite')['Accident_Id'].count()
    x = accident_par_luminosite.index
    y = accident_par_luminosite.values

    # Créer un diagramme circulaire avec Matplotlib
    fig, ax = plt.subplots()
    ax.pie(y, labels=x, autopct='%1.1f%%')
    ax.set_title("Nombre d'accidents par type de luminosité")

    # Afficher le diagramme
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour le type de collision
    type_collision = {
    -1: "Non renseigné",
    1: "Frontale",
    2: "Arrière",
    3: "Côté",
    4: "Trois+ Chaîne",
    5: "Trois+ Multiples",
    6: "Autre",
    7: "Sans"
}

    # Ajouter une colonne 'collision' en utilisant la correspondance du dictionnaire
    caracteristiques['collision'] = caracteristiques['col'].map(type_collision)

    # Calculer le nombre d'accidents par type de collision
    accident_par_type_de_collision = caracteristiques.groupby('collision')['Accident_Id'].count().sort_values(ascending=False)
    x = accident_par_type_de_collision.index
    y = accident_par_type_de_collision.values

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Type de collision")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents par type de collision")
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour la localisation
    localisation = {1: "Hors agglomération", 2: "En agglomération"}
    caracteristiques['localisation'] = caracteristiques['agg'].map(localisation)

    # Calculer le nombre d'accidents par localisation
    accident_par_localisation = caracteristiques.groupby('localisation')['Accident_Id'].count()
    x = accident_par_localisation.index
    y = accident_par_localisation.values

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Localisation")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents par localisation")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour le type d'intersection
    intersection = {
    1: "Hors",
    2: "En X",
    3: "En T",
    4: "En Y",
    5: "Plus de 4 branches",
    6: "Giratoire",
    7: "Place",
    8: "Passage à niveau",
    9: "Autre"
    }

    # Ajouter une colonne 'intersection' en utilisant la correspondance du dictionnaire
    caracteristiques['intersection'] = caracteristiques['int'].map(intersection)

    # Calculer le nombre d'accidents par type d'intersection
    accident_par_intersection = caracteristiques.groupby('intersection')['Accident_Id'].count().sort_values(ascending=False)
    x = accident_par_intersection.index
    y = accident_par_intersection.values

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Type d'intersection")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents par type d'intersection")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Remplacer les virgules par des points dans les colonnes 'lat' et 'long'
    caracteristiques['lat'] = caracteristiques['lat'].str.replace(',', '.')
    caracteristiques['long'] = caracteristiques['long'].str.replace(',', '.')

    # Convertir les colonnes 'lat' et 'long' en numérique
    caracteristiques['lat'] = pd.to_numeric(caracteristiques['lat'], errors='coerce')
    caracteristiques['long'] = pd.to_numeric(caracteristiques['long'], errors='coerce')

    # Demander à l'utilisateur de choisir un département
    departement = st.text_input("Choisissez un département", value='59')

    # Filtrer les données pour le département choisi
    departement_data = caracteristiques[caracteristiques['dep'] == departement]

    # Vérifier si des données sont disponibles pour le département choisi
    if not departement_data.empty:
        # Créer la carte avec Plotly Express
        fig = px.scatter_mapbox(departement_data, lat="lat", lon="long", hover_name="dep",
                                hover_data=['Accident_Id'], color_discrete_sequence=["fuchsia"],
                                zoom=5, height=300, mapbox_style="open-street-map", title="Zones les plus accidentogènes par département")
        
        # Afficher la carte dans Streamlit
        st.plotly_chart(fig)
    else:
        st.write("Aucune donnée disponible pour ce département.")

    st.write("---")

    # Définir le dictionnaire de correspondance pour le libellé du mois
    libelle_mois = {
    1: "janvier",
    2: "février",
    3: "mars",
    4: "avril",
    5: "mai",
    6: "juin",
    7: "juillet",
    8: "août",
    9: "septembre",
    10: "octobre",
    11: "novembre",
    12: "décembre"
    }

    # Ajouter une colonne 'libellé_mois' en utilisant la correspondance du dictionnaire
    caracteristiques['libelle_mois'] = caracteristiques['mois'].map(libelle_mois)

    # Calculer le nombre d'accidents par mois
    accidents_par_mois = caracteristiques.groupby('libelle_mois')['Accident_Id'].count()

    # Réorganiser les données pour suivre l'ordre des mois
    ordre_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    accidents_par_mois = accidents_par_mois.reindex(ordre_mois)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_par_mois.index, accidents_par_mois.values)
    ax.set_xlabel("Mois")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents en fonction du mois")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Convertir la colonne 'hrmn' en datetime et extraire l'heure
    caracteristiques['heure'] = pd.to_datetime(caracteristiques['hrmn'], format='%H:%M').dt.hour

    # Créer un histogramme avec Matplotlib
    fig, ax = plt.subplots()
    ax.hist(caracteristiques['heure'], bins=24, edgecolor='black')
    ax.set_xlabel("Heure")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents en fonction de l'heure")
    ax.set_xlim(0, 23)  # Limiter l'axe x de 0 à 23 pour les heures de la journée

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

with tab2:
    # Définir le dictionnaire de correspondance pour le type de route
    route = {
    1: "Autoroute",
    2: "Route nationale",
    3: "Route Départementale",
    4: "Voie Communales",
    5: "Hors réseau public",
    6: "Stationnement publique",
    7: "Routes de métropole urbaine",
    9: "Autre"
    }

    # Ajouter une colonne 'type_route' en utilisant la correspondance du dictionnaire
    lieux['type_route'] = lieux['catr'].map(route)

    # Calculer le nombre d'accidents par type de route
    accidents_par_type_route = lieux.groupby('type_route')['Num_Acc'].count().sort_values(ascending=False)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_par_type_route.index, accidents_par_type_route.values)
    ax.set_xlabel("Type de route")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents par type de route")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour la déclivité
    declivite = {
        -1: "Non renseigné",
        1: "Plat",
        2: "Pente",
        3: "Sommet de côte",
        4: "Bas de côte"
    }

    # Ajouter une colonne 'declivite' en utilisant la correspondance du dictionnaire
    lieux['declivite'] = lieux['catr'].map(declivite)

    # Calculer le nombre d'accidents par déclivité
    accidents_par_declivite = lieux.groupby('declivite')['Num_Acc'].count().sort_values(ascending=False)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_par_declivite.index, accidents_par_declivite.values)
    ax.set_xlabel("Déclivité")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents en fonction de la déclivité")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour le type de circulation
    circulation = {
        -1: 'Non renseigné',
        1: 'A sens unique',
        2: 'Bidirectionnelle',
        3: 'A chaussées séparées',
        4: 'Avec voies d’affectation variable'
    }

    # Ajouter une colonne 'circulation' en utilisant la correspondance du dictionnaire
    lieux['circulation'] = lieux['circ'].map(circulation)

    # Calculer le nombre d'accidents par type de circulation
    accidents_par_circulation = lieux.groupby('circulation')['Num_Acc'].count().sort_values(ascending=False)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_par_circulation.index, accidents_par_circulation.values)
    ax.set_xlabel("Type de circulation")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents en fonction du type de circulation")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour le type de surface
    surface = {
    -1: 'Non renseigné',
    1: 'Normale',
    2: 'Mouillée',
    3: 'Flaques',
    4: 'Inondée',
    5: 'Enneigée',
    6: 'Boue',
    7: 'Verglacée',
    8: 'Corps gras – huile',
    9: 'Autre'
    }

    # Ajouter une colonne 'surface' en utilisant la correspondance du dictionnaire
    lieux['surface'] = lieux['surf'].map(surface)

    # Calculer le nombre d'accidents par type de surface
    accidents_par_surface = lieux.groupby('surface')['Num_Acc'].count().sort_values(ascending=False)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_par_surface.index, accidents_par_surface.values)
    ax.set_xlabel("Type de surface")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents en fonction de la surface")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour le type d'infrastructure
    infrastructure = {
    -1: 'Non renseigné',
    0: 'Aucun',
    1: 'Souterrain - tunnel',
    2: 'Pont - autopont',
    3: 'Echangeur',
    4: 'Voie ferrée',
    5: 'Carrefour aménagé',
    6: 'Zone piétonne',
    7: 'Zone de péage',
    8: 'Chantier',
    9: 'Autres'
    }

    # Ajouter une colonne 'infrastructure' en utilisant la correspondance du dictionnaire
    lieux['infrastructure'] = lieux['infra'].map(infrastructure)

    # Calculer le nombre d'accidents par type d'infrastructure
    accidents_par_infrastructure = lieux.groupby('infrastructure')['Num_Acc'].count().sort_values(ascending=False)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_par_infrastructure.index, accidents_par_infrastructure.values)
    ax.set_xlabel("Type d'infrastructure")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents par type d'infrastructure")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir le dictionnaire de correspondance pour la situation
    situation = {
        -1: 'Non renseigné',
        0: 'Aucun',
        1: 'chaussée',
        2: 'bande d’arrêt d’urgence',
        3: 'accotement',
        4: 'trottoir',
        5: 'piste cyclable',
        6: 'autre voie spéciale',
        8: 'Autres'
    }

    # Ajouter une colonne 'situation' en utilisant la correspondance du dictionnaire
    lieux['situation'] = lieux['situ'].map(situation)

    # Calculer le nombre d'accidents par situation
    accidents_par_situation = lieux.groupby('situation')['Num_Acc'].count().sort_values(ascending=False)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_par_situation.index, accidents_par_situation.values)
    ax.set_xlabel("Situation")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents en fonction de la situation")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Calculer le nombre d'accidents par vitesse maximale autorisée (vma)
    accidents_va = lieux.groupby('vma')['Num_Acc'].count().sort_values(ascending=False)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(accidents_va.index, accidents_va.values)
    ax.set_xlabel("Vitesse maximale autorisée")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents en fonction de la vitesse maximale autorisée")
    ax.set_xlim(0, 140)  # Limiter l'axe x de 0 à 140 km/h

    # Afficher le graphique
    st.pyplot(fig)

with tab3:

        # Définir les dictionnaires de correspondance
    categorie_usager = {1: 'Conducteur', 2: 'Passager', 3: 'Piéton'}
    gravite = {1: 'Indemne', 2: 'Tué', 3: 'Blessé hospitalisé', 4: 'Blessé léger'}

    # Ajouter des colonnes pour la catégorie d'usager et la gravité des blessures en utilisant les dictionnaires de correspondance
    usagers['categorie_usager'] = usagers['catu'].map(categorie_usager)
    usagers['gravite'] = usagers['grav'].map(gravite)

    # Calculer le nombre d'accidents par catégorie d'usager et gravité des blessures
    gravite_par_type_usager = usagers.groupby(['categorie_usager', 'gravite']).size().reset_index(name='count')

    # Préparer les données pour le graphique Matplotlib
    pivot_table = gravite_par_type_usager.pivot_table(index='categorie_usager', columns='gravite', values='count', fill_value=0)

    # Créer un graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    pivot_table.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel("Catégorie d'usager")
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Répartition de la gravité des blessures par catégorie d'usager")

    # Légende
    plt.legend(title="Gravité des blessures")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    sexe = {1:'Masculin',2:'Féminin'}
    usagers['sex']=usagers['sexe'].map(sexe)
    gravité = {1:'Indemne',2:'Tué',3:'Blessé hospitalisé',4:'Blessé léger'}
    usagers['gravité']=usagers['grav'].map(gravité)
    data = usagers.groupby(['sex', 'gravité']).size().reset_index(name='count')
    data['sex_gravité'] = data['sex'] + ' - ' + data['gravité']
    fig = px.pie(data, names='sex_gravité', values='count', 
                labels={'sex_gravité': 'Sexe et Gravité', 'count': 'Nombre d\'accidents'},
                title='Répartition des accidents par sexe et par gravité des blessures')
    st.plotly_chart(fig)

    st.write("---")

    # Calculer l'âge des usagers
    usagers['age'] = 2022 - usagers['an_nais']

    # Créer un histogramme avec Matplotlib
    fig, ax = plt.subplots()

    # Diviser les données par gravité des blessures
    for gravite, data in usagers.groupby('gravité'):
        ax.hist(data['age'], bins=30, alpha=0.5, label=gravite)

    # Définir les étiquettes et le titre
    ax.set_xlabel('Âge')
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title('Distribution des âges des usagers en fonction de la gravité des blessures')

    # Définir les intervalles d'âge sur l'axe des x
    age_intervals = [0, 18, 40, 60, 80, 100]
    ax.set_xticks(age_intervals)
    ax.set_xticklabels(['0-18', '18-40', '40-60', '60-80', '80-100','100 +'], rotation=45)

    # Afficher la légende
    ax.legend()

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir les dictionnaires de correspondance
    motif_deplacement = {-1: 'Non renseigné', 0: 'Non renseigné', 1: 'Domicile – travail', 2: 'Domicile – école',
                        3: 'Courses – achats', 4: 'Utilisation professionnelle', 5: 'Promenade – loisirs', 9: 'Autre'}

    # Ajouter une colonne 'motif_déplacement' en utilisant la correspondance du dictionnaire
    usagers['motif_déplacement'] = usagers['trajet'].map(motif_deplacement)

    # Créer un histogramme avec Matplotlib
    fig, ax = plt.subplots()

    # Diviser les données par gravité des blessures
    for gravite, data in usagers.groupby('gravité'):
        ax.hist(data['motif_déplacement'], bins=len(motif_deplacement.keys())-2, alpha=0.5, label=gravite, align='mid')

    # Définir les étiquettes et le titre
    ax.set_xlabel('Motif de déplacement')
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title('Répartition des usagers selon le motif de déplacement et la gravité des blessures')

    # Faire pivoter les étiquettes de l'axe x pour éviter le chevauchement
    plt.xticks(rotation=45, ha='right')

    # Afficher la légende
    ax.legend()

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    # Définir les dictionnaires de correspondance
    motif_deplacement = {-1: 'Non renseigné', 0: 'Non renseigné', 1: 'Domicile – travail', 2: 'Domicile – école',
                        3: 'Courses – achats', 4: 'Utilisation professionnelle', 5: 'Promenade – loisirs', 9: 'Autre'}
    usagers['motif_déplacement'] = usagers['trajet'].map(motif_deplacement)

    # Compter le nombre d'occurrences de chaque motif de déplacement
    count_motif_deplacement = usagers['motif_déplacement'].value_counts()

    # Créer le graphique en diagramme circulaire avec Matplotlib
    fig, ax = plt.subplots()
    ax.pie(count_motif_deplacement, labels=count_motif_deplacement.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Répartition des usagers selon le motif de déplacement')

    # Afficher le graphique
    st.pyplot(fig)

with tab4:

    # Définir les dictionnaires de correspondance
    categories_vehicules = {
        1: 'Bicyclette',
        2: 'Cyclomoteur <50cm3',
        3: 'Voiturette',
        4: 'Scooter immatriculé',
        5: 'Motocyclette',
        6: 'Side-car',
        7: 'VL seul',
        8: 'VL + caravane',
        9: 'VL + remorque',
        10: 'VU seul 1,5T <= PTAC <= 3,5T',
    }

    # Ajouter une colonne 'categorie_vehicule' en utilisant la correspondance du dictionnaire
    vehicules['categorie_vehicule'] = vehicules['catv'].map(categories_vehicules)

    # Calculer le nombre d'accidents par catégorie de véhicule
    accident_par_type_vehicule = vehicules['categorie_vehicule'].value_counts().sort_values(ascending=False)

    # Créer le graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    accident_par_type_vehicule.plot(kind='bar', ax=ax)
    ax.set_xlabel('Type de véhicule')
    ax.set_ylabel("Nombre d'accidents")
    ax.set_title("Nombre d'accidents par catégorie de véhicule")

    # Rotation de l'axe x
    plt.xticks(rotation=45)

    # Afficher le graphique
    st.pyplot(fig)

    st.write("---")

    choc_libelle = {-1:'Non renseigné',0:'Aucun',1:'Avant',2:'Avant droit',3:'Avant gauche',4:'Arrière',5:'Arrière droit',
                6:'Arrière gauche',7:'Côté droit',8:'Côté gauche',9:'Chocs multiples (tonneaux)'}
    vehicules['choc_libelle']=vehicules['choc'].map(choc_libelle)
    points = pd.DataFrame(vehicules.groupby(['choc_libelle', "categorie_vehicule"])['id_vehicule'].count()).reset_index()
    fig = px.bar(points, x='choc_libelle', y='id_vehicule', color='categorie_vehicule', 
             title="Répartition des points de choc initial par catégorie de véhicule",
             labels={'choc_libelle': 'Point de choc initial', 'id_vehicule': "Nombre d'accidents"},
             category_orders={'choc_libelle': ['Avant', 'Avant droit', 'Avant gauche', 'Arrière', 
                                        'Arrière droit', 'Arrière gauche', 'Côté droit', 'Côté gauche', 
                                        'Chocs multiples (tonneaux)']})
    st.plotly_chart(fig)

    st.write("---")

    motorisation = {-1:'Non renseigné',0:'Inconnue',1:'Hydrocarbures',2:'Hybride électrique',3:'Electrique',4:'Hydrogène',
                5:'Humaine',6:'Autre'}
    vehicules['motorisation']=vehicules['motor'].map(motorisation)

    repartition_motorisation = vehicules.groupby('motorisation')['id_vehicule'].count()

    fig=px.pie(repartition_motorisation, 
                names=repartition_motorisation.index, 
                values=repartition_motorisation.values,
                title="Répartition des types de motorisation des véhicules impliqués dans les accidents")
    st.plotly_chart(fig)
    



