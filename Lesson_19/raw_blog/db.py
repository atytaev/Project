from constants import DB_CONNECTION
from db_connect import DBConnect

db = DBConnect(**DB_CONNECTION)

def _add_cursor_wrapper(func):
    def wrapper (*args, **kwargs):
        with db.get_connection().cursor() as cur:
            return func(cur, *args, **kwargs)
    return wrapper

@_add_cursor_wrapper
def all_post (cur, ordering='id', asc=True):
    cur.execute("SELECT id, title, content, author, created_at"
                " FROM posts ORDER BY {} {}".format(ordering, 'ASC' if asc else 'DESC'))
    return cur.fetchall()

@_add_cursor_wrapper
def add_post(cur, title, content, author):
    cur.execute(
        "INSERT INTO posts"
        "(title, content, author)"
        "VALUES (%s, %s, %s)",
        (title, content, author)
    )

@_add_cursor_wrapper
def get_post_by_id(cur, post_id):
    cur.execute(
        "SELECT * FROM posts WHERE id = %s", (post_id,)
    )
    return cur.fetchone()

@_add_cursor_wrapper
def get_post_comments(cur, post_id):
    cur.execute(
        'SELECT id, post_id, author, content, created_at FROM comments '
        'WHERE post_id = %s',
        (post_id,)
    )
    return cur.fetchall()
@_add_cursor_wrapper
def delete_post (cur, post_id):
    cur.execute ("DELETE FROM posts WHERE id = %s", (post_id,))

@_add_cursor_wrapper
def update_post(cur, id, title, content, author):
    cur.execute("UPDATE posts SET "
                "title=%s, content=%s, author=%s "
                "WHERE id = %s ",
                (title, content, author, id)
    )



