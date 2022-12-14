from db.run_sql import run_sql
import pdb
from models.exercise import Exercise
from models.record import Record
from repositories import exercise_repository, user_repository, workout_repository


def save(record):
    sql = "INSERT INTO records (exercise_id, workout_dict) VALUES (%s, %s) RETURNING *"

    values = [record.exercise.id, record.workout_dict]
    results = run_sql(sql, values)
    
    id = results[0]['id']
    record.id = id
    return  record

def select_all():
    records = []

    sql = "SELECT * FROM records"
    results = run_sql(sql)

    for row in results:
        # exercise = exercise_repository.select(row['exercise_id'])
        record = Record(row['workout_dict'], row['exercise_id'], row['id'])
        records.append(record)
    return records


def select_exercise_reps():
    records_reps = []

    sql = "SELECT workout_dict, exercise_id FROM records"
    results = run_sql(sql)

    for row in results:
        exercise = exercise_repository.select(row['exercise_id'])
        
        # records_reps.append({exercise.id: row['workout_dict']})
        records_reps.append(row)
    
    return records_reps





def delete_all():
    sql = "DELETE FROM records"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM records WHERE id = %s"
    values = [id]
    run_sql(sql, values)