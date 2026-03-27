import json
import pymysql

db_connection = pymysql.connect(
    host="8.130.164.39",
    port=3306,
    user="root",
    password="root123456",
    database="memory_db",
    charset="utf8mb4"
)

cursor = db_connection.cursor()
cursor.execute("SELECT session_id, message FROM message_store ORDER BY created_at")

print("=== 对话历史（中文可读）===")
for sid, msg in cursor:
    data = json.loads(msg)
    role = "用户" if data["type"] == "human" else "AI"
    content = data["data"]["content"]
    print(f"[{role}] {content}")