from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ItemModel(db.Model):
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True}
    itemId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, itemId, name, price):
        self.itemId = itemId
        self.name = name
        self.price = price

    def returnJSON(self):
        return {"itemId": self.itemId, "name": self.name, "price": self.price}

    def finditembyid(self):
        return self.query.filter_by(itemId=self.itemId).first()

    def finditembyname(self):
        return self.query.filter_by(name=self.name).first()

    def insertItem(self):
        try:
            myobject = self.query.filter_by(name=self.name).first()
            if myobject:
                return -1
            db.session.add(self)
            db.session.commit()
            return 0
        except Exception as e:
            print(e)
            return -2

    def updateItem(self):
        try:
            myobject = self.query.filter_by(itemId=self.itemId).first()
            if myobject:
                myobject.name = self.name
                myobject.price = self.price
                db.session.commit()
                return 0
            return -1
        except Exception as e:
            print(e)
            return -2

    def deleteItem(self):
        try:
            myobject = self.query.filter_by(itemId=self.itemId).first()
            if myobject:
                db.session.delete(myobject)
                db.session.commit()
                return 0
            return -1
        except Exception as e:
            print(e)
            return -2
