from app.db.connection import engine

print("🚀 Script started")

try:
    conn = engine.connect()
    print("✅ Database connected successfully")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)

print("🏁 Script finished")