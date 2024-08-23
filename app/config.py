import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://db_224077665_sit722_part_1_user:GGHCngnaTTJ96e6bQFnqYzPLkZOfZiO4@dpg-cr0pc03tq21c73cjijlg-a.oregon-postgres.render.com/db_224077665_sit722_part_1")

settings = Settings()
