import os
import bcrypt
import asyncpg
from dotenv import load_dotenv


load_dotenv()

credentials = {
        "user": os.getenv('user'),
        "password": os.getenv('password'),
        "database": os.getenv('database'),
        "host": "127.0.0.1",
}


async def get_user_by_email(email: str) -> str|None:
    pool = await asyncpg.create_pool(**credentials)
    async with pool.acquire() as connection:
        async with connection.transaction():
            result = await connection.fetch('SELECT * FROM users WHERE email = $1::text', email)
            return result

    
async def create_user(name: str, password: str, email: str) -> bool:
    hashed_password = bcrypt.hashpw(password=password.encode('utf-8'), salt=bcrypt.gensalt())
    pool = await asyncpg.create_pool(**credentials)
    async with pool.acquire() as connection:
        async with connection.transaction():
            unique_email = await connection.fetchrow('SELECT * FROM users WHERE email = $1::text', email)
            if not unique_email:
                await connection.execute('INSERT INTO users VALUES (DEFAULT, $1::text, $2::text, $3::text);', name, email, hashed_password.decode('utf-8'))
                is_created = await connection.fetchrow('SELECT * FROM users WHERE email = $1::text', email)
                return is_created
                