from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import uuid

app = Flask(__name__)
NOTES_DIR = 'notes'

# Create notes directory if it doesn't exist
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

@app.route('/')
def index():
    # Generate a random note ID using first 8 characters of UUID
    note_id = str(uuid.uuid4())[:8]
    return redirect(f'/{note_id}')

@app.route('/<note_id>')
def get_note(note_id):
    return render_template('notepad.html', note_id=note_id)

@app.route('/api/note/<note_id>', methods=['GET'])
def load_note(note_id):
    file_path = os.path.join(NOTES_DIR, f"{note_id}.txt")
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return jsonify({'content': content})
    except FileNotFoundError:
        return jsonify({'content': ''})

@app.route('/api/note/<note_id>', methods=['POST'])
def save_note(note_id):
    content = request.json.get('content', '')
    file_path = os.path.join(NOTES_DIR, f"{note_id}.txt")
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
