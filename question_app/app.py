from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from models import jenis_mainan

db = SQLAlchemy()
app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': '3210151201900081KTp',
    'db': 'kahoot',
    'host': 'localhost',
    'port': '5432'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
from models import ClassQuestion

@app.route('/')
def main():
    return 'Hello questions'

@app.route("/getAllQuestions", methods=['GET'])
def get_all_Questions():
    try:
        Questions = ClassQuestion.query.order_by(ClassQuestion.id_questions).all()
        return jsonify([Question.serialize() for Question in Questions])
    except Exception as e:
        return(str(e))

@app.route("/getQuestion/<id_>", methods=['GET'])
def get_Question(id_):
    try:
        getQuestion = ClassQuestion.query.filter_by(id_questions = id_).first()
        return jsonify(getQuestion.serialize())
    except Exception as e:
        return(str(e))

@app.route("/addQuestions", methods=['POST'])
def add_Questions():
    quiz_id = request.args.get('quiz_id')
    question = request.args.get('question')
    number = request.args.get('number')
    answer = request.args.get('answer')
    created_at = request.args.get('created_at')
    modified_at = request.args.get('modified_at')
    deleted_at = request.args.get('deleted_at')

    try:
        addQuestions = ClassQuestion (
            quiz_id = quiz_id,
            question = question,
            number = number,
            answer = answer,
            created_at = created_at,
            modified_at = modified_at,
            deleted_at = deleted_at
            )
        db.session.add(addQuestions)
        db.session.commit()
        return "Questions added.add Questions id={}".format(addQuestions.id_questions)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/deleteQuestions/<id_>", methods=['DELETE'])
def remove_Questions(id_):

    try:
        delQuestion=ClassQuestion.query.filter_by(id_questions=id_).first()
        db.session.delete(delQuestion)
        db.session.commit()
        return " Questions deleted."
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()

@app.route("/updateQuestions/<id_>", methods=['PUT'])
def update_Questions(id_):
    try:
        updateQuestion=ClassQuestion.query.filter_by(id_questions=(id_)).first()
        updateQuestion.quiz_id=request.args.get('quiz_id')
        updateQuestion.question=request.args.get('question')
        updateQuestion.number=request.args.get('number')
        updateQuestion.answer=request.args.get('answer')
        # updateUser.status_enabled = bool(request.args.get('statusEnabled'))
        # updateUser.created_at=request.args.get('created_at')
        # updateUser.modified_at=request.args.get('modified_at')
        # updateUser.deleted_at=request.args.get('deleted_at')


        db.session.commit()
        return "Quiz updated. Kuis= " + str(updateQuizzes.quiz_id)
    except Exception as e:
        return(str(e))
    finally:
        db.session.close()
    
# @app.route('/updateQuizPerSpecColumn/<id_>/<keyCol>', methods=['PUT'])
# def updateQuizPerSpecColumn(id_,keyCol):   

#     try:
#         UpColQu = Kuis.query.filter_by(quiz_id = (id_)).first()
        
#         if (keyCol.lower() == 'creator_id'):
#             UpColQu.creator_id = request.args.get('keyCol')
#             print(UpColQu.creator_id)
#         elif (keyCol.lower() == 'quiz_category'):
#             UpColQu.quiz_category = request.args.get('quiz_category')
#         elif (keyCol.lower() == 'title'):
#             UpColQu.title = request.args.get('keyCol')
#         elif (keyCol.lower() == 'play_times'):
#             UpColQu.play_times = request.args.get('keyCol')
#         # elif (keyCol.lower() == 'statusenabled'):
#         #     user.status_enabled = bool(request.args.get('keyCol'))
#         ## tambahin updated_on nanti hahahhh
#         else:
#             return "No column related exist"

#         db.session.commit()
#         return "Quizzes updated. quiz-d = " + str(UpColQu.quiz_id) + " updated"

#     except Exception as e:
#         return str(e)

#     finally:
#         db.session.close()
# if __name__=='__main__':
#     app.run()