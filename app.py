from flask import Flask, render_template, request, jsonify, redirect
import os
import uuid
import redis

app = Flask(__name__)

# Configure Redis
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
redis_client = redis.from_url(redis_url)

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
    content = redis_client.get(f"note:{note_id}")
    return jsonify({'content': content.decode('utf-8') if content else ''})

@app.route('/api/note/<note_id>', methods=['POST'])
def save_note(note_id):
    content = request.json.get('content', '')
    redis_client.set(f"note:{note_id}", content)
    return jsonify({'success': True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
