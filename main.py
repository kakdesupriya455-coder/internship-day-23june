# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI(title="To-Do List API")

# tasks = []

# class Task(BaseModel):
#     id: int
#     title: str
#     description: str
#     completed: bool = False


# # Create Task
# @app.post("/tasks", status_code=201)
# def create_task(task: Task):
#     tasks.append(task.dict())
#     return {
#         "message": "Task created successfully",
#         "task": task
#     }


# # View All Tasks
# @app.get("/tasks", status_code=200)
# def get_tasks():
#     return tasks


# # Get Single Task
# @app.get("/tasks/{task_id}", status_code=200)
# def get_task(task_id: int):
#     for task in tasks:
#         if task["id"] == task_id:
#             return task

#     raise HTTPException(
#         status_code=404,
#         detail="Task not found"
#     )


# # Update Task
# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, updated_task: Task):

#     for index, task in enumerate(tasks):
#         if task["id"] == task_id:
#             tasks[index] = updated_task.dict()
#             return {
#                 "message": "Task updated successfully",
#                 "task": updated_task
#             }

#     raise HTTPException(
#         status_code=404,
#         detail="Task not found"
#     )


# # Mark Task Completed
# @app.patch("/tasks/{task_id}/complete")
# def complete_task(task_id: int):

#     for task in tasks:
#         if task["id"] == task_id:
#             task["completed"] = True
#             return {
#                 "message": "Task marked as completed",
#                 "task": task
#             }

#     raise HTTPException(
#         status_code=404,
#         detail="Task not found"
#     )


# # Delete Task
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):

#     for task in tasks:
#         if task["id"] == task_id:
#             tasks.remove(task)
#             return {
#                 "message": "Task deleted successfully"
#             }

#     raise HTTPException(
#         status_code=404,
#         detail="Task not found"
#     )
from fastapi import FastAPI
app = FastAPI()

@app.get("/students")
def get_all_students():
    return {"students":[
        {"id": 1, "name": "ravi", "age": 20},
        {"id": 2, "name": "priya", "age": 28},
        {"id": 3, "name": "supriya", "age": 18}
        
    ]}

@app.get("/students/{student_id}/{student_name}/{student_age}")
def get_student(student_id: int, student_name: str, student_age: int):
    return{"id": student_id, "name": "student_name", "age": "student_age"}

