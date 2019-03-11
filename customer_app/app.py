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
    finally:
        db.session.close()

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

@app.route('/updateCustomer/<id_>', methods=["PUT"])
def update_Customer(id_):
    updateCustomer = get_customer_by_id(id_).json

    if request.args.get('customer_id') == None:
        customer_id = updateCustomer['customer_id']
    else:
        customer_id = request.args.get('customer_id')
    
    if request.args.get('username') == None:
        username = updateCustomer['username']
    else:
        username = request.args.get('username')

    if request.args.get('password') == None:
        password = updateCustomer['password']
    else:
        password = request.args.get('password')

    if request.args.get('email') == None:
        email = updateCustomer['email']
    else:
        email = request.args.get('email')
    # if request.args.get('kapasitas_memory') == None:
    #     kapasitas_memory = model_existing['kapasitas_memory']
    # else:
    #     kapasitas_memory = request.args.get('kapasitas_memory')

    try:
        CustomerUpdate = {
            'customer_id' : customer_id,
            'username' : username,
            'password' : password,
            'email' : email            
        }
        customer = Customer.query.filter_by(customer_id=id_).update(CustomerUpdate)
        db.session.commit()
        return 'update customer'
    except Exception as e:
        return(str(e))

# if __name__=='__main__':
#     app.run()