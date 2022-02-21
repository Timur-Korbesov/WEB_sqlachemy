import datetime

from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.name = "Пользователь 1"
    user.about = "биография пользователя 1"
    user.email = "email@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    # db_sess = db_session.create_session()
    # user = db_sess.query(User).all()
    #
    # for user in db_sess.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
    #     print(user)

    user = User()
    user.name = "Пользователь 2"
    user.about = "биография пользователя 2"
    user.email = "email2@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()