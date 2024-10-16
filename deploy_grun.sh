# having the google cloud cli on your computer

# enable the api for the artifact registry


# having a dockerfile
# docker is install and running




# create a repo in artifact registry



gcloud artifacts repositories create [NOM_DU_REPO] --repository-format=docker --location=[REGION] --description="[DESCRIPTION]"


# Construire l'image docker 


docker build -t [REGION]-docker.pkg.dev/[PROJET_ID]/[NOM_DU_REPO]/[NOM_IMAGE]:[TAG] .



# configurer l'authentification 


docker push [REGION]-docker.pkg.dev/[PROJET_ID]/[NOM_DU_REPO]/[NOM_IMAGE]:[TAG]


# run the google cloud run 


gcloud run deploy [NOM_SERVICE] \
  --image=[REGION]-docker.pkg.dev/[PROJET_ID]/[NOM_DU_REPO]/[NOM_IMAGE]:[TAG] \
  --platform=managed \
  --region=[REGION] \
  --port=8080 \
  --allow-unauthenticated