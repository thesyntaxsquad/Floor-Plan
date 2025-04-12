from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# mapping of room codes to floor plan images
floor_plans = {
    "SJ2 01": "static/floor_plans/SJ2.01.jpg",
    "SJ2 03": "static/floor_plans/SJ2.03.jpg",
    "SJ2 04": "static/floor_plans/SJ2.04.jpg",
    "SJ2 09": "static/floor_plans/SJ2.09.jpg",
    "SJ2 17": "static/floor_plans/SJ2.17.jpg",
    # More room codes to be added
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_floor_plan/<room_code>')
def get_floor_plan(room_code):
    # Sanitise room code input by user.
    room_code = room_code.strip().upper()
    image_path = floor_plans.get(room_code)
    return jsonify({"image_path": image_path})

if __name__ == '__main__':
    app.run(debug=True)