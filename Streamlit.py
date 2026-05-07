
#   CONFIGURATION DE LA PAGE  
st.set_page_config(page_title="AI Skills for Manufacturing", layout="wide", page_icon="Logo2.png")

#   STYLE PERSONNALISÉ  
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    /* 3. Effet de survol du bouton */
    div.stButton > button:hover {
        background-color: #0056b3 !important;
        transform: scale(1.02) !important;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15) !important;
    }
            </style>
    """, unsafe_allow_html=True)
# 1. INITIALISATION (À mettre tout en haut, avant la sidebar)
if 'page' not in st.session_state:
    st.session_state.page = "Accueil"

# On initialise aussi les clés des widgets pour éviter qu'ils soient vides au départ
if 'a' not in st.session_state:
    st.session_state.a = "Accueil"
if 'b' not in st.session_state:
    st.session_state.b = " "
if 'c' not in st.session_state:
    st.session_state.c = " "
if 'd' not in st.session_state:
    st.session_state.d = " "

# 2. Fonction de nettoyage
def reset_others(current_key):
    keys = ["a", "b", "c", "d"]
    for key in keys:
        if key != current_key:
            st.session_state[key] = " "
    
    if st.session_state[current_key] != " ":
        st.session_state.page = st.session_state[current_key]
#   SIDEBAR  
st.sidebar.markdown("### AI SKILLS")
st.sidebar.markdown("### Menu Principal")

# SECTION A
st.sidebar.write("**Général**")
st.sidebar.selectbox(
    "A", [" ", "Accueil", "Questionnaire"], 
    key="a", 
    on_change=reset_others, 
    args=("a",), # Passage de la clé à la fonction
    label_visibility="collapsed"
)

# SECTION B
st.sidebar.write("**Observation**")
st.sidebar.selectbox(
    "B", [" ", "Analyse défaut image", "- Fiche : Analyse défaut image", "DBSCAN", "- Fiche : DBSCAN"], 
    key="b", 
    on_change=reset_others, 
    args=("b",),
    label_visibility="collapsed"
)

# SECTION C
st.sidebar.write("**Classification**")
st.sidebar.selectbox(
    "C", [" ", "K-means", "- Fiche : K-means", "SVM", "- Fiche : SVM"], 
    key="c", 
    on_change=reset_others, 
    args=("c",),
    label_visibility="collapsed"
)

# SECTION D
st.sidebar.write("**Prédiction**")
st.sidebar.selectbox(
    "D", [" ", " Méthode KNN", "- Fiche méthode KNN", "Régression linéaire", "- Fiche régression linéaire", "Régression logistique", "- Fiche régression logistique"], 
    key="d", 
    on_change=reset_others, 
    args=("d",),
    label_visibility="collapsed"
)

# On récupère la page active finale
skill_choice = st.session_state.page

# ==========================================
# SECTION A1 : ACCUEIL
# ==========================================
if skill_choice == "Accueil":
    # Titre principal centré
    st.markdown("<h1 style='text-align: center;'>Bienvenue sur AI Skills</h1>", unsafe_allow_html=True)

    with st.container():
        #   NOTRE PROJET  
        st.markdown("""
            <h3 style="margin-left: 20px;">Notre Projet :</h3>""", unsafe_allow_html=True)
        st.markdown("""
        **IA Skills for Manufacturing** est un projet étudiant visant à rendre l’apprentissage automatisé
        accessible aux ouvriers, techniciens et opérateurs industriels. L’idée est de 
        permettre à n’importe qui de pouvoir utiliser des modèles d’apprentissage automatisé plus ou moins 
        complexe **sans jamais écrire une seule ligne de code**.
        """)

        st.write("") # Petit espace

        st.markdown("""
            <h3 style="margin-left: 20px;">AI Skills c'est :</h3>""", unsafe_allow_html=True)
        
        # Utilisation de symboles pour reproduire les flèches de l'image
        st.markdown("""
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Boîte à outil interactive de techniques d’apprentissage automatisé  
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Façonnée pour l’industrie  
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Facile à utiliser, simple, intuitif  
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Portée éducative
        """)

        st.write("") # Petit espace

        st.markdown("""
    <div style='text-align: center;'>
        <em>Les détails du fonctionnement de chaque méthode d'apprentissage automatisé sont disponibles en haut de chaque 
        interface, et les méthodes sont directement utilisables depuis l’interface.</em>
    </div>
    """, unsafe_allow_html=True) 
        
        st.write("") # Petit espace

        st.warning("""
        **Note sur la terminologie :** Dans ce projet, nous privilégions le terme **Apprentissage Automatisé** (Machine Learning) plutôt qu'Intelligence Artificielle.  
    
        *Pourquoi ?* Contrairement à l'idée d'une machine "pensante" (ChatGPT), nos outils reposent sur des modèles mathématiques qui apprennent à reconnaître des motifs (patterns) à partir de vos données pour automatiser des décisions dans le domaine de l'industrie.
        """)
        
        st.write("") # Petit espace
    
        # Sous-titre centré
        st.markdown("<h3 style='text-align: center;'>Notre Equipe</h3>", unsafe_allow_html=True)

            #   AFFICHAGE DE L'IMAGE "Image.png" CENTRÉE  
        col_img1, col_img2, col_img3 = st.columns([1, 2, 1]) 
        with col_img2:
            # On charge l'image locale. use_container_width l'adapte à la colonne.
            st.image("Image.jpeg", caption="Equipe ayant réalisé le projet", use_container_width=True)

        
        st.subheader("Membres de l'équipe")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write("CLAUDEL Bastien")
        st.write("Développeur")
        st.image("CV1.jpg", use_container_width=True)
        with open("CV1.pdf", "rb") as file:
            btn = st.download_button(
                label="Télécharger CV pdf",
                data=file,
                file_name="CV_Bastien_Claudel.pdf",
                mime="image/pdf",
                use_container_width=True
        )

    with col2:
        st.write("LABORDE Julien")
        st.write("Développeur")
        st.image("CV2.jpg", use_container_width=True)
        with open("CV2.pdf", "rb") as file:
            btn = st.download_button(
                label="Télécharger CV pdf",
                data=file,
                file_name="CV_Julien_Laborde.pdf",
                mime="image/pdf",
                use_container_width=True
        )
    with col3:
        st.write("TRAMAUX Noah")
        st.write("Développeur")
        st.image("CV3.jpg", use_container_width=True)
        with open("CV3.pdf", "rb") as file:
            btn = st.download_button(
                label="Télécharger CV pdf",
                data=file,
                file_name="CV_Noah_Tramaux.pdf",
                mime="image/pdf",
                use_container_width=True
            )
    with col4:
        st.write("BREL Thibault")
        st.write("Développeur")
        st.image("CV4.jpg", use_container_width=True)
        with open("CV4.pdf", "rb") as file:
            btn = st.download_button(
                label="Télécharger CV pdf",
                data=file,
                file_name="CV_Thibault_Brel.pdf",
                mime="image/pdf",
                use_container_width=True
            )
    with col5:
        st.write("CHEVRIER Héloïse")
        st.write("Développeuse")
        st.image("CV5.jpg", use_container_width=True)
        with open("CV5.pdf", "rb") as file:
            btn = st.download_button(
                label="Télécharger CV pdf",
                data=file,
                file_name="CV_Héloïse_Chevrier.pdf",
                mime="image/pdf",
                use_container_width=True
            )

    with col6:
        st.write("Manohisoa RAZDA")
        st.write("Développeur")
        st.image("CV6.jpg", use_container_width=True)
        with open("CV1.pdf", "rb") as file:
            btn = st.download_button(
                label="Télécharger CV pdf",
                data=file,
                file_name="CV_Manohisoa_RAZAFINDRAKOTO.pdf",
                mime="image/pdf",
                use_container_width=True
        )
    
    st.markdown(" ") # Une ligne de séparation pour faire propre
    # On crée des colonnes pour centrer ou décaler le bouton à droite
    def aller_au_questionnaire():
        st.session_state.page = "Questionnaire"
        st.session_state.a = "Questionnaire"
        st.session_state.b = " "
        st.session_state.c = " "
        st.session_state.d = " "
    st.button("**Commencer à traiter mes données**", on_click=aller_au_questionnaire, use_container_width=True)
    
