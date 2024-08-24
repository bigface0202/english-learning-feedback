docker build -t asia-northeast1-docker.pkg.dev/ksst-genai-app/genai-app/english-learning-feedback:latest .
docker push asia-northeast1-docker.pkg.dev/ksst-genai-app/genai-app/english-learning-feedback:latest
gcloud run deploy english-learning-feedback \
  --image asia-northeast1-docker.pkg.dev/ksst-genai-app/genai-app/english-learning-feedback:latest \
  --platform managed \
  --region asia-northeast1 \
  --allow-unauthenticated \
  --max-instances 1 \
  --min-instances 0 \
  --memory 512Mi
