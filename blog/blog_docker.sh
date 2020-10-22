sudo docker build -t django_blog .
sudo docker run -d -i -t -p 8080:8000 django_blog