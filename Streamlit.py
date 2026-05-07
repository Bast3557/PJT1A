import streamlit as st
import numpy as np
from PIL import Image
from skimage.feature import hog
from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

Here is your code with all French text converted to English, without changing any code structure:

``python
PAGE CONFIGURATION  
st.setpageconfig(pagetitle="AI Skills for Manufacturing", layout="wide", pageicon="Logo2.png")

CUSTOM STYLE  
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    / 3. Button hover effect /
    div.stButton > button:hover {
        background-color: #0056b3 !important;
        transform: scale(1.02) !important;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15) !important;
    }
            </style>
    """, unsafeallowhtml=True)
INITIALIZATION (Place at the very top, before the sidebar)
if 'page' not in st.sessionstate:
    st.sessionstate.page = "Home"

Initialize widget keys to prevent them from being empty at start
if 'a' not in st.sessionstate:
    st.sessionstate.a = "Home"
if 'b' not in st.sessionstate:
    st.sessionstate.b = " "
if 'c' not in st.sessionstate:
    st.sessionstate.c = " "
if 'd' not in st.sessionstate:
    st.sessionstate.d = " "

Reset function
def resetothers(currentkey):
    keys = ["a", "b", "c", "d"]
    for key in keys:
        if key != currentkey:
            st.sessionstate[key] = " "
    
    if st.sessionstate[currentkey] != " ":
        st.sessionstate.page = st.sessionstate[currentkey]
SIDEBAR  
st.sidebar.markdown("### AI SKILLS")
st.sidebar.markdown("### Main Menu")

SECTION A
st.sidebar.write("General")
st.sidebar.selectbox(
    "A", [" ", "Home", "Questionnaire"], 
    key="a", 
    onchange=resetothers, 
    args=("a",), # Pass the key to the function
    labelvisibility="collapsed"
)

SECTION B
st.sidebar.write("Observation")
st.sidebar.selectbox(
    "B", [" ", "Image Defect Analysis", "- Guide: Image Defect Analysis", "DBSCAN", "- Guide: DBSCAN"], 
    key="b", 
    onchange=resetothers, 
    args=("b",),
    labelvisibility="collapsed"
)

SECTION C
st.sidebar.write("Classification")
st.sidebar.selectbox(
    "C", [" ", "K-means", "- Guide: K-means", "SVM", "- Guide: SVM"], 
    key="c", 
    onchange=resetothers, 
    args=("c",),
    labelvisibility="collapsed"
)

SECTION D
st.sidebar.write("Prediction")
st.sidebar.selectbox(
    "D", [" ", " KNN Method", "- Guide: KNN Method", "Linear Regression", "- Guide: Linear Regression", "Logistic Regression", "- Guide: Logistic Regression"], 
    key="d", 
    onchange=resetothers, 
    args=("d",),
    labelvisibility="collapsed"
)

Get the final active page
skillchoice = st.sessionstate.page

==========================================
SECTION A1: HOME
==========================================
if skillchoice == "Home":
    # Centered main title
    st.markdown("<h1 style='text-align: center;'>Welcome to AI Skills</h1>", unsafeallowhtml=True)

    with st.container():
        #   OUR PROJECT  
        st.markdown("""
            <h3 style="margin-left: 20px;">Our Project:</h3>""", unsafeallowhtml=True)
        st.markdown("""
        AI Skills for Manufacturing is a student project aimed at making machine learning
        accessible to workers, technicians, and industrial operators. The goal is to 
        allow anyone to use more or less complex machine learning models 
        without ever writing a single line of code.
        """)

        st.write("") # Small space

        st.markdown("""
            <h3 style="margin-left: 20px;">AI Skills is:</h3>""", unsafeallowhtml=True)
        
        # Using symbols to reproduce the arrows from the image
        st.markdown("""
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Interactive toolbox of machine learning techniques  
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Designed for industry  
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Easy to use, simple, intuitive  
        &nbsp;&nbsp;&nbsp;&nbsp;➤ &nbsp; Educational purpose
        """)

        st.write("") # Small space

        st.markdown("""
    <div style='text-align: center;'>
        <em>Details on how each machine learning method works are available at the top of each 
        interface, and the methods can be used directly from the interface.</em>
    </div>
    """, unsafeallowhtml=True) 
        
        st.write("") # Small space

        st.warning("""
        Note on terminology: In this project, we prefer the term Machine Learning rather than Artificial Intelligence.  
    
        Why? Unlike the idea of a "thinking" machine (ChatGPT), our tools rely on mathematical models that learn to recognize patterns from your data to automate decisions in the industrial domain.
        """)
        
        st.write("") # Small space
    
        # Centered subtitle
        st.markdown("<h3 style='text-align: center;'>Our Team</h3>", unsafeallowhtml=True)

            #   DISPLAY OF "Image.png" IMAGE CENTERED  
        colimg1, colimg2, colimg3 = st.columns([1, 2, 1]) 
        with colimg2:
            # Load the local image. usecontainerwidth adapts it to the column.
            st.image("Image.jpeg", caption="Team that created the project", usecontainerwidth=True)

        
        st.subheader("Team Members")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write("CLAUDEL Bastien")
        st.write("Developer")
        st.image("CV1.jpg", usecontainerwidth=True)
        with open("CV1.pdf", "rb") as file:
            btn = st.downloadbutton(
                label="Download CV pdf",
                data=file,
                filename="CVBastienClaudel.pdf",
                mime="image/pdf",
                usecontainerwidth=True
        )

    with col2:
        st.write("LABORDE Julien")
        st.write("Developer")
        st.image("CV2.jpg", usecontainerwidth=True)
        with open("CV2.pdf", "rb") as file:
            btn = st.downloadbutton(
                label="Download CV pdf",
                data=file,
                filename="CVJulienLaborde.pdf",
                mime="image/pdf",
                usecontainerwidth=True
        )
    with col3:
        st.write("TRAMAUX Noah")
        st.write("Developer")
        st.image("CV3.jpg", usecontainerwidth=True)
        with open("CV3.pdf", "rb") as file:
            btn = st.downloadbutton(
                label="Download CV pdf",
                data=file,
                filename="CVNoahTramaux.pdf",
                mime="image/pdf",
                usecontainerwidth=True
            )
    with col4:
        st.write("BREL Thibault")
        st.write("Developer")
        st.image("CV4.jpg", usecontainerwidth=True)
        with open("CV4.pdf", "rb") as file:
            btn = st.downloadbutton(
                label="Download CV pdf",
                data=file,
                filename="CVThibaultBrel.pdf",
                mime="image/pdf",
                usecontainerwidth=True
            )
    with col5:
        st.write("CHEVRIER Héloïse")
        st.write("Developer")
        st.image("CV5.jpg", usecontainerwidth=True)
        with open("CV5.pdf", "rb") as file:
            btn = st.downloadbutton(
                label="Download CV pdf",
                data=file,
                filename="CVHéloïseChevrier.pdf",
                mime="image/pdf",
                usecontainerwidth=True
            )

    with col6:
        st.write("Manohisoa RAZDA")
        st.write("Developer")
        st.image("CV6.jpg", usecontainerwidth=True)
        with open("CV1.pdf", "rb") as file:
            btn = st.downloadbutton(
                label="Download CV pdf",
                data=file,
                filename="CVManohisoaRAZAFINDRAKOTO.pdf",
                mime="image/pdf",
                usecontainerwidth=True
        )
    
    st.markdown(" ") # A separator line for cleanliness
    # Create columns to center or shift the button to the right
    def gotoquestionnaire():
        st.sessionstate.page = "Questionnaire"
        st.sessionstate.a = "Questionnaire"
        st.sessionstate.b = " "
        st.sessionstate.c = " "
        st.sessionstate.d = " "
    st.button("Start processing my data", onclick=gotoquestionnaire, usecontainerwidth=True)
    
==========================================
SECTION A2: QUESTIONNAIRE
==========================================

elif skillchoice == "Questionnaire":
    st.markdown("<h1 style='text-align: center;'>Which machine learning technique should I choose?</h1>", unsafeallowhtml=True)

    st.write("") # Small space
    st.markdown(""" What machine learning techniques do I have at my disposal?""")
    st.markdown("""
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Our site offers 3 categories of techniques: 
        """)

    #Observation
    st.markdown("""
        <h5 style="margin-left: 20px;">➤&nbsp; Observation:</h5>""", unsafeallowhtml=True)
    st.markdown("""
    In industry, it is mainly used for visual quality control. 
    The algorithm learns what a "perfect" (conforming) part looks like and immediately 
    alerts when it detects an irregularity: a scratch, a crack, missing 
    material, or an assembly error. It's a valuable method because it allows 
    real-time production monitoring without needing to catalog in advance 
    all possible types of defects.
    """)

    #Classification
    st.markdown("""
        <h5 style="margin-left: 20px;">➤&nbsp; Classification:</h5>""", unsafeallowhtml=True)
    st.markdown("""
    Classification involves teaching the computer to sort objects or 
    situations into predefined "boxes" or categories. On a production line, 
    this allows, for example, automatic sorting of parts by their model, 
    material (steel, aluminum, plastic), or finish level. Unlike 
    observation which looks for anomalies, classification precisely identifies what 
    the object is by comparing it to a database of examples already known and labeled 
    by technicians.
    """)

    #Prediction
    st.markdown("""
        <h5 style="margin-left: 20px;">➤&nbsp; Prediction:</h5>""", unsafeallowhtml=True)
    st.markdown("""
    Prediction (often called regression in mathematics) does not seek to sort,
    but to calculate a precise numerical value for the future. By analyzing 
    sensor history (temperature, pressure, vibrations), the method can 
    estimate how long a machine can still run before the next 
    breakdown or predict the energy consumption needed for a given task. 
    It's the ideal tool for preventive maintenance: you don't wait for the machine to break, 
    you predict the exact moment when it will need servicing.
    """)

    st.warning("""Warning: The available models only process .csv, .txt files and .png, .jpg, .jpeg images""")

    st.markdown("<h1 style='text-align: center;'>Questionnaire:</h1>", unsafeallowhtml=True)
    st.info("Please answer the questions below to determine the method suited to your problem.")

    # --- STEP 1: FORMAT ---
    st.markdown("### 1. What is the format of your data?")
    formatdata = st.radio(
        "Select the type of support:",
        ["Images (photos of parts, camera captures)", 
         "A data table (numbers, text, CSV file)"],
        index=None, key="q1"
    )

    if formatdata:
        if "Images" in formatdata:
            # --- IMAGE LOGIC ---
            st.markdown("---")
            st.markdown("### 2. Do you have an image database?")
            hasdatabase = st.radio("Select your answer:", ["Yes", "No"], index=None, key="qimg")

            if hasdatabase == "Yes":
                st.success("Recommendation: Image Defect Analysis (Isolation Forest)")
                def goB1():
                    st.sessionstate.page = "Image Defect Analysis"
                    st.sessionstate.a, st.sessionstate.b, st.sessionstate.c, st.sessionstate.d = " ", "Image Defect Analysis", " ", " "
                st.button("Use Image Defect Analysis", onclick=goB1, key="btnisoimg", usecontainerwidth=True)
            elif hasdatabase == "No":
                st.warning("You must first build an image sample.")
                st.linkbutton("Search on Kaggle", "https://www.kaggle.com/")

        else:
            # --- TABLE LOGIC (CSV/TXT) ---
            st.markdown("---")
            st.markdown("### 2. What is the main objective?")
            goal = st.radio(
                "Choose your objective:",
                ["Group my data automatically (without labels)", 
                 "Classify my data according to known categories",
                 "Predict a numerical value (estimation)"],
                index=None, key="q2"
            )

            if goal:
                st.markdown("---")
    
                # --- CLUSTERING CASE ---
                if "Group" in goal:
                    clusterchoice = st.radio("Do you know the number of groups in advance?", ["Yes", "No"], index=None, key="qclust")
                    if clusterchoice == "Yes":
                        st.success("Recommendation: K-means")
                        def goC1():
                            st.sessionstate.page = "K-means"
                            st.sessionstate.a, st.sessionstate.b, st.sessionstate.c, st.sessionstate.d = " ", " ", "K-means", " "
                        st.button("Use K-means", onclick=goC1, key="btnkm", usecontainerwidth=True)
                    elif clusterchoice == "No":
                        st.success("Recommendation: DBSCAN")
                        def goB3():
                            st.sessionstate.page = "DBSCAN"
                            st.sessionstate.a, st.sessionstate.b, st.sessionstate.c, st.sessionstate.d = " ", "DBSCAN", " ", " "
                        st.button("Use DBSCAN", onclick=goB3, key="btndb", usecontainerwidth=True)

                # --- CLASSIFICATION CASE (Adding SVM here) ---
                elif "Classify" in goal:
                    st.success("Recommendation: Several tools are suitable for classification")
                    st.write("Choose the method according to your data complexity:")
                    
                    colc1, colc2, colc3 = st.columns(3)
                    
                    with colc1:
                        st.info("Neighborhood")
                        def goD1():
                            st.sessionstate.page = " KNN Method"
                            st.sessionstate.a, st.sessionstate.b, st.sessionstate.c, st.sessionstate.d = " ", " ", " ", " KNN Method"
                        st.button("Use KNN", onclick=goD1, key="btnknn", usecontainerwidth=True)
                            
                    with colc2:
                        st.info("Binary (Yes/No)")
                        def goD5():
                            st.sessionstate.page = "Logistic Regression"
                            st.sessionstate.a, st.sessionstate.b, st.sessionstate.c, st.sessionstate.d = " ", " ", " ", "Logistic Regression"
                        st.button("Logistic", onclick=goD5, key="btnlog", usecontainerwidth=True)

                    with colc3:
                        st.info("Non-binary Classification")
                        def goC3():
                            st.sessionstate.page = "SVM"
                            st.sessionstate.a = " "
                            st.sessionstate.b = " "
                            st.sessionstate.c = " "
                            st.sessionstate.d = "SVM"
                        st.button("Use SVM", onclick=goC3, key="btnsvm", usecontainerwidth=True)

                # --- PREDICTION CASE ---
                elif "Predict" in goal:
                    st.success("Recommendation: Linear Regression")
                    def goD3():
                        st.sessionstate.page = "Linear Regression"
                        st.sessionstate.a, st.sessionstate.b, st.sessionstate.c, st.sessionstate.d = " ", " ", " ", "Linear Regression"
                    st.button("Use Linear Regression", onclick=goD3, key="btnlin", usecontainerwidth=True)

==========================================
SECTION B1: ISOLATION FOREST (Image Defect Analysis)
==========================================
#Associated guide:
elif skillchoice == "- Guide: Image Defect Analysis":
    st.markdown("<h1 style='text-align: center;'>Image Defect Analysis</h1>", unsafeallowhtml=True)
    st.markdown("<h5 style='text-align: center;'>ISOLATION FOREST</h5>", unsafeallowhtml=True)
    st.image("FicheB1.jpg", caption="Explanatory guide: Image Defect Analysis", usecontainerwidth=True)
    def goB1():
            st.sessionstate.page = "Image Defect Analysis"
            st.sessionstate.a = " "
            st.sessionstate.b = "Image Defect Analysis"
            st.sessionstate.c = " "
            st.sessionstate.d = " "
    st.button("Use this technique", onclick=goB1, usecontainerwidth=True)
    
elif skillchoice == "Image Defect Analysis":
    st.markdown("<h1 style='text-align: center;'>Image Defect Analysis</h1>", unsafeallowhtml=True)
    st.markdown("<h5 style='text-align: center;'>ISOLATION FOREST</h5>", unsafeallowhtml=True)
    def goguideB1():
            st.sessionstate.page = "- Guide: Image Defect Analysis"
            st.sessionstate.a = " "
            st.sessionstate.b = "- Guide: Image Defect Analysis"
            st.sessionstate.c = " "
            st.sessionstate.d = " "
    st.button("How does this technique work?", onclick=goguideB1, usecontainerwidth=True)
    RESOLUTION = 160
    with st.expander("Hyperparameters"):
        contamination = st.slider("Sensitivity threshold (Contamination)", 0.01, 0.20, 0.10)
        st.info(f"Analysis resolution fixed at {RESOLUTION}x{RESOLUTION} to ensure stability.")

    trainfiles = st.fileuploader("1. Upload GOOD images for training",
                                   type=['png', 'jpg', 'jpeg'], acceptmultiplefiles=True)

    if st.button("2. Train the model"):
        if not trainfiles:
            st.error("Please upload training images first.")
        else:
            with st.spinner("Training in progress..."):
                features = []
                for file in trainfiles:
                    # Using fixed resolution
                    img = Image.open(file).convert('L').resize((RESOLUTION, RESOLUTION))
                    fd = hog(np.array(img), orientations=9, pixelspercell=(8, 8), cellsperblock=(2, 2))
                    features.append(fd)

                model = IsolationForest(contamination=contamination, randomstate=42)
                model.fit(np.array(features))
                
                # Store the model in sessionstate
                st.sessionstate['model'] = model
                st.success("Model trained successfully!")

    testfiles = st.fileuploader("3. Upload images to test",
                                  type=['png', 'jpg', 'jpeg'], acceptmultiplefiles=True)

    if st.button("4. Run analysis"):
        if 'model' not in st.sessionstate:
            st.error("The model is not yet trained. Please complete step 2.")
        elif not testfiles:
            st.error("Please upload images to test first.")
        else:
            cols = st.columns(4)
            for idx, file in enumerate(testfiles):
                # Using the same fixed resolution for testing
                img = Image.open(file).convert('L').resize((RESOLUTION, RESOLUTION))
                fd = hog(np.array(img), orientations=9, pixelspercell=(8, 8), cellsperblock=(2, 2))
                
                # Prediction
                score = st.sessionstate['model'].decisionfunction([fd])[0]
                prediction = st.sessionstate['model'].predict([fd])[0]

                with cols[idx % 4]:
                    st.image(img, usecontainerwidth=True)
                    if prediction == -1:
                        st.error(f"DEFECT (Score: {score:.2f})")
                    else:
                        st.success(f"OK (Score: {score:.2f})")
                        
==========================================
SECTION B3: DBSCAN
==========================================
#Associated guide:
elif skillchoice == "- Guide: DBSCAN":
    st.markdown("<h1 style='text-align: center;'>DBSCAN</h1>", unsafeallowhtml=True)
    st.image("FicheB3.png", caption="Explanatory guide: DBSCAN", usecontainerwidth=True)
    def goB3():
            st.sessionstate.page = "DBSCAN"
            st.sessionstate.a = " "
            st.sessionstate.b = "DBSCAN"
            st.sessionstate.c = " "
            st.sessionstate.d = " "
    st.button("Use this technique", onclick=goB3, usecontainerwidth=True)
    
elif skillchoice == "DBSCAN": 
    st.markdown("<h1 style='text-align: center;'>DBSCAN</h1>", unsafeallowhtml=True)
    st.markdown("<h5 style='text-align: center;'>Density-Based Spatial Clustering of Applications with Noise</h5>", unsafeallowhtml=True)

    def goguideB3():
            st.sessionstate.page = "- Guide: DBSCAN"
            st.sessionstate.a = " "
            st.sessionstate.b = "- Guide: DBSCAN"
            st.sessionstate.c = " "
            st.sessionstate.d = " "
    st.button("How does this technique work?", onclick=goguideB3, usecontainerwidth=True)
    
    st.write("""
    The DBSCAN algorithm groups points located in dense areas. 
    Isolated points are automatically marked as 'Noise' (-1)
    """)

    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import StandardScaler

    # --- 1. FILE LOADING ---
    uploadedfiledb = st.fileuploader("Load a CSV for density analysis", type="csv", key="dbscanupload")

    if uploadedfiledb is not None:
        dfdb = pd.readcsv(uploadedfiledb)
        
        # Select numeric columns
        colsnum = dfdb.selectdtypes(include=[np.number]).columns.tolist()

        if len(colsnum) < 2:
            st.error("Need at least 2 numeric columns.")
        else:
            col1, col2 = st.columns([1, 2])

            with col1:
                st.subheader("Hyperparameters")
                selx = st.selectbox("X Axis", colsnum, index=0, key="dbx")
                sely = st.selectbox("Y Axis", colsnum, index=1, key="dby")
                
                st.markdown("---")
                # DBSCAN-specific parameters
                eps = st.slider("Neighborhood distance (eps)", 0.1, 2.0, 0.3, help="Max distance between two points to be neighbors.")
                minsamples = st.slider("Minimum points", 2, 20, 5, help="Minimum number of points to form a group.")
                
                rundb = st.button("Run DBSCAN analysis")

            with col2:
                if rundb:
                    # Data preparation
                    Xdb = dfdb[[selx, sely]].values
                    
                    # Normalization (Essential for DBSCAN as it's distance-based)
                    scaler = StandardScaler()
                    Xscaled = scaler.fittransform(Xdb)

                    # Apply DBSCAN
                    db = DBSCAN(eps=eps, minsamples=minsamples)
                    clusters = db.fitpredict(Xscaled)

                    # Statistics
                    nclusters = len(set(clusters)) - (1 if -1 in clusters else 0)
                    nnoise = list(clusters).count(-1)

                    # Display results
                    st.subheader("Results")
                    colres1, colres2 = st.columns(2)
                    colres1.metric("Groups found", nclusters)
                    colres2.metric("Anomalies (Noise)", nnoise)

                    # Visualization
                    fig, ax = plt.subplots(figsize=(10, 6))
                    # Using 'c=clusters' to color by group. -1 (noise) will often appear in purple/dark.
                    scatter = ax.scatter(Xdb[:, 0], Xdb[:, 1], c=clusters, cmap='viridis', s=50)
                    
                    ax.settitle(f'Clusters: {nclusters} | Anomalies: {nnoise}')
                    ax.setxlabel(selx)
                    ax.setylabel(sely)
                    plt.colorbar(scatter, ax=ax, label='Cluster ID (-1 = Anomaly)')
                    
                    st.pyplot(fig)
                    
                    if nnoise > 0:
                        st.warning(f"DBSCAN detected {nnoise} suspicious points. Check these samples on the production line.")

==========================================
SECTION C1: K-means
==========================================

#Associated guide:
elif skillchoice == "- Guide: K-means":
    st.markdown("<h1 style='text-align: center;'>K-means</h1>", unsafeallowhtml=True)
    st.image("FicheC1.png", caption="Explanatory guide: K-means", usecontainerwidth=True)
    def goC1():
            st.sessionstate.page = "K-means"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = "K-means"
            st.sessionstate.d = " "
    st.button("Use this technique", onclick=goC1, usecontainerwidth=True)
    
elif skillchoice == "K-means": 
    st.markdown("<h1 style='text-align: center;'>K-means (Clustering)</h1>", unsafeallowhtml=True)
    def goguideC1():
            st.sessionstate.page = "- Guide: K-means"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = "- Guide: K-means"
            st.sessionstate.d = " "
    st.button("How does this technique work?", onclick=goguideC1, usecontainerwidth=True)
    st.write("""
    Import your own data to group your equipment or products according to their technical characteristics.
    """)

    # --- K-MEANS LOGIC ---
    def euclideandistance(x1, x2):
        return np.sqrt(np.sum((x1 - x2) * 2))

    class KMeansCustom:
        def init(self, k=3, maxiters=100):
            self.k = k
            self.maxiters = maxiters
            self.centroids = None

        def initializecentroids(self, X):
            idx = np.random.choice(X.shape[0], self.k, replace=False)
            return X[idx]

        def assignclusters(self, X, centroids):
            clusters = [[] for  in range(self.k)]
            for i, x in enumerate(X):
                distances = [euclideandistance(x, c) for c in centroids]
                clusteridx = np.argmin(distances)
                clusters[clusteridx].append(i)
            return clusters

        def updatecentroids(self, X, clusters):
            centroids = np.zeros((self.k, X.shape[1]))
            for i, cluster in enumerate(clusters):
                if len(cluster) > 0:
                    centroids[i] = np.mean(X[cluster], axis=0)
            return centroids

        def fit(self, X):
            self.centroids = self.initializecentroids(X)
            for  in range(self.maxiters):
                # Fix here: passing both X AND centroids
                clusters = self.assignclusters(X, self.centroids) 
                
                prevcentroids = self.centroids.copy()
                self.centroids = self.updatecentroids(X, clusters)
                
                # If centers don't move anymore, stop
                if np.allclose(prevcentroids, self.centroids):
                    break
            return clusters, self.centroids

    # --- IMPORT ZONE ---
    uploadedfile = st.fileuploader("1. Choose a CSV file", type="csv")

    if uploadedfile is not None:
        dfkm = pd.readcsv(uploadedfile)
        st.write("Data preview:", dfkm.head(3))

        # Filter only numeric columns
        colsnumeriques = dfkm.selectdtypes(include=[np.number]).columns.tolist()

        if len(colsnumeriques) < 2:
            st.error("The file must contain at least 2 numeric columns for visualization.")
        else:
            colsetup, colviz = st.columns([1, 2])

            with colsetup:
                st.subheader("Configuration")
                # Select columns for X and Y axes
                colx = st.selectbox("X Axis (Abscissa)", colsnumeriques, index=0)
                coly = st.selectbox("Y Axis (Ordinate)", colsnumeriques, index=1)
                
                kval = st.slider("Number of groups (K)", 2, 8, 3)
                
                # Convert dataframe to numpy for calculation
                Xinput = dfkm[[colx, coly]].values
                
                btnrun = st.button("Run analysis")

            with colviz:
                if btnrun:
                    with st.spinner("Analysis in progress..."):
                        km = KMeansCustom(k=kval)
                        clusters, centroids = km.fit(Xinput)

                        # Cluster graph
                        figres, axres = plt.subplots()
                        for i, cluster in enumerate(clusters):
                            points = Xinput[cluster]
                            if len(points) > 0:
                                axres.scatter(points[:, 0], points[:, 1], label=f"Group {i+1}")
                        
                        axres.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=150, label="Centers")
                        axres.setxlabel(colx)
                        axres.setylabel(coly)
                        axres.legend()
                        st.pyplot(figres)

                        # Elbow method graph
                        st.write("📉 Optimizing the number of groups")
                        wcss = []
                        for k in range(1, min(len(Xinput), 8)):
                            tk = KMeansCustom(k=k)
                            tc, tcent = tk.fit(Xinput)
                            score = sum(euclideandistance(Xinput[idx], tcent[i]) 
                                        for i in range(k) for idx in tc[i])
                            wcss.append(score)
                        
                        figelbow, axelbow = plt.subplots()
                        axelbow.plot(range(1, len(wcss)+1), wcss, marker='o')
                        axelbow.setylabel("Total dispersion")
                        st.pyplot(figelbow)
    else:
        st.info("Waiting for a CSV file to begin.")

==========================================
SECTION C3: SVM
==========================================

#Associated guide:
elif skillchoice == "- Guide: SVM":
    st.markdown("<h1 style='text-align: center;'>SVM</h1>", unsafeallowhtml=True)
    st.image("FicheC3.png", caption="Explanatory guide: SVM", usecontainerwidth=True)
    def goC3():
            st.sessionstate.page = "SVM"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = "SVM"
            st.sessionstate.d = " "
    st.button("Use this technique", onclick=goC3, usecontainerwidth=True)
    
elif skillchoice == "SVM": 
    st.markdown("<h1 style='text-align: center;'>SVM (Support Vector Machine)</h1>", unsafeallowhtml=True)
    def goguideC3():
            st.sessionstate.page = "- Guide: SVM"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = "- Guide: SVM"
            st.sessionstate.d = " "
    st.button("How does this technique work?", onclick=goguideC3, usecontainerwidth=True)

    st.write("SVM (Support Vector Machine) is ideal for classifying complex data by finding the best possible separation between categories.")

    # --- 1. TRAINING (HISTORICAL) ---
    st.subheader("Step 1: Learning (Historical Data)")
    filehist = st.fileuploader("Load the CSV file", type="csv", key="hist")

    if filehist:
        dfhist = pd.readcsv(filehist)
        targetcol = st.selectbox("Which column contains the actual result?", dfhist.columns)
        
        if st.button("Start learning"):
            with st.spinner("AI is learning from past data..."):
                Xtrain = dfhist.drop(columns=[targetcol])
                # Automatic text-to-number conversion for explanatory variables
                Xtrain = pd.getdummies(Xtrain)
                ytrain = dfhist[targetcol]

                modelpipeline = Pipeline([
                    ('scaler', StandardScaler()),
                    ('svm', svm.SVC(kernel='rbf', C=1.0, probability=True))
                ])
                
                modelpipeline.fit(Xtrain, ytrain)
                st.sessionstate['svmmodel'] = modelpipeline
                st.sessionstate['svmcolumns'] = Xtrain.columns # Keep columns to align future CSV
                st.success("Learning completed successfully.")

    # --- 2. PREDICTION (NEW DATA) ---
    if 'svmmodel' in st.sessionstate:
        st.divider()
        st.subheader("Step 2: Sorting new data")
        filenew = st.fileuploader("Load 'NEWDATATOSORT.csv'", type="csv", key="new")

        if filenew:
            dfnew = pd.readcsv(filenew)
            
            if st.button("Run automatic sorting"):
                # Prepare new CSV (Encoding identical to historical)
                Xnew = pd.getdummies(dfnew)
                
                # Ensure columns are identical (alignment)
                Xnew = Xnew.reindex(columns=st.sessionstate['svmcolumns'], fillvalue=0)

                # Predictions
                preds = st.sessionstate['svmmodel'].predict(Xnew)
                probs = st.sessionstate['svmmodel'].predictproba(Xnew)
                confidence = np.max(probs, axis=1)

                dfnew['AIPrediction'] = preds
                dfnew['AIConfidence'] = confidence

                # --- 3. DISPLAY WITH ALERTS ---
                st.write("### Real-time sorting report")
                
                # Create a list to display alerts properly
                for i, row in dfnew.iterrows():
                    col1, col2, col3, col4 = st.columns([1, 2, 2, 4])
                    
                    with col1:
                        st.write(f"#{i+1}")
                    with col2:
                        st.write(f"{row['AIPrediction']}")
                    with col3:
                        st.write(f"{row['AIConfidence']:.2%}")
                    with col4:
                        if row['AIConfidence'] < 0.60:
                            st.error("MANUAL INSPECTION")
                        else:
                            st.success("Automatic Validation")

                # Download button
                csv = dfnew.tocsv(index=False).encode('utf-8')
                st.downloadbutton("💾 Download FINALSORTINGREPORT.csv", csv, "FINALSORTINGREPORT.csv", "text/csv")

==========================================
SECTION D1: KNN Method
==========================================
#"- Guide: KNN Method"
#" KNN Method"
#Associated guide:
elif skillchoice == "- Guide: KNN Method":
    st.markdown("<h1 style='text-align: center;'>KNN</h1>", unsafeallowhtml=True)
    st.image("FicheD1.png", caption="Explanatory guide: KNN", usecontainerwidth=True)
    def goD1():
            st.sessionstate.page = " KNN Method"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = " "
            st.sessionstate.d = " KNN Method"
    st.button("Use this technique", onclick=goD1, usecontainerwidth=True)
    
    
elif skillchoice == " KNN Method":
    
    st.markdown("<h1 style='text-align: center;'>KNN</h1>", unsafeallowhtml=True)
    st.markdown("<h5 style='text-align: center;'>k-Nearest Neighbors</h5>", unsafeallowhtml=True)

    def goguideD1():
            st.sessionstate.page = "- Guide: KNN Method"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = " "
            st.sessionstate.d = "- Guide: KNN Method"
    st.button("How does this technique work?", onclick=goguideD1, usecontainerwidth=True)
    #   STEP 1: CONFIGURATION AND LOADING  
    st.subheader("1. Training or Loading the model")

    colload1, colload2 = st.columns(2)

    with colload1:
        fichiercsv = st.fileuploader("Option A: Load a CSV for training", type=['csv'])

    with colload2:
        if os.path.exists("modeleknnfinal.joblib"):
            if st.button("Option B: Load the last saved model"):
                savedata = joblib.load("modeleknnfinal.joblib")
                st.sessionstate['knnmodel'] = savedata['model']
                st.sessionstate['knncolumns'] = savedata['columns']
                st.sessionstate['cibleactive'] = savedata['target']
                st.sessionstate['modeactif'] = savedata['mode']
                st.success(f"Model '{savedata['target']}' loaded!")

    if fichiercsv:
        df = pd.readcsv(fichiercsv)
        st.write("Preview:", df.head(3))

        col1, col2, col3 = st.columns(3)
        with col2:
            modeknn = st.radio("Prediction type", ["Classification", "Regression"])

        with col1:
            if modeknn == "Classification":
                colonnesvalides = [c for c in df.columns if df[c].dtype == 'object' or df[c].nunique() < 15]
                classecible = st.selectbox("Target (Categories)", colonnesvalides)
            else:
                colonnesnum = df.selectdtypes(include=['number']).columns
                # Filter: at least 15 different values to be considered a continuous measure
                colonnesreg = [c for c in colonnesnum if df[c].nunique() >= 15]
                classecible = st.selectbox("Target (Continuous value)", colonnesreg if colonnesreg else colonnesnum)

        with col3:
            kvoisins = st.numberinput("Neighbors (K)", minvalue=1, maxvalue=20, value=5)

        listeparametres = [col for col in df.columns if col != classecible]

        #   STEP 2: TRAINING  
        if st.button("Train the model"):
            from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
            try:
                X, y = df[listeparametres], df[classecible]

                modelknn = KNeighborsClassifier(nneighbors=kvoisins) if modeknn == "Classification" else KNeighborsRegressor(nneighbors=kvoisins)
                modelknn.fit(X, y)

                # Physical save with Joblib
                infosasauver = {
                    'model': modelknn,
                    'columns': listeparametres,
                    'target': classecible,
                    'mode': modeknn
                }
                joblib.dump(infosasauver, "modeleknnfinal.joblib")

                # Update session
                st.sessionstate['knnmodel'] = modelknn
                st.sessionstate['knncolumns'] = listeparametres
                st.sessionstate['cibleactive'] = classecible
                st.sessionstate['modeactif'] = modeknn
                st.success(f"Model saved to predict: {classecible}")
            except Exception as e:
                st.error(f"Error: {e}")

    #   STEP 3: KNN PREDICTION 
    if 'knnmodel' in st.sessionstate:
        # Check if top settings match the model in memory
        if 'modeactif' in st.sessionstate and fichiercsv and st.sessionstate['modeactif'] != modeknn:
            st.warning(f"Warning: The loaded model is in {st.sessionstate['modeactif']} mode. Retrain to use {modeknn} mode.")

        st.markdown(" ")
        st.subheader(f"2. Test the model ({st.sessionstate['modeactif']})")
        st.write(f"Enter the parameters to estimate {st.sessionstate['cibleactive']}:")

        colsinputs = st.columns(len(st.sessionstate['knncolumns']))
        valeurstest = []

        for i, nomcol in enumerate(st.sessionstate['knncolumns']):
            with colsinputs[i % len(colsinputs)]:
                val = st.numberinput(f"{nomcol}", value=0.0, key=f"test{nomcol}")
                valeurstest.append(val)

        if st.button("Calculate prediction"):
            pred = st.sessionstate['knnmodel'].predict([valeurstest])

            if st.sessionstate['modeactif'] == "Classification":
                st.success(f"Result: Class {pred[0]}")
            else:
                st.info(f"Result: Value {pred[0]:.2f}")
            

==========================================
SECTION D3: Linear Regression
==========================================
elif skillchoice == "- Guide: Linear Regression":
    st.markdown("<h1 style='text-align: center;'>Linear Regression</h1>", unsafeallowhtml=True)
    st.image("FicheD3.png", caption="Explanatory guide: Linear Regression", usecontainerwidth=True)
    def goD3():
            st.sessionstate.page = "Linear Regression"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = " "
            st.sessionstate.d = "Linear Regression"
    st.button("Use this technique", onclick=goD3, usecontainerwidth=True)
    
elif skillchoice == "Linear Regression":
    st.markdown("<h1 style='text-align: center;'>Linear Regression</h1>", unsafeallowhtml=True)

    def goguideD3():
                st.sessionstate.page = "- Guide: Linear Regression"
                st.sessionstate.a = " "
                st.sessionstate.b = " "
                st.sessionstate.c = " "
                st.sessionstate.d = "- Guide: Linear Regression"
    st.button("How does this technique work?", onclick=goguideD3, usecontainerwidth=True)

    # 1. Load CSV file
    fichiercsv = st.fileuploader("Step 1: Import your CSV file", type=['csv'], key="ureglin")

    if fichiercsv:
        df = pd.readcsv(fichiercsv)
        st.write("### Data preview")
        st.dataframe(df.head(5), usecontainerwidth=True)

        colsnumeriques = df.selectdtypes(include=[np.number]).columns.tolist()

        if len(colsnumeriques) < 2:
            st.error("Sorry, your file must contain at least 2 numeric columns.")
        else:
            colsel1, colsel2 = st.columns(2)
            with colsel1:
                colonnecible = st.selectbox("Target to predict (Y)", colsnumeriques, key="targetlin")
            with colsel2:
                optionsentrees = [c for c in colsnumeriques if c != colonnecible]
                colonnesentrees = st.multiselect("Influence variables (X)", optionsentrees, default=optionsentrees[0])

            if colonnesentrees:
                if st.button("Step 2: Train the model", usecontainerwidth=True):
                    try:
                        dfclean = df.dropna(subset=[colonnecible] + colonnesentrees)
                        X = dfclean[colonnesentrees]
                        y = dfclean[colonnecible]

                        from sklearn.modelselection import traintestsplit
                        from sklearn.metrics import r2score
                        
                        Xtrain, Xtest, ytrain, ytest = traintestsplit(X, y, testsize=0.2, randomstate=42)

                        model = LinearRegression()
                        model.fit(Xtrain, ytrain)

                        ypred = model.predict(Xtest)
                        scorer2 = r2score(ytest, ypred)
                        
                        bval = model.intercept
                        avals = model.coef

                        st.sessionstate['linactivemodel'] = {
                            'model': model,
                            'features': colonnesentrees,
                            'target': colonnecible,
                            'r2': scorer2,
                            'a': avals,
                            'b': bval
                        }
                        st.success("Model trained")
                    except Exception as e:
                        st.error(f"Error: {e}")

    # --- DISPLAY RESULTS AND EQUATION ---
    if 'linactivemodel' in st.sessionstate:
        m = st.sessionstate['linactivemodel']
        
        st.divider()
        st.subheader("2. Analysis and Reliability")

        # --- AUTOMATIC LINEARITY DIAGNOSTIC ---
        if m['r2'] >= 0.85:
            st.success(f"Diagnosis: Very well linear. (Accuracy: {m['r2']100:.1f}%)  \nVariations in X perfectly explain Y. The model is reliable.")
        elif 0.5 <= m['r2'] < 0.85:
            st.warning(f"Diagnosis: Moderate linearity. (Accuracy: {m['r2']100:.1f}%)  \nThere is a trend, but many points deviate from the line (noise or missing factors).")
        else:
            st.error(f"Diagnosis: No linear relationship. (Accuracy: {m['r2']100:.1f}%)  \nPoints are too scattered or the relationship is curved. Do not use this model for decisions.")

        # Display equation
        if len(m['features']) == 1:
            st.latex(f"y = {m['a'][0]:.4f}x + {m['b']:.4f}")
        else:
            equationtext = " + ".join([f"({m['a'][i]:.4f} * {name})" for i, name in enumerate(m['features'])])
            st.info(f"y = {equationtext} + {m['b']:.4f}")

        c1, c2, c3 = st.columns(3)
        c1.metric("Slope (a)", f"{m['a'][0]:.4f}" if len(m['a'])==1 else "Multi")
        c2.metric("Intercept (b)", f"{m['b']:.4f}")
        c3.metric("Accuracy (R²)", f"{m['r2']:.2f}")

        st.subheader("3. Prediction")
        inputdata = []
        colsinput = st.columns(len(m['features']))
        for i, fname in enumerate(m['features']):
            with colsinput[i % len(colsinput)]:
                # Note: Trying to retrieve the mean from the original dataframe to help the user
                defaultval = 0.0
                val = st.numberinput(f"Enter {fname}", value=defaultval, key=f"in{fname}")
                inputdata.append(val)

        if st.button("Calculate the value of Y"):
            prediction = m['model'].predict([inputdata])[0]
            
            st.write(f"### Result for {m['target']}:")
            # Result displayed in a light green box
            st.success(f"### {prediction:.4f}")

==========================================
SECTION D5: Logistic Regression
==========================================
elif skillchoice == "- Guide: Logistic Regression":
    st.markdown("<h1 style='text-align: center;'>Logistic Regression</h1>", unsafeallowhtml=True)
    st.image("FicheD5.png", caption="Explanatory guide: Logistic Regression", usecontainerwidth=True)
    def goD5():
            st.sessionstate.page = "Logistic Regression"
            st.sessionstate.a = " "
            st.sessionstate.b = " "
            st.sessionstate.c = " "
            st.sessionstate.d = "Logistic Regression"
    st.button("Use this technique", onclick=goD5, usecontainerwidth=True)
    
elif skillchoice == "Logistic Regression":
    st.markdown("<h1 style='text-align: center;'>Logistic Regression</h1>", unsafeallowhtml=True)

    def goguideD5():
                st.sessionstate.page = "- Guide: Logistic Regression"
                st.sessionstate.a = " "
                st.sessionstate.b = " "
                st.sessionstate.c = " "
                st.sessionstate.d = "- Guide: Logistic Regression"
    st.button("How does this technique work?", onclick=goguideD5, usecontainerwidth=True)

    # 1. Load CSV file
    fichiercsv = st.fileuploader("Step 1: Import your CSV file", type=['csv'], key="ureglog")

    if fichiercsv:
        df = pd.readcsv(fichiercsv)
        st.write("### Data preview")
        st.dataframe(df.head(5), usecontainerwidth=True)

        # Column identification
        colsall = df.columns.tolist()
        colsnum = df.selectdtypes(include=[np.number]).columns.tolist()

        colsel1, colsel2 = st.columns(2)
        with colsel1:
            # Target can be text (OK/DEFECT) or numbers (0/1)
            colonnecible = st.selectbox("Category to predict (Y)", colsall, key="targetlog")
        with colsel2:
            # Inputs must be numeric for calculation
            optionsentrees = [c for c in colsnum if c != colonnecible]
            colonnesentrees = st.multiselect("Influence parameters (X)", optionsentrees)

        if colonnesentrees:
            if st.button("Step 2: Train the classification AI", usecontainerwidth=True):
                try:
                    from sklearn.linearmodel import LogisticRegression
                    from sklearn.modelselection import traintestsplit
                    from sklearn.metrics import accuracyscore

                    # Cleaning
                    dfclean = df.dropna(subset=[colonnecible] + colonnesentrees)
                    X = dfclean[colonnesentrees]
                    y = dfclean[colonnecible]

                    # 80/20 split
                    Xtrain, Xtest, ytrain, ytest = traintestsplit(X, y, testsize=0.2, randomstate=42)

                    # Training
                    model = LogisticRegression(maxiter=1000)
                    model.fit(Xtrain, ytrain)

                    # Score
                    ypred = model.predict(Xtest)
                    acc = accuracyscore(ytest, ypred)

                    st.sessionstate['logactivemodel'] = {
                        'model': model,
                        'features': colonnesentrees,
                        'target': colonnecible,
                        'accuracy': acc,
                        'classes': model.classes
                    }
                    st.success(f"✅ Model trained! Overall accuracy: {acc:.2%}")
                except Exception as e:
                    st.error(f"Training error: {e}")

    # --- RESULTS AND PREDICTION ---
    if 'logactivemodel' in st.sessionstate:
        m = st.sessionstate['logactivemodel']
        st.divider()
        
        st.subheader("2. Reliability analysis")
        if m['accuracy'] > 0.80:
            st.success(f"The AI correctly classifies {m['accuracy']:.1%} of test cases. High reliability.")
        else:
            st.warning(f"Accuracy of {m['accuracy']:.1%}. The model may make diagnostic errors.")

        st.subheader("3. Predict a category")
        st.write("Enter the parameters to know the likely category:")
        
        inputdata = []
        colsin = st.columns(len(m['features']))
        for i, fname in enumerate(m['features']):
            with colsin[i % len(colsin)]:
                val = st.numberinput(f"{fname}", value=float(df[fname].mean()), key=f"login{fname}")
                inputdata.append(val)

        if st.button("Run AI diagnosis"):
            # Class prediction
            resultat = m['model'].predict([inputdata])[0]
            # Probability calculation (confidence)
            proba = m['model'].predictproba([inputdata])[0]
            confiance = max(proba)

            st.write(f"### Diagnosis result:")
            # Dynamic color based on result (if result contains "DEFECT" or equals 0)
            isbad = str(resultat).lower() in ['defect', 'défaut', '0', 'ko']
            
            if is_bad:
                st.error(f"ALERT: {resultat} (Confidence: {confiance:.1%})")
            else:
                st.success(f"CONFORMING: {resultat} (Confidence: {confiance:.1%})")
