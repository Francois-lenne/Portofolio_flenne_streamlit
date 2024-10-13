# having the google cloud cli on your computer

# having a dockerfile
# docker is install and running


gcloud services enable run.googleapis.com containerregistry.googleapis.com


docker build -t gcr.io/$project_id/$app_name.
docker push gcr.io/$project_id/$app_name 
