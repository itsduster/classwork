from flask import Flask, render_template, request, url_for
import os

appp = Flask(__name__)

# Define the image folder
IMAGE_FOLDER = 'static/Image'

@appp.route("/", methods=["GET", "POST"])
def index():
    word = ""  
    image_paths = []

    if request.method == "POST":
       
        word = request.form.get("word", "").strip().upper()
        with open('log.txt', 'a') as log_file:
            log_file.write(word + '\n')
        
        if not word:
            appp.logger.warning("Empty word input received.")
        else:
            
            for char in word:
                image_filename = f"{char}_test.jpg"
                full_image_path = os.path.join(IMAGE_FOLDER, image_filename)

                if os.path.exists(full_image_path):
                    image_paths.append(url_for('static', filename=f'Image/{image_filename}'))
                else:
                    appp.logger.warning(f"Image not found: {full_image_path}")

    return render_template("index.html", images=image_paths, word=word)

if __name__ == "__main__":
    appp.run(debug=True)
