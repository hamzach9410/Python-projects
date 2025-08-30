import eventlet
eventlet.monkey_patch()

import os
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import yt_dlp

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fetch", methods=["POST"])
def fetch():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    ydl_opts = {"quiet": True, "extract_flat": True, "dump_single_json": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        videos = [{"id": e["id"], "title": e["title"], "index": e.get("playlist_index", i+1),
                   "url": f"https://www.youtube.com/watch?v={e['id']}"} 
                  for i, e in enumerate(info.get("entries", []))]
        return jsonify({"videos": videos})
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

def create_progress_hook(video_id):
    def hook(d):
        if d["status"] == "downloading":
            dl = d.get("downloaded_bytes", 0)
            total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
            pct = int(dl / total * 100) if total else 0
            print(f"[{video_id}] DL bytes: {dl} / {total} → {pct}%")
            socketio.emit("progress", {"id": video_id, "pct": pct})
        elif d["status"] == "finished":
            print(f"[{video_id}] Finished")
            socketio.emit("done", {"id": video_id})
    return hook

@app.route("/download", methods=["POST"])
def download():
    videos = request.json.get("videos", [])
    if not videos:
        return jsonify({"error": "No videos provided"}), 400

    def run_downloads():
        for v in videos:
            vid = v["id"]
            title = "".join(c for c in v["title"] if c.isalnum() or c in " .-_").strip()
            fn = f"{v['index']:02d}. {title}"
            ydl_opts = {
                "outtmpl": os.path.join(DOWNLOAD_FOLDER, f"{fn}.%(ext)s"),
                "progress_hooks": [create_progress_hook(vid)],
                "format": "bestvideo+bestaudio/best",
                "merge_output_format": "mp4",
                "quiet": True
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([v["url"]])
            except Exception as e:
                print(f"[{vid}] ERROR: {e}")
                socketio.emit("error", {"id": vid, "error": str(e)})

    socketio.start_background_task(run_downloads)
    return jsonify({"status": "Download started"})

if __name__ == "__main__":
    socketio.run(app, debug=True)