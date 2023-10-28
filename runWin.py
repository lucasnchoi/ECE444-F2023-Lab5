import os
os.system('/venv/Scripts/activate')
os.system('pip install -r requirements.txt')
os.system('set FLASK_APP=app')
#keep in mind the first os command depends on what you named your virtual environment and where it is located

from project.app import app

if __name__ == '__main__':
    #using loopback address and default flask port
    app.run(host='127.0.0.1', port=5000) #can set debug by adding debug=True

#note reusing code I made for the project alrdy, just automates opening flask app