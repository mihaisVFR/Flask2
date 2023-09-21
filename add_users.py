from app import UserModel, db


def add_users():
    with open("./users.txt", "r", encoding="utf-8") as f:
        for row_line in f:
            data = row_line.strip().split(";")
            user = UserModel(*data)
            db.session.add(user)
            db.session.commit()


db.create_all()
add_users()
