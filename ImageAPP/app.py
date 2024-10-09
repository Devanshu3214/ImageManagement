from flask import Flask, render_template, request, redirect, url_for, send_file, flash, session, Response
import boto3
import os
import io
from io import BytesIO
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = 'myverysecretprivatekey9140730664'

s3 = boto3.client('s3', 
                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), 
                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

BUCKET_NAME = 'devanshubucket'

users = {}

@app.route('/')
def home():
    if 'username' not in session:
        flash('You need to log in to view this page.')
        return redirect(url_for('login'))

    show_encrypted = request.args.get('encrypted', 'false') == 'true'
    images_response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    images = images_response.get('Contents', []) if 'Contents' in images_response else []

    image_urls = []
    for img in images:
        key = img['Key']
        if show_encrypted and not key.endswith('.enc'):
            continue  
        image_urls.append(f"https://{BUCKET_NAME}.s3.amazonaws.com/{key}")

    return render_template('index.html', images=image_urls)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'username' not in session:
        flash('You need to log in to upload files.')
        return redirect(url_for('login'))

    file = request.files['file']
    encrypt = 'encrypt' in request.form

    if file:
        print(f"Received file: {file.filename}")
        file_data = file.read()

        if encrypt:
            encryption_key = Fernet.generate_key()
            cipher = Fernet(encryption_key)
            file_data = cipher.encrypt(file_data)
            filename = f"{file.filename}.enc"
            s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=file_data)
        else:
            s3.put_object(Bucket=BUCKET_NAME, Key=file.filename, Body=file_data)
        
        flash('File uploaded successfully!')
        return redirect(url_for('home'))
    flash('No file selected or error occurred.')
    return redirect(url_for('home'))

@app.route('/download/<filename>')
def download_file(filename):
    decrypt = request.args.get('decrypt', 'false') == 'true'

    # Get the S3 object
    s3_object = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
    encrypted_file_stream = s3_object['Body']
    
    if decrypt:
        flash('Decryption not implemented. Ensure you have the correct key.')
        # You may implement decryption logic here if needed
        return Response(encrypted_file_stream, 
                        headers={
                            'Content-Disposition': f'attachment; filename={filename[:-4]}',
                            'Content-Type': 'application/octet-stream'  # or image type
                        })
    
    return Response(encrypted_file_stream, 
                    headers={
                        'Content-Disposition': f'attachment; filename={filename}',
                        'Content-Type': 'application/octet-stream'  # or image type
                    })


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists!')
            return redirect(url_for('signup'))
        users[username] = password 
        flash('Signup successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('home'))
        flash('Invalid username or password!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
