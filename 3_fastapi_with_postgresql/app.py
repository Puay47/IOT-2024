from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.patch('/books/{book_id}')
async def update_book(book_id: int, book: dict, db: Session = Depends(get_db)):
    existing_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not existing_book:
        return {
        'message': 'Book not found'
    }
    if 'title' in book:
        existing_book.title = book['title']
    if 'author' in book:
        existing_book.author = book['author']
    if 'year' in book:
        existing_book.year = book['year']
    if 'is_published' in book:
        existing_book.is_published = book['is_published']
    db.commit()
    db.refresh(existing_book)
    return existing_book

@router_v1.delete('/books/{book_id}')
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    existing_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not existing_book:
        return {
        'message': 'Book not found'
    }
    db.delete(existing_book)
    db.commit()
    return {"detail": "Book deleted successfully"}

#Homework
@router_v1.get('/students')
async def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router_v1.get('/students/{student_id}')
async def get_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

@router_v1.post('/students')
async def create_student(student: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstudent = models.Student(firstname=student['firstname'], lastname=student['lastname'], std_id=student['std_id'], birth=student['birth'], gender=student['gender'])
    db.add(newstudent)
    db.commit()
    db.refresh(newstudent)
    response.status_code = 201
    return newstudent

@router_v1.patch('/students/{student_id}')
async def update_student(student_id: int, student: dict, db: Session = Depends(get_db)):
    existing_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not existing_student:
        return {
        'message': 'Student not found'
    }

    if 'firstname' in student:
        existing_student.firstname = student['firstname']
    if 'lastname' in student:
        existing_student.lastname = student['lastname']
    if 'std_id' in student:
        existing_student.std_id = student['std_id']
    if 'birth' in student:
        existing_student.birth = student['birth']
    if 'gender' in student:
        existing_student.gender = student['gender']
    
    db.commit()
    db.refresh(existing_student)
    return existing_student

@router_v1.delete('/students/{student_id}')
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    existing_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not existing_student:
        return {
        'message': 'Student not found'
    }
    
    db.delete(existing_student)
    db.commit()
    return {"detail": "Student deleted successfully"}


app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
