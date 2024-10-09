# Flask File Upload and Encryption App


# Deployed Link : http://16.170.242.2:5000/


## Screenshots

### Home Page (File List)
![Signup](https://github.com/user-attachments/assets/05636a3d-8135-4b0c-928a-ae01f2581037)



### Upload Page

![Home](https://github.com/user-attachments/assets/d62d345a-288d-4507-8940-05d5ae051c9b)


### Encrypted File

![Show Encrypted](https://github.com/user-attachments/assets/81787611-6e28-4ff1-852c-8fa7459969d3)


## Folder Structure

```
├── app.py           # Main Flask app
├── templates/       # HTML templates
│   ├── index.html   # Home page template
│   ├── login.html   # Login page template
│   ├── signup.html  # Signup page template
├── requirements.txt # List of dependencies
└── README.md        # This file
```

A simple Flask web application that allows users to:
- Upload files to an AWS S3 bucket.
- Optionally encrypt files during upload using the `cryptography` library.
- Download files from the S3 bucket, with an option to decrypt them if they were encrypted.

## Features
- **User Authentication**: Users must sign up and log in before uploading or downloading files.
- **File Upload**: Upload files to an S3 bucket with the option to encrypt them.
- **File Download**: Download files from the S3 bucket, with the option to decrypt them if they were encrypted.
- **Encryption**: Uses AES-based encryption (via the `cryptography.fernet` library) to securely encrypt and decrypt files.
- **AWS S3 Integration**: The app uses `boto3` to manage file storage on AWS S3.

## Getting Started

### Prerequisites

Before running the app, ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [cryptography](https://cryptography.io/en/latest/)

### Environment Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Devanshu3214/ImageManagement.git
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables for AWS and encryption key:
    ```bash
    export AWS_ACCESS_KEY_ID='your_aws_access_key'
    export AWS_SECRET_ACCESS_KEY='your_aws_secret_key'
    export ENCRYPTION_KEY='your_generated_fernet_key'
    export FLASK_APP=app.py
    ```

### Running the Application

To run the Flask app locally, use the following command:
```bash
flask run
# Secure File Storage Application
```

## How to Use

1. **Sign Up**: Create a user account via the `/signup` page.
2. **Log In**: Log in to access the file upload and download functionality.
3. **Upload Files**:
   * Go to the upload page and choose a file.
   * Optionally select the "Encrypt" checkbox to encrypt the file before uploading.
4. **Download Files**:
   * Choose a file from the home page to download.
   * If the file was encrypted, select the "Decrypt" option to download the decrypted version.


## Encryption and Decryption

* The app uses the `cryptography.fernet.Fernet` module for symmetric encryption.
* Files uploaded with the "Encrypt" option will be encrypted using the AES algorithm.
* When downloading encrypted files, users can choose to decrypt them.

## Dependencies

* **Flask**: Web framework.
* **boto3**: AWS SDK for Python to interact with S3.
* **cryptography**: For encrypting and decrypting files.
* **Python-dotenv** (optional): To manage environment variables in a `.env` file.

Install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```


### Notes:
- Replace the placeholder GitHub link with the actual repository link.
- You can update the screenshots with actual images from your application.
- Ensure to add a LICENSE file if applicable.
