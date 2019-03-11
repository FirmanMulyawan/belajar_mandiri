from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from models import jenis_mainan

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
from models import jenis_mainan

@app.route('/')
def main():
    return 'Hello world'

@app.route("/getAllJenisMainan", methods=['GET'])
def get_all_jenis_mainan():
    try:
        jmainan=jenis_mainan.query.order_by(jenis_mainan.mainan_id).all()
        return jsonify([jmn.serialize() for jmn in jmainan])
    except Exception as e:
        return(str(e))

@app.route("/getJenisMainan/<id_>", methods=['GET'])
def get_jenis_mainan_by_id(id_):
    try:
        jmainan=jenis_mainan.query.filter_by(mainan_id=id_).first()
        return jsonify(jmainan.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addJenisMainan", methods=['POST'])
def add_jenisMainan():
    nama_mainan=request.args.get('nama_mainan')
    pengguna=request.args.get('pengguna')
    harga=request.args.get('harga')

    try:
        jmainan=jenis_mainan (
            nama_mainan=nama_mainan,
            pengguna=pengguna,
            harga=harga
            )
        db.session.add(jmainan)
        db.session.commit()
        return "jenis_mainan added.jmainan id={}".format(jmainan.mainan_id)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

# @app.route("/deleteJenisMainan/<id_>", methods=["DELETE"])
# def delete_jenis_manian_id(id_):
#     try:
#         jmainan=jenis_mainan.query().filter_by(mainan_id=id_).first()
#         jmainan=jenis_mainan.query

@app.route("/deletejenisMainan/<id_>", methods=['DELETE'])
def remove_jenis_Mainan(id_):

    try:
        # customer=Customer.query.filter_by(customer_id=id_).first()
        jmainan=jenis_mainan.query.filter_by(mainan_id=id_).first()
        db.session.delete(jmainan)
        db.session.commit()
        return " jenis_mainan deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateJenisMainan/<id_>", methods=['PUT'])
def update_jenis_mainan(id_):
    try:
        jmainan=jenis_mainan.query.filter_by(mainan_id=id_).first()
        jmainan.nama_mainan=request.args.get('nama_mainan')
        jmainan.pengguna=request.args.get('pengguna')
        jmainan.harga=request.args.get('harga')

        db.session.commit()
        return "jenis_mainan updated. jenis_mainan= " + str(jmainan.nama_mainan)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
        
# if __name__=='__main__':
#     app.run()