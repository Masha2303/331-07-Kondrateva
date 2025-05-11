
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/your_database'
db = SQLAlchemy(app)

class Partner(db.Model):
    __tablename__ = 'partners'
    partner_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    company_name = db.Column(db.String(100), nullable=False)
    legal_address = db.Column(db.Text)
    inn = db.Column(db.String(12))
    director_name = db.Column(db.String(100))
    contact_phone = db.Column(db.String(20))
    contact_email = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    logo = db.Column(db.Text)

class SaleLocation(db.Model):
    __tablename__ = 'sale_locations'
    location_id = db.Column(db.Integer, primary_key=True)
    partner_id = db.Column(db.Integer, db.ForeignKey('partners.partner_id'), nullable=False)
    address = db.Column(db.Text, nullable=False)

class SalesHistory(db.Model):
    __tablename__ = 'sales_history'
    history_id = db.Column(db.Integer, primary_key=True)
    partner_id = db.Column(db.Integer, db.ForeignKey('partners.partner_id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(12, 2), nullable=False)

@app.route('/partners', methods=['GET'])
def get_partners():
    partners = Partner.query.all()
    return jsonify([{
        'partner_id': p.partner_id,
        'company_name': p.company_name,
        'type': p.type,
        'rating': p.rating
    } for p in partners])

@app.route('/partners/<int:partner_id>', methods=['GET'])
def get_partner(partner_id):
    p = Partner.query.get_or_404(partner_id)
    return jsonify({
        'partner_id': p.partner_id,
        'company_name': p.company_name,
        'type': p.type,
        'legal_address': p.legal_address,
        'inn': p.inn,
        'director_name': p.director_name,
        'contact_phone': p.contact_phone,
        'contact_email': p.contact_email,
        'rating': p.rating,
        'logo': p.logo
    })

@app.route('/partners', methods=['POST'])
def add_partner():
    data = request.get_json()
    new_partner = Partner(**data)
    db.session.add(new_partner)
    db.session.commit()
    return jsonify({'message': 'Partner added successfully'}), 201

@app.route('/partners/<int:partner_id>', methods=['PUT'])
def update_partner(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(partner, key, value)
    db.session.commit()
    return jsonify({'message': 'Partner updated successfully'})

@app.route('/partners/<int:partner_id>/sales', methods=['GET'])
def get_sales_by_partner(partner_id):
    sales = SalesHistory.query.filter_by(partner_id=partner_id).all()
    return jsonify([{
        'product_name': s.product_name,
        'sale_date': s.sale_date.isoformat(),
        'quantity': s.quantity,
        'total_price': float(s.total_price)
    } for s in sales])

if __name__ == '__main__':
    app.run(debug=True)
