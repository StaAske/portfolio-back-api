from flask import Flask, request, jsonify, send_file, render_template
from config import ClientReq, ClientReqSchema, CVStorage, app, db
from io import BytesIO

@app.route('/')
def index():
    return "Hello there"

# VIEW FOR CLIENTS REQUEST
@app.route('/api/client-contact', methods=['GET', 'POST'])
def clientContact():
    if request.method == "POST":

        request_data = request.get_json(force=True)

        name = request_data['name']
        email = request_data['email']
        message = request_data['message']
        date_time = request_data['date_time']


        c_data = ClientReq(name, email, message, date_time)
        db.session.add(c_data)
        db.session.commit()
        return {"response": "Dear {} I recived your message.".format(name)}, 200


    elif request.method == "GET":
        all_client_req = ClientReq.query.all()
        req_schema = ClientReqSchema(many=True)

        return jsonify(req_schema.dump(all_client_req)), 200

#VIEW FOR CV LOADER
@app.route('/api/cvloader', methods=['POST', 'GET'])
def cvloader():
    if request.method == 'POST':

        file_del = CVStorage.query.first()

        if file_del != None:
            db.session.delete(file_del)
            db.session.commit()


        cv = request.files['cv']
        new_file = CVStorage(name=cv.filename, file=cv.read())
        db.session.add(new_file)
        db.session.commit()

        return {"cv_name": cv.filename}, 200

    elif request.method == 'GET':

        cv = CVStorage.query.first()

        if cv == None:
            return {"existing_cv": 'No CV loaded, click "Browse" button to load it'}, 200
        else:
            file_name = CVStorage.query.first().name
            return {"existing_cv": file_name}, 200

@app.route('/api/projects', methods=['POST', 'GET'])
def projects():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass




if __name__ == "__main__":
    app.run(debug=True)
