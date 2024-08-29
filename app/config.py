import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://db_224077665_sit722_part1_user:64qF9PZo6eSe4Y7S9y63dzTvNKHI5oK7@dpg-cr40ub08fa8c73debg40-a.oregon-postgres.render.com/db_224077665_sit722_part1")

settings = Settings()