# ==========================================
# SECTION A2 : QUESTIONNAIRE
# ==========================================

elif skill_choice == "Questionnaire":
    st.markdown("<h1 style='text-align: center;'>Quelle technique d'apprentissage automatique choisir ?</h1>", unsafe_allow_html=True)

    st.write("") # Petit espace
    st.markdown(""" Quelles techniques d'apprentissages automatiques ai-je à ma disposition ?""")
    st.markdown("""
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Notre site propose 3 catégories de techniques: 
        """)

    #Observation
    st.markdown("""
        <h5 style="margin-left: 20px;">➤&nbsp; Observation :</h5>""", unsafe_allow_html=True)
    st.markdown("""
    Dans l'industrie, elle est principalement utilisée pour le contrôle qualité visuel. 
    L'algorithme apprend à connaître l'aspect d'une pièce "parfaite" (conforme) et alerte 
    immédiatement dès qu'il repère une irrégularité : une rayure, une fissure, un manque 
    de matière ou une erreur d'assemblage. C'est une méthode précieuse car elle permet de 
    surveiller une production en temps réel sans avoir besoin de répertorier à l'avance 
    tous les types de défauts possibles.
    """)

    #Classification
    st.markdown("""
        <h5 style="margin-left: 20px;">➤&nbsp; Classification :</h5>""", unsafe_allow_html=True)
    st.markdown("""
    La classification consiste à apprendre à l'ordinateur à ranger des objets ou des 
                situations dans des "boîtes" ou catégories prédéfinies. Sur une ligne de production, 
                cela permet par exemple de trier automatiquement des pièces selon leur modèle, leur 
                matériau (acier, aluminium, plastique) ou leur niveau de finition. Contrairement à 
                l'observation qui cherche l'anormal, la classification identifie précisément ce qu'est 
                l'objet en le comparant à une base de données d'exemples déjà connus et étiquetés 
                par les techniciens.
    """)

    #La Prédiction
    st.markdown("""
        <h5 style="margin-left: 20px;">➤&nbsp; Prédiction :</h5>""", unsafe_allow_html=True)
    st.markdown("""
    La prédiction (souvent appelée régression en mathématiques) ne cherche pas à trier,
    mais à calculer une valeur chiffrée précise pour le futur. En analysant 
    l'historique des capteurs (température, pression, vibrations), la méthode est capable 
    d'estimer combien de temps une machine peut encore fonctionner avant la prochaine 
    panne ou de prédire la consommation d'énergie nécessaire pour une tâche donnée. 
    C'est l'outil idéal pour la maintenance préventive : on n'attend pas que la machine casse, 
    on prévoit le moment exact où elle aura besoin d'une révision.
    """)

    st.warning("""**Attention** : Les modèles mis à disposition ne traitent que les fichiers .csv, .txt et les images .png, .jpg, .jpeg""")

    st.markdown("<h1 style='text-align: center;'>Questionnaire :</h1>", unsafe_allow_html=True)
    st.info("Veuillez répondre aux questions ci-dessous pour déterminer la méthode adaptée à votre problème.")

    # --- ÉTAPE 1 : FORMAT ---
    st.markdown("### 1. Quel est le format de vos données ?")
    format_data = st.radio(
        "Sélectionnez le type de support :",
        ["Des images (photos de pièces, captures caméra)", 
         "Un tableau de données (chiffres, texte, fichier CSV)"],
        index=None, key="q1"
    )

    if format_data:
        if "images" in format_data:
            # --- LOGIQUE IMAGES ---
            st.markdown("---")
            st.markdown("### 2. Possédez-vous une base de données d'images ?")
            possede_base = st.radio("Sélectionnez votre réponse :", ["Oui", "Non"], index=None, key="q_img")

            if possede_base == "Oui":
                st.success("**Recommandation : Analyse défaut image (Isolation Forest)**")
                def aller_B1():
                    st.session_state.page = "Analyse défaut image"
                    st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.d = " ", "Analyse défaut image", " ", " "
                st.button("**Utiliser Analyse défaut image**", on_click=aller_B1, key="btn_iso_img", use_container_width=True)
            elif possede_base == "Non":
                st.warning("Vous devez d'abord constituer un échantillon d'images.")
                st.link_button("Chercher sur Kaggle", "https://www.kaggle.com/")

        else:
            # --- LOGIQUE TABLEAU (CSV/TXT) ---
            st.markdown("---")
            st.markdown("### 2. Quel est l'objectif principal ?")
            but = st.radio(
                "Choisissez votre objectif :",
                ["Grouper mes données automatiquement (sans étiquettes)", 
                 "Classer mes données selon des catégories connues",
                 "Prédire une valeur numérique (estimation)"],
                index=None, key="q2"
            )

            if but:
                st.markdown("---")
    
                # --- CAS CLUSTERING ---
                if "Grouper" in but:
                    choix_cluster = st.radio("Connaissez-vous le nombre de groupes à l'avance ?", ["Oui", "Non"], index=None, key="q_clust")
                    if choix_cluster == "Oui":
                        st.success("**Recommandation : K-means**")
                        def aller_C1():
                            st.session_state.page = "K-means"
                            st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.d = " ", " ", "K-means", " "
                        st.button("**Utiliser K-means**", on_click=aller_C1, key="btn_km", use_container_width=True)
                    elif choix_cluster == "Non":
                        st.success("**Recommandation : DBSCAN**")
                        def aller_B3():
                            st.session_state.page = "DBSCAN"
                            st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.d = " ", "DBSCAN", " ", " "
                        st.button("**Utiliser DBSCAN**", on_click=aller_B3, key="btn_db", use_container_width=True)

                # --- CAS CLASSIFICATION (Ajout du SVM ici) ---
                elif "Classer" in but:
                    st.success("**Recommandation : Plusieurs outils sont adaptés à la classification**")
                    st.write("Choisissez la méthode selon la complexité de vos données :")
                    
                    col_c1, col_c2, col_c3 = st.columns(3)
                    
                    with col_c1:
                        st.info("**Voisinage**")
                        def aller_D1():
                            st.session_state.page = " Méthode KNN"
                            st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.d = " ", " ", " ", " Méthode KNN"
                        st.button("**Utiliser KNN**", on_click=aller_D1, key="btn_knn", use_container_width=True)
                            
                    with col_c2:
                        st.info("**Binaire (Oui/Non)**")
                        def aller_D5():
                            st.session_state.page = "Régression logistique"
                            st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.d = " ", " ", " ", "Régression logistique"
                        st.button("**Logistique**", on_click=aller_D5, key="btn_log", use_container_width=True)

                    with col_c3:
                        st.info("**Classification non binaire**")
                        def aller_C3():
                            st.session_state.page = "SVM"
                            st.session_state.a = " "
                            st.session_state.b = " "
                            st.session_state.c = " "
                            st.session_state.d = "SVM"
                        st.button("**Utiliser SVM**", on_click=aller_C3, key="btn_svm", use_container_width=True)

                # --- CAS PRÉDICTION ---
                elif "Prédire" in but:
                    st.success("**Recommandation : Régression Linéaire**")
                    def aller_D3():
                        st.session_state.page = "Régression linéaire"
                        st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.d = " ", " ", " ", "Régression linéaire"
                    st.button("**Utiliser la régression linéaire**", on_click=aller_D3, key="btn_lin", use_container_width=True)

