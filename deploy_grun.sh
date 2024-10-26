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




  # create the secrets for google cloud build 



  # Create and set secrets
gcloud secrets create LOCATION --data-file=<(echo "europe-west1")
gcloud secrets create REPOSITORY --data-file=<(echo "my-repository")
gcloud secrets create IMAGE --data-file=<(echo "my-app")
gcloud secrets create TAG --data-file=<(echo "latest")
gcloud secrets create SERVICE_NAME --data-file=<(echo "my-service")
gcloud secrets create REGION --data-file=<(echo "europe-west1")


# give access to the secrets to google cloud build 



gcloud projects list --filter="$(gcloud config get-value project)" --format="value(PROJECT_NUMBER)"



PROJECT_NUMBER=$(gcloud projects list --filter="$(gcloud config get-value project)" --format="value(PROJECT_NUMBER)")


CLOUD_BUILD_SA="${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com"


gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$CLOUD_BUILD_SA" \
    --role="roles/secretmanager.secretAccessor"