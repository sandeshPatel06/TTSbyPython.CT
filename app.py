from flask import Flask, request, render_template, send_file, jsonify
import pyttsx3
import os

app = Flask(__name__)

# Supported languages and their codes for the text-to-speech conversion
languages = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'hi': 'Hindi'
}

@app.route('/')
def index():
    # Render the index.html template and pass the languages dictionary to it
    return render_template('index.html', languages=languages)
    

@app.route('/voices')
def voices():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Create a list of voice options
    voice_options = [{'id': voice.id, 'name': voice.name} for voice in voices]
    
    return jsonify({'voices': voice_options})

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    # Retrieve the text, language code, voice ID, rate, and volume from the form submission
    text = request.form['name']
    language = request.form['language']
    voice_id = request.form['voice']
    rate = int(request.form['rate'])
    volume = float(request.form['volume'])
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set the speech properties
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    
    # Set the selected voice
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.id == voice_id:
            engine.setProperty('voice', voice.id)
            break
    
    # Generate the speech and save it to an MP3 file
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    
    # Send the generated MP3 file as a response to the client
    return send_file('output.mp3', as_attachment=True, download_name='output.mp3')

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