# ==========================================
# SECTION B1 : ISOLATION FOREST (Analyse défaut image)
# ==========================================
#Fiche associée:
elif skill_choice == "- Fiche : Analyse défaut image":
    st.markdown("<h1 style='text-align: center;'>Analyse défaut image</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>ISOLATION FOREST</h5>", unsafe_allow_html=True)
    st.image("Fiche_B1.jpg", caption="Fiche explicative : Analyse défaut image", use_container_width=True)
    def aller_B1():
            st.session_state.page = "Analyse défaut image"
            st.session_state.a = " "
            st.session_state.b = "Analyse défaut image"
            st.session_state.c = " "
            st.session_state.d = " "
    st.button("**Utiliser cette technique**", on_click=aller_B1, use_container_width=True)
    
elif skill_choice == "Analyse défaut image":
    st.markdown("<h1 style='text-align: center;'>Analyse défaut image</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>ISOLATION FOREST</h5>", unsafe_allow_html=True)
    def aller_fiche_B1():
            st.session_state.page = "- Fiche : Analyse défaut image"
            st.session_state.a = " "
            st.session_state.b = "- Fiche : Analyse défaut image"
            st.session_state.c = " "
            st.session_state.d = " "
    st.button("**Comment fonctionne cette technique ?**", on_click=aller_fiche_B1, use_container_width=True)
    RESOLUTION = 160
    with st.expander("Hyperparamètres"):
        contamination = st.slider("Seuil de sensibilité (Contamination)", 0.01, 0.20, 0.10)
        st.info(f"Résolution d'analyse fixée à {RESOLUTION}x{RESOLUTION} pour garantir la stabilité.")

    train_files = st.file_uploader("1. Charger les images BONNES pour l'entraînement",
                                   type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("2. Entraîner le modèle"):
        if not train_files:
            st.error("Veuillez d'abord uploader des images d'entraînement.")
        else:
            with st.spinner("Entraînement en cours..."):
                features = []
                for file in train_files:
                    # Utilisation de la résolution fixe
                    img = Image.open(file).convert('L').resize((RESOLUTION, RESOLUTION))
                    fd = hog(np.array(img), orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
                    features.append(fd)

                model = IsolationForest(contamination=contamination, random_state=42)
                model.fit(np.array(features))
                
                # On stocke le modèle dans le session_state
                st.session_state['model'] = model
                st.success("Modèle entraîné avec succès !")

    test_files = st.file_uploader("3. Charger les images à tester",
                                  type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if st.button("4. Lancer l'analyse"):
        if 'model' not in st.session_state:
            st.error("Le modèle n'est pas encore entraîné. Veuillez faire l'étape 2.")
        elif not test_files:
            st.error("Veuillez d'abord uploader des images à tester.")
        else:
            cols = st.columns(4)
            for idx, file in enumerate(test_files):
                # Utilisation de la même résolution fixe pour le test
                img = Image.open(file).convert('L').resize((RESOLUTION, RESOLUTION))
                fd = hog(np.array(img), orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
                
                # Prédiction
                score = st.session_state['model'].decision_function([fd])[0]
                prediction = st.session_state['model'].predict([fd])[0]

                with cols[idx % 4]:
                    st.image(img, use_container_width=True)
                    if prediction == -1:
                        st.error(f"DÉFAUT (Score: {score:.2f})")
                    else:
                        st.success(f"OK (Score: {score:.2f})")
                        
# ==========================================
# SECTION B3 :  DBSCAN
# ==========================================
#Fiche associée:
elif skill_choice == "- Fiche : DBSCAN":
    st.markdown("<h1 style='text-align: center;'>DBSCAN</h1>", unsafe_allow_html=True)
    st.image("Fiche_B3.png", caption="Fiche explicative : DBSCAN", use_container_width=True)
    def aller_B3():
            st.session_state.page = "DBSCAN"
            st.session_state.a = " "
            st.session_state.b = "DBSCAN"
            st.session_state.c = " "
            st.session_state.d = " "
    st.button("**Utiliser cette technique**", on_click=aller_B3, use_container_width=True)
    
elif skill_choice == "DBSCAN": 
    st.markdown("<h1 style='text-align: center;'>DBSCAN</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Density-Based Spatial Clustering of Applications with Noise</h5>", unsafe_allow_html=True)

    def aller_fiche_B3():
            st.session_state.page = "- Fiche : DBSCAN"
            st.session_state.a = " "
            st.session_state.b = "- Fiche : DBSCAN"
            st.session_state.c = " "
            st.session_state.d = " "
    st.button("**Comment fonctionne cette technique ?**", on_click=aller_fiche_B3, use_container_width=True)
    
    st.write("""
    L'algorithme **DBSCAN** regroupe les points situés dans des zones denses. 
    Les points isolés sont automatiquement marqués comme **'Bruit' (-1)**
    """)

    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import StandardScaler

    # --- 1. CHARGEMENT DU FICHIER ---
    uploaded_file_db = st.file_uploader("Charger un CSV pour l'analyse de densité", type="csv", key="dbscan_upload")

    if uploaded_file_db is not None:
        df_db = pd.read_csv(uploaded_file_db)
        
        # Sélection des colonnes numériques
        cols_num = df_db.select_dtypes(include=[np.number]).columns.tolist()

        if len(cols_num) < 2:
            st.error("Besoin d'au moins 2 colonnes numériques.")
        else:
            col1, col2 = st.columns([1, 2])

            with col1:
                st.subheader("Hyperparamètres")
                sel_x = st.selectbox("Axe X", cols_num, index=0, key="dbx")
                sel_y = st.selectbox("Axe Y", cols_num, index=1, key="dby")
                
                st.markdown("---")
                # Paramètres spécifiques à DBSCAN
                eps = st.slider("Distance de voisinage (eps)", 0.1, 2.0, 0.3, help="Distance max entre deux points pour être voisins.")
                min_samples = st.slider("Points minimum", 2, 20, 5, help="Nombre de points minimum pour former un groupe.")
                
                lancer_db = st.button("Lancer l'analyse DBSCAN")

            with col2:
                if lancer_db:
                    # Préparation des données
                    X_db = df_db[[sel_x, sel_y]].values
                    
                    # Normalisation (Indispensable pour DBSCAN car basé sur les distances)
                    scaler = StandardScaler()
                    X_scaled = scaler.fit_transform(X_db)

                    # Application de DBSCAN
                    db = DBSCAN(eps=eps, min_samples=min_samples)
                    clusters = db.fit_predict(X_scaled)

                    # Statistiques
                    n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
                    n_noise = list(clusters).count(-1)

                    # Affichage des résultats
                    st.subheader("Résultats")
                    col_res1, col_res2 = st.columns(2)
                    col_res1.metric("Groupes trouvés", n_clusters)
                    col_res2.metric("Anomalies (Bruit)", n_noise)

                    # Visualisation
                    fig, ax = plt.subplots(figsize=(10, 6))
                    # On utilise 'c=clusters' pour colorer par groupe. Le -1 (bruit) ressortira souvent en violet/sombre.
                    scatter = ax.scatter(X_db[:, 0], X_db[:, 1], c=clusters, cmap='viridis', s=50)
                    
                    ax.set_title(f'Clusters: {n_clusters} | Anomalies: {n_noise}')
                    ax.set_xlabel(sel_x)
                    ax.set_ylabel(sel_y)
                    plt.colorbar(scatter, ax=ax, label='ID du Cluster (-1 = Anomalie)')
                    
                    st.pyplot(fig)
                    
                    if n_noise > 0:
                        st.warning(f"DBSCAN a détecté {n_noise} points suspects. Vérifiez ces échantillons sur la ligne de production.")


# ==========================================
# SECTION C1 :  K-means
# ==========================================

#Fiche associée:
elif skill_choice == "- Fiche : K-means":
    st.markdown("<h1 style='text-align: center;'>K-means</h1>", unsafe_allow_html=True)
    st.image("Fiche_C1.png", caption="Fiche explicative : K-means", use_container_width=True)
    def aller_C1():
            st.session_state.page = "K-means"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = "K-means"
            st.session_state.d = " "
    st.button("**Utiliser cette technique**", on_click=aller_C1, use_container_width=True)
    
elif skill_choice == "K-means": 
    st.markdown("<h1 style='text-align: center;'>K-means (Clustering)</h1>", unsafe_allow_html=True)
    def aller_fiche_C1():
            st.session_state.page = "- Fiche : K-means"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = "- Fiche : K-means"
            st.session_state.d = " "
    st.button("**Comment fonctionne cette technique ?**", on_click=aller_fiche_C1, use_container_width=True)
    st.write("""
    Importez vos propres données pour regrouper vos équipements ou vos produits selon leurs caractéristiques techniques.
    """)

    # --- LOGIQUE K-MEANS ---
    def euclidean_distance(x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    class KMeansCustom:
        def __init__(self, k=3, max_iters=100):
            self.k = k
            self.max_iters = max_iters
            self.centroids = None

        def initialize_centroids(self, X):
            idx = np.random.choice(X.shape[0], self.k, replace=False)
            return X[idx]

        def assign_clusters(self, X, centroids):
            clusters = [[] for _ in range(self.k)]
            for i, x in enumerate(X):
                distances = [euclidean_distance(x, c) for c in centroids]
                cluster_idx = np.argmin(distances)
                clusters[cluster_idx].append(i)
            return clusters

        def update_centroids(self, X, clusters):
            centroids = np.zeros((self.k, X.shape[1]))
            for i, cluster in enumerate(clusters):
                if len(cluster) > 0:
                    centroids[i] = np.mean(X[cluster], axis=0)
            return centroids

        def fit(self, X):
            self.centroids = self.initialize_centroids(X)
            for _ in range(self.max_iters):
                # Correction ici : on passe bien X ET les centroids
                clusters = self.assign_clusters(X, self.centroids) 
                
                prev_centroids = self.centroids.copy()
                self.centroids = self.update_centroids(X, clusters)
                
                # Si les centres ne bougent plus, on arrête
                if np.allclose(prev_centroids, self.centroids):
                    break
            return clusters, self.centroids

    # --- ZONE D'IMPORTATION ---
    uploaded_file = st.file_uploader("1. Choisissez un fichier CSV", type="csv")

    if uploaded_file is not None:
        df_km = pd.read_csv(uploaded_file)
        st.write("Aperçu des données :", df_km.head(3))

        # Filtrer uniquement les colonnes numériques
        cols_numeriques = df_km.select_dtypes(include=[np.number]).columns.tolist()

        if len(cols_numeriques) < 2:
            st.error("Le fichier doit contenir au moins 2 colonnes numériques pour la visualisation.")
        else:
            col_setup, col_viz = st.columns([1, 2])

            with col_setup:
                st.subheader("Configuration")
                # Sélection des colonnes pour les axes X et Y
                col_x = st.selectbox("Axe X (Abscisse)", cols_numeriques, index=0)
                col_y = st.selectbox("Axe Y (Ordonnée)", cols_numeriques, index=1)
                
                k_val = st.slider("Nombre de groupes (K)", 2, 8, 3)
                
                # Conversion du dataframe en numpy pour le calcul
                X_input = df_km[[col_x, col_y]].values
                
                btn_run = st.button("Lancer l'analyse")

            with col_viz:
                if btn_run:
                    with st.spinner("Analyse en cours..."):
                        km = KMeansCustom(k=k_val)
                        clusters, centroids = km.fit(X_input)

                        # Graphique des Clusters
                        fig_res, ax_res = plt.subplots()
                        for i, cluster in enumerate(clusters):
                            points = X_input[cluster]
                            if len(points) > 0:
                                ax_res.scatter(points[:, 0], points[:, 1], label=f"Groupe {i+1}")
                        
                        ax_res.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=150, label="Centres")
                        ax_res.set_xlabel(col_x)
                        ax_res.set_ylabel(col_y)
                        ax_res.legend()
                        st.pyplot(fig_res)

                        # Graphique de la méthode du coude
                        st.write("📉 **Optimisation du nombre de groupes**")
                        wcss = []
                        for k in range(1, min(len(X_input), 8)):
                            tk = KMeansCustom(k=k)
                            tc, tcent = tk.fit(X_input)
                            score = sum(euclidean_distance(X_input[idx], tcent[i]) 
                                        for i in range(k) for idx in tc[i])
                            wcss.append(score)
                        
                        fig_elbow, ax_elbow = plt.subplots()
                        ax_elbow.plot(range(1, len(wcss)+1), wcss, marker='o')
                        ax_elbow.set_ylabel("Dispersion totale")
                        st.pyplot(fig_elbow)
    else:
        st.info("En attente d'un fichier CSV pour commencer.")

# ==========================================
# SECTION C3 : SVM
# ==========================================

#Fiche associée:
elif skill_choice == "- Fiche : SVM":
    st.markdown("<h1 style='text-align: center;'>SVM</h1>", unsafe_allow_html=True)
    st.image("Fiche_C3.png", caption="Fiche explicative : SVM", use_container_width=True)
    def aller_C3():
            st.session_state.page = "SVM"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = "SVM"
            st.session_state.d = " "
    st.button("**Utiliser cette technique**", on_click=aller_C3, use_container_width=True)
    
elif skill_choice == "SVM": 
    st.markdown("<h1 style='text-align: center;'>SVM (Support Vector Machine)</h1>", unsafe_allow_html=True)
    def aller_fiche_C3():
            st.session_state.page = "- Fiche : SVM"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = "- Fiche : SVM"
            st.session_state.d = " "
    st.button("**Comment fonctionne cette technique ?**", on_click=aller_fiche_C3, use_container_width=True)

    st.write("Le SVM (Machine à Vecteurs de Support) est idéal pour classer des données complexes en cherchant la meilleure séparation possible entre les catégories.")

    # --- 1. ENTRAÎNEMENT (HISTORIQUE) ---
    st.subheader("Étape 1 : Apprentissage (Historique)")
    file_hist = st.file_uploader("Charger le fichier csv", type="csv", key="hist")

    if file_hist:
        df_hist = pd.read_csv(file_hist)
        target_col = st.selectbox("Quelle colonne contient le résultat réel ?", df_hist.columns)
        
        if st.button("Lancer l'apprentissage"):
            with st.spinner("L'IA apprend des données passées..."):
                X_train = df_hist.drop(columns=[target_col])
                # Conversion automatique du texte en nombres pour les variables explicatives
                X_train = pd.get_dummies(X_train)
                y_train = df_hist[target_col]

                model_pipeline = Pipeline([
                    ('scaler', StandardScaler()),
                    ('svm', svm.SVC(kernel='rbf', C=1.0, probability=True))
                ])
                
                model_pipeline.fit(X_train, y_train)
                st.session_state['svm_model'] = model_pipeline
                st.session_state['svm_columns'] = X_train.columns # On garde les colonnes pour aligner le futur CSV
                st.success("Apprentissage terminé avec succès.")

    # --- 2. PRÉDICTION (ARRIVAGE) ---
    if 'svm_model' in st.session_state:
        st.divider()
        st.subheader(" Étape 2 : Tri des nouvelles données")
        file_new = st.file_uploader("Charger 'ARRIVAGE_A_TRIER.csv'", type="csv", key="new")

        if file_new:
            df_new = pd.read_csv(file_new)
            
            if st.button("Lancer le tri automatique"):
                # Préparation du nouveau CSV (Encoding identique à l'historique)
                X_new = pd.get_dummies(df_new)
                
                # S'assurer que les colonnes sont identiques (alignement)
                X_new = X_new.reindex(columns=st.session_state['svm_columns'], fill_value=0)

                # Prédictions
                preds = st.session_state['svm_model'].predict(X_new)
                probs = st.session_state['svm_model'].predict_proba(X_new)
                confiance = np.max(probs, axis=1)

                df_new['Prediction_IA'] = preds
                df_new['Confiance_IA'] = confiance

                # --- 3. AFFICHAGE AVEC ALERTES ---
                st.write("### Rapport de tri en temps réel")
                
                # On crée une liste pour afficher les alertes proprement
                for i, row in df_new.iterrows():
                    col1, col2, col3, col4 = st.columns([1, 2, 2, 4])
                    
                    with col1:
                        st.write(f"#{i+1}")
                    with col2:
                        st.write(f"**{row['Prediction_IA']}**")
                    with col3:
                        st.write(f"{row['Confiance_IA']:.2%}")
                    with col4:
                        if row['Confiance_IA'] < 0.60:
                            st.error("INSPECTION MANUELLE")
                        else:
                            st.success("Validation Automatique")

                # Bouton de téléchargement
                csv = df_new.to_csv(index=False).encode('utf-8')
                st.download_button("💾 Télécharger le RAPPORT_FINAL_TRI.csv", csv, "RAPPORT_FINAL_TRI.csv", "text/csv")

# ==========================================
# SECTION D1 :  Méthode KNN (KNN)
# ==========================================
#"- Fiche méthode KNN"
#" Méthode KNN"
#Fiche associée:
elif skill_choice == "- Fiche méthode KNN":
    st.markdown("<h1 style='text-align: center;'>KNN</h1>", unsafe_allow_html=True)
    st.image("Fiche_D1.png", caption="Fiche explicative : KNN", use_container_width=True)
    def aller_D1():
            st.session_state.page = " Méthode KNN"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = " "
            st.session_state.d = " Méthode KNN"
    st.button("**Utiliser cette technique**", on_click=aller_D1, use_container_width=True)
    
    
elif skill_choice == " Méthode KNN":
    
    st.markdown("<h1 style='text-align: center;'>KNN</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>k-Nearest Neighbours</h5>", unsafe_allow_html=True)

    def aller_fiche_D1():
            st.session_state.page = "- Fiche méthode KNN"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = " "
            st.session_state.d = "- Fiche méthode KNN"
    st.button("**Comment fonctionne cette technique ?**", on_click=aller_fiche_D1, use_container_width=True)
    #   ÉTAPE 1 : CONFIGURATION ET CHARGEMENT  
    st.subheader("1. Entraînement ou Chargement du modèle")

    col_load1, col_load2 = st.columns(2)

    with col_load1:
        fichier_csv = st.file_uploader("Option A : Charger un CSV pour entraîner", type=['csv'])

    with col_load2:
        if os.path.exists("modele_knn_final.joblib"):
            if st.button("Option B : Charger le dernier modèle enregistré"):
                save_data = joblib.load("modele_knn_final.joblib")
                st.session_state['knn_model'] = save_data['model']
                st.session_state['knn_columns'] = save_data['columns']
                st.session_state['cible_active'] = save_data['target']
                st.session_state['mode_actif'] = save_data['mode']
                st.success(f"Modèle '{save_data['target']}' chargé !")

    if fichier_csv:
        df = pd.read_csv(fichier_csv)
        st.write("Aperçu :", df.head(3))

        col1, col2, col3 = st.columns(3)
        with col2:
            mode_knn = st.radio("Type de prédiction", ["Classification", "Régression"])

        with col1:
            if mode_knn == "Classification":
                colonnes_valides = [c for c in df.columns if df[c].dtype == 'object' or df[c].nunique() < 15]
                classe_cible = st.selectbox("Cible (Catégories)", colonnes_valides)
            else:
                colonnes_num = df.select_dtypes(include=['number']).columns
                # Filtre : au moins 15 valeurs différentes pour être considéré comme une mesure continue
                colonnes_reg = [c for c in colonnes_num if df[c].nunique() >= 15]
                classe_cible = st.selectbox("Cible (Valeur continue)", colonnes_reg if colonnes_reg else colonnes_num)

        with col3:
            k_voisins = st.number_input("Voisins (K)", min_value=1, max_value=20, value=5)

        liste_parametres = [col for col in df.columns if col != classe_cible]

        #   ÉTAPE 2 : ENTRAÎNEMENT  
        if st.button("Entraîner le modèle"):
            from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
            try:
                X, y = df[liste_parametres], df[classe_cible]

                model_knn = KNeighborsClassifier(n_neighbors=k_voisins) if mode_knn == "Classification" else KNeighborsRegressor(n_neighbors=k_voisins)
                model_knn.fit(X, y)

                # Sauvegarde physique avec Joblib
                infos_a_sauver = {
                    'model': model_knn,
                    'columns': liste_parametres,
                    'target': classe_cible,
                    'mode': mode_knn
                }
                joblib.dump(infos_a_sauver, "modele_knn_final.joblib")

                # Mise à jour de la session
                st.session_state['knn_model'] = model_knn
                st.session_state['knn_columns'] = liste_parametres
                st.session_state['cible_active'] = classe_cible
                st.session_state['mode_actif'] = mode_knn
                st.success(f"Modèle enregistré pour prédire : {classe_cible}")
            except Exception as e:
                st.error(f"Erreur : {e}")

    #   ÉTAPE 3 : PRÉDICTION KNN 
    if 'knn_model' in st.session_state:
        # On vérifie si les réglages du haut correspondent au modèle en mémoire
        if 'mode_actif' in st.session_state and fichier_csv and st.session_state['mode_actif'] != mode_knn:
            st.warning(f"Attention : Le modèle chargé est en mode {st.session_state['mode_actif']}. Ré-entraînez pour utiliser le mode {mode_knn}.")

        st.markdown(" ")
        st.subheader(f"2. Tester le modèle ({st.session_state['mode_actif']})")
        st.write(f"Saisissez les paramètres pour estimer **{st.session_state['cible_active']}** :")

        cols_inputs = st.columns(len(st.session_state['knn_columns']))
        valeurs_test = []

        for i, nom_col in enumerate(st.session_state['knn_columns']):
            with cols_inputs[i % len(cols_inputs)]:
                val = st.number_input(f"{nom_col}", value=0.0, key=f"test_{nom_col}")
                valeurs_test.append(val)

        if st.button("Calculer la prédiction"):
            pred = st.session_state['knn_model'].predict([valeurs_test])

            if st.session_state['mode_actif'] == "Classification":
                st.success(f"Résultat : **Classe {pred[0]}**")
            else:
                st.info(f"Résultat : **Valeur {pred[0]:.2f}**")
            

# ==========================================
# SECTION D3 : Régression linéaire
# ==========================================
elif skill_choice == "- Fiche régression linéaire":
    st.markdown("<h1 style='text-align: center;'>Régression linéaire</h1>", unsafe_allow_html=True)
    st.image("Fiche_D3.png", caption="Fiche explicative : régression linéaire", use_container_width=True)
    def aller_D3():
            st.session_state.page = "Régression linéaire"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = " "
            st.session_state.d = "Régression linéaire"
    st.button("**Utiliser cette technique**", on_click=aller_D3, use_container_width=True)
    
elif skill_choice == "Régression linéaire":
    st.markdown("<h1 style='text-align: center;'>Régression linéaire</h1>", unsafe_allow_html=True)

    def aller_fiche_D3():
                st.session_state.page = "- Fiche régression linéaire"
                st.session_state.a = " "
                st.session_state.b = " "
                st.session_state.c = " "
                st.session_state.d = "- Fiche régression linéaire"
    st.button("**Comment fonctionne cette technique ?**", on_click=aller_fiche_D3, use_container_width=True)

    # 1. Chargement du fichier CSV
    fichier_csv = st.file_uploader("Étape 1 : Importez votre fichier CSV", type=['csv'], key="u_reg_lin")

    if fichier_csv:
        df = pd.read_csv(fichier_csv)
        st.write("### Aperçu des données")
        st.dataframe(df.head(5), use_container_width=True)

        cols_numeriques = df.select_dtypes(include=[np.number]).columns.tolist()

        if len(cols_numeriques) < 2:
            st.error("Désolé, votre fichier doit contenir au moins 2 colonnes numériques.")
        else:
            col_sel1, col_sel2 = st.columns(2)
            with col_sel1:
                colonne_cible = st.selectbox("Cible à prédire (Y)", cols_numeriques, key="target_lin")
            with col_sel2:
                options_entrees = [c for c in cols_numeriques if c != colonne_cible]
                colonnes_entrees = st.multiselect("Variables d'influence (X)", options_entrees, default=options_entrees[0])

            if colonnes_entrees:
                if st.button("Étape 2 : Entraîner le modèle", use_container_width=True):
                    try:
                        df_clean = df.dropna(subset=[colonne_cible] + colonnes_entrees)
                        X = df_clean[colonnes_entrees]
                        y = df_clean[colonne_cible]

                        from sklearn.model_selection import train_test_split
                        from sklearn.metrics import r2_score
                        
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                        model = LinearRegression()
                        model.fit(X_train, y_train)

                        y_pred = model.predict(X_test)
                        score_r2 = r2_score(y_test, y_pred)
                        
                        b_val = model.intercept_
                        a_vals = model.coef_

                        st.session_state['lin_active_model'] = {
                            'model': model,
                            'features': colonnes_entrees,
                            'target': colonne_cible,
                            'r2': score_r2,
                            'a': a_vals,
                            'b': b_val
                        }
                        st.success("Modèle entraîné")
                    except Exception as e:
                        st.error(f"Erreur : {e}")

    # --- AFFICHAGE DES RÉSULTATS ET ÉQUATION ---
    if 'lin_active_model' in st.session_state:
        m = st.session_state['lin_active_model']
        
        st.divider()
        st.subheader("2. Analyse et Fiabilité")

        # --- DIAGNOSTIC AUTOMATIQUE DE LINÉARITÉ ---
        if m['r2'] >= 0.85:
            st.success(f"**Diagnostic : Très bien linéaire.** (Précision : {m['r2']*100:.1f}%)  \nLes variations de X expliquent parfaitement Y. Le modèle est fiable.")
        elif 0.5 <= m['r2'] < 0.85:
            st.warning(f"**Diagnostic : Linéarité modérée.** (Précision : {m['r2']*100:.1f}%)  \nIl y a une tendance, mais beaucoup de points s'écartent de la droite (bruit ou facteurs manquants).")
        else:
            st.error(f"**Diagnostic : Pas de relation linéaire.** (Précision : {m['r2']*100:.1f}%)  \nLes points sont trop dispersés ou la relation est courbe. Ne pas utiliser ce modèle pour décider.")

        # Affichage de l'équation
        if len(m['features']) == 1:
            st.latex(f"y = {m['a'][0]:.4f}x + {m['b']:.4f}")
        else:
            equation_text = " + ".join([f"({m['a'][i]:.4f} * {name})" for i, name in enumerate(m['features'])])
            st.info(f"y = {equation_text} + {m['b']:.4f}")

        c1, c2, c3 = st.columns(3)
        c1.metric("Pente (a)", f"{m['a'][0]:.4f}" if len(m['a'])==1 else "Multi")
        c2.metric("Ordonnée (b)", f"{m['b']:.4f}")
        c3.metric("Précision (R²)", f"{m['r2']:.2f}")

        st.subheader("3. Prédiction")
        input_data = []
        cols_input = st.columns(len(m['features']))
        for i, f_name in enumerate(m['features']):
            with cols_input[i % len(cols_input)]:
                # Note : On essaye de récupérer la moyenne depuis le dataframe original pour aider l'utilisateur
                default_val = 0.0
                val = st.number_input(f"Saisir {f_name}", value=default_val, key=f"in_{f_name}")
                input_data.append(val)

        if st.button("Calculer la valeur de Y"):
            prediction = m['model'].predict([input_data])[0]
            
            st.write(f"### Résultat pour {m['target']} :")
            # Résultat affiché dans une boîte verte claire
            st.success(f"### **{prediction:.4f}**")


# ==========================================
# SECTION D5 : Régression logistique
# ==========================================
elif skill_choice == "- Fiche régression logistique":
    st.markdown("<h1 style='text-align: center;'>Régression logistique</h1>", unsafe_allow_html=True)
    st.image("Fiche_D5.png", caption="Fiche explicative : régression logistique", use_container_width=True)
    def aller_D5():
            st.session_state.page = "Régression logistique"
            st.session_state.a = " "
            st.session_state.b = " "
            st.session_state.c = " "
            st.session_state.d = "Régression logistique"
    st.button("**Utiliser cette technique**", on_click=aller_D5, use_container_width=True)
    
elif skill_choice == "Régression logistique":
    st.markdown("<h1 style='text-align: center;'>Régression logistique</h1>", unsafe_allow_html=True)

    def aller_fiche_D5():
                st.session_state.page = "- Fiche régression logistique"
                st.session_state.a = " "
                st.session_state.b = " "
                st.session_state.c = " "
                st.session_state.d = "- Fiche régression logistique"
    st.button("**Comment fonctionne cette technique ?**", on_click=aller_fiche_D5, use_container_width=True)

    # 1. Chargement du fichier CSV
    fichier_csv = st.file_uploader("Étape 1 : Importez votre fichier CSV", type=['csv'], key="u_reg_log")

    if fichier_csv:
        df = pd.read_csv(fichier_csv)
        st.write("### Aperçu des données")
        st.dataframe(df.head(5), use_container_width=True)

        # Identification des colonnes
        cols_all = df.columns.tolist()
        cols_num = df.select_dtypes(include=[np.number]).columns.tolist()

        col_sel1, col_sel2 = st.columns(2)
        with col_sel1:
            # La cible peut être du texte (OK/DEFAUT) ou des chiffres (0/1)
            colonne_cible = st.selectbox("Catégorie à prédire (Y)", cols_all, key="target_log")
        with col_sel2:
            # Les entrées doivent être numériques pour le calcul
            options_entrees = [c for c in cols_num if c != colonne_cible]
            colonnes_entrees = st.multiselect("Paramètres d'influence (X)", options_entrees)

        if colonnes_entrees:
            if st.button("Étape 2 : Entraîner l'IA de classification", use_container_width=True):
                try:
                    from sklearn.linear_model import LogisticRegression
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import accuracy_score

                    # Nettoyage
                    df_clean = df.dropna(subset=[colonne_cible] + colonnes_entrees)
                    X = df_clean[colonnes_entrees]
                    y = df_clean[colonne_cible]

                    # Split 80/20
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    # Entraînement
                    model = LogisticRegression(max_iter=1000)
                    model.fit(X_train, y_train)

                    # Score
                    y_pred = model.predict(X_test)
                    acc = accuracy_score(y_test, y_pred)

                    st.session_state['log_active_model'] = {
                        'model': model,
                        'features': colonnes_entrees,
                        'target': colonne_cible,
                        'accuracy': acc,
                        'classes': model.classes_
                    }
                    st.success(f"✅ Modèle entraîné ! Précision globale : {acc:.2%}")
                except Exception as e:
                    st.error(f"Erreur d'entraînement : {e}")

    # --- RÉSULTATS ET PRÉDICTION ---
    if 'log_active_model' in st.session_state:
        m = st.session_state['log_active_model']
        st.divider()
        
        st.subheader("2. Analyse de fiabilité")
        if m['accuracy'] > 0.80:
            st.success(f"L'IA arrive à classer correctement **{m['accuracy']:.1%}** des cas de test. Fiabilité élevée.")
        else:
            st.warning(f"Précision de **{m['accuracy']:.1%}**. Le modèle peut faire des erreurs de diagnostic.")

        st.subheader("3. Prédire une catégorie")
        st.write("Entrez les paramètres pour connaître la catégorie probable :")
        
        input_data = []
        cols_in = st.columns(len(m['features']))
        for i, f_name in enumerate(m['features']):
            with cols_in[i % len(cols_in)]:
                val = st.number_input(f"{f_name}", value=float(df[f_name].mean()), key=f"log_in_{f_name}")
                input_data.append(val)

        if st.button("Lancer le diagnostic IA"):
            # Prédiction de la classe
            resultat = m['model'].predict([input_data])[0]
            # Calcul de la probabilité (confiance)
            proba = m['model'].predict_proba([input_data])[0]
            confiance = max(proba)

            st.write(f"### Résultat du diagnostic :")
            # Couleur dynamique selon le résultat (si résultat contient "DEFAUT" ou est égal à 0)
            is_bad = str(resultat).lower() in ['defaut', 'défaut', '0', 'ko']
            
            if is_bad:
                st.error(f"**ALERTE : {resultat}** (Confiance : {confiance:.1%})")
            else:
                st.success(f"**CONFORME : {resultat}** (Confiance : {confiance:.1%})")
