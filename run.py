from my_app import app
from my_app import db
with app.app_context():
    db.create_all()
app.run(debug=True)

