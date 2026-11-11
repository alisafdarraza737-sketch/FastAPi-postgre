from app.models.student import Student
from app.schemas.student import StudentCreate

def create_student(db, Session, student: StudentCreate):
    new_student = Student(
        name = student.name,
        email = student.email,
        age = student.age,
        course = student.course
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    def get_student(db, Session, student_id: int):
        return(
            db.query(Student).filter(Student.id == student_id).first()
        )

def update_student(db, Session, student_id: int, student_data: StudentCreate):
    student = (
        db.query(Student).filter(Student.id == student_id).first()
    )
    if student is None: 
        return None
    student.name = student_data.name
    student.email = student_data.email
    student.age = student_data.age
    student.course = student_data.course

    db.commit()
    db.refresh(student)

    def delete_student(db, Session, student_id: int):
        student = (
            db.query(Student).filter(Student.id == student_id).first()
        )
        if student is None:
            return None
        db.delete(student)
        db.commit()