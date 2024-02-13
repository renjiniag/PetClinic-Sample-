from flask import Flask, render_template

app = Flask(__name__)

# Sample data for pets
pets = [
    {"id": 1, "name": "Dog", "type": "Mammal", "price": 500},
    {"id": 2, "name": "Cat", "type": "Mammal", "price": 400},
    {"id": 3, "name": "Fish", "type": "Fish", "price": 50},
    {"id": 4, "name": "Parrot", "type": "Bird", "price": 150},
]

@app.route('/')
def home():
    return render_template('index.html', title='Pet Store', pets=pets)

@app.route('/pet/<int:pet_id>')
def pet_detail(pet_id):
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if pet:
        return render_template('pet_detail.html', title=f"{pet['name']} Details", pet=pet)
    else:
        return "Pet not found", 404

if __name__ == '__main__':
    app.run(debug=True)
