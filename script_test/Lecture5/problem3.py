import sqlite3 

def retrieve_article(sql_connection, article_name):
    cursor = sql_connection.cursor()
    result = cursor.execute(f"SELECT name,article FROM articles WHERE name=?",[article_name])
    return result.fetchone()

def retrieve_names(sql_connection):
    cursor = sql_connection.cursor()
    select_string = "SELECT name FROM articles"
    result = cursor.execute(select_string)
    return [res[0] for res in result.fetchall()]

if __name__ == "__main__":
    print("Opening database: site.db")

    conn = sqlite3.connect("site.db")
    print("Database connected")

    print("----Article Names----")
    for name in retrieve_names(conn):
        print(f"* {name}")
    article_name = input("\nArticle Name: ")
    print(f"Retrieving {article_name}\n")
    name, article = retrieve_article(conn, article_name)
    if article:
        print(f"*****{name}*****")
        print(article)
    else:
        print(f"{article_name} does not exist")