from app import create_app

app = create_app()







# @celery.task()
# def add_together(a, b):
#     return a + b


if __name__ == '__main__':
    app.run(debug=True)
