from flask import Flask, render_template, request
from departments import departments, teachers
import copy

app = Flask(__name__)
all_semesters = {
1 :[
    [{'course': '', 'teacher': ''} for _ in range(6)] for _ in range(5)
],
2 : [
    [{'course': '', 'teacher': ''} for _ in range(6)] for _ in range(5)
],
3 :[
    [{'course': '', 'teacher': ''} for _ in range(6)] for _ in range(5)
],
4 : [
    [{'course': '', 'teacher': ''} for _ in range(6)] for _ in range(5)
],
}

departments_list = list(departments.keys())

all_departments ={
}

all_teachers = [[copy.deepcopy(teachers) for _ in range(6)] for _ in range(5)]
   



for department in departments_list:
    all_departments[department] = copy.deepcopy(all_semesters) #all_semesters.copy()

slots_data = all_semesters[1]
global semester
semester = 1
department = 'Computer Science'
@app.route('/')
def hello_world():
    global semester
    d = departments['Computer Science']
    corse = d[1]
    courses = [{'value': course, 'name': course}
               for course in corse]
    return render_template('html/timetable1.html',departments_list=departments_list,department=department, courses=courses, all_teachers=all_teachers, slots_data=slots_data,semester=semester)

@app.route('/add_slot', methods=['POST'])
def add_slot():
    global semester
    semester = request.form['semester']
    department = request.form['departments']
    slot = request.form['slot']
    day = request.form['day']
    course = request.form['courses']
    teacher = request.form['teachers']
    al_semesters = all_departments[department]
    d = departments[department]
    corse = d[int(semester)]
    courses = [{'value': course, 'name': course}
               for course in corse]

    all_teachers[int(slot)-1][int(day)-1].remove(teacher)

    if int(semester) == 1:
        al_semesters[1][int(slot)-1][int(day)-1] = {'course': course, 'teacher': teacher}
        slots_data = al_semesters[1]
    elif int(semester) == 2:
        al_semesters[2][int(slot)-1][int(day)-1] = {'course': course, 'teacher': teacher}
        slots_data = al_semesters[2]
    elif int(semester) == 3:
        al_semesters[3][int(slot)-1][int(day)-1] = {'course': course, 'teacher': teacher}
        slots_data = al_semesters[3]
    elif int(semester) == 4:
        al_semesters[4][int(slot)-1][int(day)-1] = {'course': course, 'teacher': teacher}
        slots_data = al_semesters[4]

    return render_template('html/timetable1.html',departments_list=departments_list,department=department, courses=courses, all_teachers=all_teachers, slots_data=slots_data,semester=semester)


@app.route('/select_semester', methods=['POST'])
def select_semester():
    global semester
    semester = int(request.form['semesters'])
    department = request.form['departments']
    d = departments[department]
    corse = d[semester]
    courses = [{'value': course, 'name': course}
               for course in corse]
    al_semesters = all_departments[department]
    if semester == 1:
        slots_data = al_semesters[1]
    elif semester == 2:
        slots_data = al_semesters[2]
    elif semester == 3:
        slots_data = al_semesters[3]
    elif semester == 4:
        slots_data = al_semesters[4]

    
    return render_template('html/timetable1.html',departments_list=departments_list,department=department, courses=courses,all_teachers=all_teachers, slots_data=slots_data, semester=semester)

    
if __name__ == '__main__':
    courses = [{'value': course, 'name': course}
               for semesters in departments
               for corses in semesters
               for course in corses]

    # teachers_list = [{'value': teacher, 'name': teacher} for teacher in teachers]
    
    app.run(debug=True)
