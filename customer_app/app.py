from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from models import Customer

db = SQLAlchemy()
app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': '3210151201900081KTp',
    'db': 'postgres',
    'host': 'localhost',
    'port': '5432'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
from models import Customer

@app.route('/')
def main():
    return 'Hello world'

@app.route("/getAllCustomers", methods=['GET'])
def get_all_customer():
    try:
        customers=Customer.query.order_by(Customer.customer_id).limit(3).all()
        return jsonify([cstr.serialize() for cstr in customers])
    except Exception as e:
        return(str(e))

@app.route("/getCustomer/<id_>", methods=['GET'])
def get_customer_by_id(id_):
    try:
        customer=Customer.query.filter_by(customer_id=id_).first()
        return jsonify(customer.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addCustomer", methods=['POST'])
def add_customer():
    username=request.args.get('username')
    password=request.args.get('password')
    email=request.args.get('email')

    try:
        customer=Customer (
            username=username,
            password=password,
            email=email
            )
        db.session.add(customer)
        db.session.commit()
        return "Customer added.customer id={}".format(customer.customer_id)
    except Exception as e:
        return(str(e))

@app.route("/deleteCustomer/<id_>", methods=['DELETE'])
def remove_customer(id_):

    try:
        customer=Customer.query.filter_by(customer_id=id_).first()
        db.session.delete(customer)
        db.session.commit()
        return " Customer deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

if __name__=='__main__':
    app.run()