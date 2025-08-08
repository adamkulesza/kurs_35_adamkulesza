from flask import Blueprint, render_template, request
from ksiegozbior import get_bookstore_state, change_saldo, create_new_book

ksiegarnia_blueprint = Blueprint('ksiegarnia', __name__)

@ksiegarnia_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        match form_type:
            case 'add_book':
                create_new_book(request.form)
            case 'borrow_book':
                # Here you would handle the logic for buying a book
                pass
            case 'change_balance':
                change_saldo(float(request.form.get('saldo')))

            case _:
                pass
    stan = get_bookstore_state()
    return render_template('ksiegarnia.html', **stan)