# import pymysql

# db = pymysql.connect(
#     host="103.218.156.9", port=33760, user="Lotte", password="akemahdkwpf@Lotte", db="Lotte"
# )

from db import db

print(db.select("SELECT * from Lotte"))
