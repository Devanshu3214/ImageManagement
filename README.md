# Image Management App

## Description

The Image Management App is a web application built using Flask and AWS services that allows users to upload, list, and download images. Users can choose to encrypt their files upon upload, ensuring enhanced security for sensitive data. The application provides functionality to view only encrypted images and download both encrypted and decrypted versions.

## Features

- **Upload Images**: Users can upload images to the application.
- **Encrypt Files**: Users can opt to encrypt their files during the upload process.
- **List Uploaded Images**: A user-friendly interface to view all uploaded images.
- **Download Options**: Users can download images in both encrypted and decrypted formats.
- **Filter Functionality**: Ability to filter and view only encrypted images.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Cloud Services**: AWS S3 for storage
- **Encryption**: AES (Advanced Encryption Standard)

## Installation

### Prerequisites

- Python 3.x
- AWS Account

### Set your AWS credentials in a `.env` file (follow the example below):

```makefile
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
BUCKET_NAME=your_bucket_name




