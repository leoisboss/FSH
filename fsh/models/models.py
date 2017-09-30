from . import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    products = db.relationship('Product', back_populates='category')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='products')

    product_entries = db.relationship('ProductEntry', back_populates='product')


class ProductEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String(80))
    taken = db.Column(db.Boolean, default=False)

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', back_populates='product_entries')
