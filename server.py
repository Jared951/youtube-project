from flask import Flask, render_template, request, redirect, url_for, flash  # Import 'flash'
from youtube import convert_playlist_to_mp4

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Set a secret key for session security

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
        else:
            flash("Conversion failed. Please check the playlist URL and try again.", "error")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
