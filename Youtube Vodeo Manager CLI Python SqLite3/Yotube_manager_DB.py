import sqlite3
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS youtube_videos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
     url TEXT NOT NULL,
     time TEXT NOT NULL,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )              
''')
def list_videos():
    cursor.execute("SELECT * FROM youtube_videos")
    for row in cursor.fetchall():
        print(f"{row[0]} Title :  {row[1]} | URL:{row[2]} | Durition: {row[3]} | Added on list at: {row[4]}")
    
def add_video(title, url, time):
    cursor.execute("INSERT INTO youtube_videos (title, url, time) VALUES (?, ?, ?)", (title, url, time))
    conn.commit()
    print("Video added successfully!")
def update_video(new_title, new_url, new_time, video_id):
    cursor.execute("UPDATE youtube_videos SET title = ?, url = ?, time = ? WHERE id = ?", (new_title, new_url, new_time, video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM youtube_videos WHERE id = ?", (video_id,))
    conn.commit()
    print("Video deleted successfully!")

def main():
    while True:
        print("YOUTUBE VIDEO MANAGER")
        print("**********************")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            list_videos()
        elif choice == "2":
            title = input("Enter Video Title: ")
            url = input("Enter Video URL: ")
            time = input("Enter Video Duration: ")
            add_video(title, url, time)
            

        elif choice == "3":
            video_id = input("Enter video ID: ")
            title = input("Enter Video Title: ")
            url = input("Enter Video URL: ")
            time = input("Enter Video Duration: ")
            update_video(video_id, title, url, time)

        elif choice == "4":
            video_id = input("Enter video ID To Delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

    conn.close()

if __name__ == "__main__":
    main()
