from main import app
from flask import render_template, flash
from forms import SearchBar, BigForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    area_of_service = db.Column(db.String(200), nullable=False)
    wallet_add = db.Column(db.String(200), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Title %r>' % self.title

@app.route('/', methods=['POST', 'GET'])
def home():
    search_bar = SearchBar()
    return render_template('home.html', search_bar=search_bar)

@app.route('/sell_item', methods=['POST','GET'])
def sell_item():
    form = BigForm()
    if form.validate_on_submit():
        item_to_add = Item(title=form.title.data, description=form.description.data, area_of_service=form.area_of_service.data,
                           wallet_add=form.wallet_add.data, contact_info=form.contact_info.something.data)
        db.session.add(item_to_add)
        db.session.commit()
        flash("Item added successfully")
        return f"""<h1> Welcome {form.title.data} </h1>"""
    return render_template('sell_item.html', form=form)
@app.route('/stock')
def stock():
    search_bar = SearchBar()
    items_to_show = Item.query.all()
    return render_template('stock.html', search_bar=search_bar, items_to_show=items_to_show)
if __name__ == '__main__':
    app.run(debug=True)