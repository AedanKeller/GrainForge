from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Order
from forms import CheckoutForm

@app.route('/')
def index():
    """Homepage with product showcase and hero section"""
    return render_template('index.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Checkout page with order form"""
    form = CheckoutForm()
    
    if form.validate_on_submit():
        # Calculate total (starter kit price: $29.99)
        starter_price = 29.99
        total_amount = starter_price * form.quantity.data
        
        # Create new order
        order = Order(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
            quantity=form.quantity.data,
            total_amount=total_amount
        )
        
        try:
            db.session.add(order)
            db.session.commit()
            flash(f'Thank you {form.name.data}! Your order has been placed successfully. Order ID: {order.id}', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('There was an error processing your order. Please try again.', 'error')
            app.logger.error(f'Order creation failed: {e}')
    
    return render_template('checkout.html', form=form)

@app.route('/about')
def about():
    """About page with company information"""
    return render_template('index.html', scroll_to='about')
