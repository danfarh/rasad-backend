# rasad-backend

# About The Project
  Rasad is a startup project that is about managing visitors, The boss can monitor the visitors with this app.

## Technologies used in this project:
  - python
  - django
  - django rest framework
  - docker 
  - nginx
  - postgres
  
   ------------------------------------

### create volume

    docker volume create postgres_data
    
    docker volume create static_file
    
    docker volume create media_file
   
### create network
   
    docker network create main
    
### build service

    docker-compose build

### run service 
 
    docker-compose up -d  

### exec service and create super user 
    docker exec -it app sh
    docker exec -it app sh -c "python manage.py createsuperuser"