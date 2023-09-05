import os, shutil, secrets
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from youtube import convert_playlist_to_mp4  

app = Flask(__name__)
secret_key = secrets.token_hex(24)
app.secret_key = secret_key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        playlist_url = request.form['playlist-url']
        output_dir = 'output_directory_here'

        success = convert_playlist_to_mp4(playlist_url, output_dir)

        if success:
            flash("Conversion successful!", "success")
            # Create a zip file and add the downloaded videos to it
            zip_filename = 'playlist_videos.zip'
            shutil.make_archive(os.path.splitext(zip_filename)[0], 'zip', output_dir)
            # Send the zip file as a response for download
            return send_file(zip_filename, as_attachment=True)
        else:
            flash("Conversion failed. Please check the playlist URL and try again.", "error")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)