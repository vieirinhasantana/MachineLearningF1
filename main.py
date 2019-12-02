from app.main.controller.update_database import UpdateDatabase

with UpdateDatabase() as upt:
    upt.update_database()
