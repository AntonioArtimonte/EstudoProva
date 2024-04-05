from .models import Database
from flask import request, jsonify, Blueprint, render_template, redirect, Response

db = Database('database/db.json')

main = Blueprint('main', __name__)

@main.route('/')
def index():
    registry = db.get_all_registrations()
    return render_template('index.html', registry=registry)

@main.route('/add_registry', methods=['POST'])
def add_registry():
    registry = request.form.get('registry')
    db.add_registry(registry)
    response = Response(status=200)
    response.headers['HX-Redirect'] = '/'
    return response

@main.route('/delete_registry/<int:id>', methods=['POST'])
def delete_registry(id):
    db.delete_registration(id)
    response = Response(status=200)
    response.headers['HX-Redirect'] = '/'
    return response

@main.route('/update_registry/<int:id>', methods=['GET', 'POST'])
def update_registry(id):
    if request.method == 'POST':
        registry = request.form.get('registry')
        if not db.update_registration(id, registry):
            return jsonify({'error': 'Item not found'}), 404  # Assuming update_registration returns False if not found
        response = Response(status=200)
        response.headers['HX-Redirect'] = '/'
        return response
    else:
        registry = db.get_registration_by_id(id)
        if not registry:
            return jsonify({'error': 'Item not found'}), 404
        return render_template('update.html', registry=registry)
