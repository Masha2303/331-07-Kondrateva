from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..services.models import db, Partner, PartnerType, Product, SalesHistory
from ..utils.discount import calculate_discount

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/partners')
def partners_list():
    partners = Partner.query.all()
    partners_data = []
    for partner in partners:
        total_sales = sum(sale.total_amount for sale in partner.sales_history)
        discount = calculate_discount(total_sales)
        partners_data.append({
            'id': partner.id,
            'name': partner.name,
            'type': partner.type.name,
            'director': partner.director_name,
            'phone': partner.contact_phone,
            'rating': partner.rating,
            'discount': discount
        })
    return render_template('partners.html', partners=partners_data)

@bp.route('/partners/new', methods=['GET', 'POST'])
def new_partner():
    if request.method == 'POST':
        try:
            rating = request.form.get('rating', 0)
            if not str(rating).isdigit() or int(rating) < 0:
                flash('Рейтинг должен быть целым и неотрицательным числом', 'danger')
                partner_types = PartnerType.query.all()
                return render_template('new_partner.html', partner_types=partner_types)
            partner = Partner(
                type_id=request.form['type_id'],
                name=request.form['name'],
                legal_address=request.form['legal_address'],
                inn=request.form['inn'],
                director_name=request.form['director_name'],
                contact_phone=request.form['contact_phone'],
                contact_email=request.form['contact_email'],
                logo=request.form.get('logo', ''),
                rating=int(rating),
                sales_locations=request.form.get('sales_locations', '')
            )
            db.session.add(partner)
            db.session.commit()
            flash('Партнёр успешно добавлен', 'success')
            return redirect(url_for('main.partners_list'))
        except Exception as e:
            flash(f'Ошибка при добавлении партнёра: {str(e)}', 'danger')
    partner_types = PartnerType.query.all()
    return render_template('new_partner.html', partner_types=partner_types)

@bp.route('/partners/<int:id>/edit', methods=['GET', 'POST'])
def edit_partner(id):
    partner = Partner.query.get_or_404(id)
    if request.method == 'POST':
        try:
            rating = request.form.get('rating', 0)
            if not str(rating).isdigit() or int(rating) < 0:
                flash('Рейтинг должен быть целым и неотрицательным числом', 'danger')
                partner_types = PartnerType.query.all()
                return render_template('edit_partner.html', partner=partner, partner_types=partner_types)
            partner.type_id = request.form['type_id']
            partner.name = request.form['name']
            partner.legal_address = request.form['legal_address']
            partner.inn = request.form['inn']
            partner.director_name = request.form['director_name']
            partner.contact_phone = request.form['contact_phone']
            partner.contact_email = request.form['contact_email']
            partner.logo = request.form.get('logo', '')
            partner.rating = int(rating)
            partner.sales_locations = request.form.get('sales_locations', '')
            db.session.commit()
            flash('Информация о партнёре успешно обновлена', 'success')
            return redirect(url_for('main.partners_list'))
        except Exception as e:
            flash(f'Ошибка при обновлении информации: {str(e)}', 'danger')
    partner_types = PartnerType.query.all()
    return render_template('edit_partner.html', partner=partner, partner_types=partner_types)

@bp.route('/partners/<int:id>/sales')
def partner_sales(id):
    partner = Partner.query.get_or_404(id)
    sales = SalesHistory.query.filter_by(partner_id=id).all()
    return render_template('partner_sales.html', partner=partner, sales=sales)

@bp.route('/import', methods=['GET', 'POST'])
def import_data():
    import pandas as pd
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Файл не выбран', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Файл не выбран', 'danger')
            return redirect(request.url)
        try:
            if file.filename.endswith('.xlsx'):
                df = pd.read_excel(file)
            elif file.filename.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                flash('Неподдерживаемый формат файла', 'danger')
                return redirect(request.url)
            required_columns = ['Тип партнёра', 'Название', 'Юридический адрес', 'ИНН', 'ФИО директора', 'Контактный телефон', 'Email']
            if not all(col in df.columns for col in required_columns):
                flash('В файле отсутствуют необходимые колонки', 'danger')
                return redirect(request.url)
            for _, row in df.iterrows():
                partner_type = PartnerType.query.filter_by(name=row['Тип партнёра']).first()
                if not partner_type:
                    partner_type = PartnerType(name=row['Тип партнёра'])
                    db.session.add(partner_type)
                    db.session.flush()
                partner = Partner(
                    type_id=partner_type.id,
                    name=row['Название'],
                    legal_address=row['Юридический адрес'],
                    inn=str(row['ИНН']),
                    director_name=row['ФИО директора'],
                    contact_phone=str(row['Контактный телефон']),
                    contact_email=row['Email'],
                    rating=int(row.get('Рейтинг', 0)),
                    sales_locations=row.get('Места реализации', '')
                )
                db.session.add(partner)
            db.session.commit()
            flash('Данные успешно импортированы', 'success')
            return redirect(url_for('main.partners_list'))
        except Exception as e:
            flash(f'Ошибка при импорте данных: {str(e)}', 'danger')
            return redirect(request.url)
    return render_template('import.html')

# ... (остальные маршруты: добавление, редактирование, история, импорт) 