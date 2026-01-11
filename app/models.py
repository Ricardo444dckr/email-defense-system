from app import db

class Analysis(db.Model):
    __tablename__ = "analyses"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120))
    verdict = db.Column(db.String(50))
    score = db.Column(db.Integer)
    date = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Analysis {self.id} - {self.verdict}>"