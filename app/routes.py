from flask import request, redirect, url_for, render_template
from app import app, db
from app.models import Task
from datetime import datetime


@app.route('/')
def index():
    taskList = Task.query.all()
    return render_template('index.html', tasks=taskList)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_task = Task(name=name, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.name = request.form['name']
        task.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', task=task)


@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get_or_404(id)
    task.is_completed = True
    task.completion_date = datetime.utcnow()
    db.session.commit()
    return redirect(url_for('index'))

