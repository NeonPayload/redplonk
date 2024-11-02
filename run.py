import app

flask_app = app.create_app()

if __name__ == '__main__':
    flask_app.run(host="localhost", port="2000", debug=True)