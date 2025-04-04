from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        person_file = request.files.get('person_image')
        garment_file = request.files.get('garment_image')

        if not person_file or not garment_file:
            return render_template('result.html', result={"error": "Both images are required."})

        files = {
            'person_image': (person_file.filename, person_file.stream, person_file.mimetype),
            'garment_image': (garment_file.filename, garment_file.stream, garment_file.mimetype)
        }

        headers = {
            'X-API-KEY': 'sk_fa90a4840b4d4e3da1f02e145c5a9198',
            'Accept': 'application/json'
        }

        response = requests.post("https://api.developer.pixelcut.ai/v1/try-on", headers=headers, files=files)

        try:
            result = response.json()
            print("API Response:", result)  # <== Add this
        except Exception:
            result = {"error": "Could not decode response", "raw_response": response.text}

            
        except Exception:
            result = {"error": "Could not decode response", "raw_response": response.text}

        return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
