
### Backend Assignment
## Overview
developing a Django application using Django REST Framework (DRF) to interact with OpenAI’s GPT-4 and DALL-E APIs for text generation and image manipulation. The project involves creating an API that allows multiple stakeholders to upload and edit images, handling special instructions, and tracking metrics.

## Features
1. ### Image Upload & Editing :
Users can upload images and generate images using prompts via the DALL-E API.

Users can edit images with special instructions such as adjusting brightness, contrast, and sharpness.

2. ### Special Instructions Handling :
The application can divert code flow to handle specific instructions like saving images or adjusting image properties.

3. ### Metrics Tracking : 

The application tracks and stores metrics related to API usage and function usage.

Metrics are tracked on a per-user basis, as well as aggregated globally.

4. ### Database Integration with S3: 

Images and their metadata are stored in a PostgreSQL database, with the actual image files being stored in an Amazon S3 bucket.

5. [HPL-Benchmark](#HPL-Benchmark) - High-Performance Linpack benchmark implementation

## Architecture

1. ### Backend: 
Django framework with Django REST Framework (DRF) for creating RESTful APIs.

2. ### Database: 
PostgreSQL for storing user data, image metadata, and metrics.

3. ### Storage: 
Amazon S3 for storing image files.

4. ### APIs: 
Integration with OpenAI’s GPT-4 and DALL-E for text generation and image manipulation.

## Setup :
1. ### Clone the Repository :

git clone https://github.com/RajaKanwar/backend_assignment.git
cd backend_assignment

2. ### Create and Activate Virtual Environment

python3 -m venv venv

On Windows use `venv\Scripts\activate`

3. ### Install Dependencies

pip install -r requirements.txt

4. ### Set Up PostgreSQL

Install PostgreSQL and create a database.

Update the backend_assignment/settings.py file with your PostgreSQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'backend_DB',
        'USER': 'Raja',
        'PASSWORD': '007Raja',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


5. ### Configure AWS S3

Set up an S3 bucket in AWS.

Update your backend_assignment/settings.py with your S3 configuration.

6. ### Run Migrations

python manage.py makemigrations

python manage.py migrate

7. ### Create a Superuser

python manage.py createsuperuser

8. ### Start the Development Server

python manage.py runserver

## Conclusion

This project demonstrates a full-stack approach to building a scalable, secure backend application integrated with external APIs. By following industry best practices and focusing on robustness, this project is well-prepared for deployment in a real-world environment.
