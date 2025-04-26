from flask import Flask, render_template, request
import boto3
import os

# Initialize Flask
app = Flask(__name__)

# Initialize AWS Translate client with credentials from Environment Variables
translate = boto3.client(
    service_name='translate',
    region_name='us-east-1',
    aws_access_key_id=os.getenv('AKIA3V7UXRTG52XI4UDY'),
    aws_secret_access_key=os.getenv('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')
)

# Function to translate text
def translate_text(text, source_language, target_language):
    try:
        response = translate.translate_text(
            Text=text,
            SourceLanguageCode=source_language,
            TargetLanguageCode=target_language
        )
        return response['TranslatedText']
    except Exception as e:
        return f"Error: {str(e)}"

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the translation
@app.route('/translate', methods=['POST'])
def translate_route():
    # Get form data
    source_text = request.form['source_text']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']

    # Perform translation
    translated_text = translate_text(source_text, source_lang, target_lang)
    
    # Return the result to the template
    return render_template('index.html', translated_text=translated_text)

# Make app accessible to Render
application = app

# Run app locally (only when testing)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
