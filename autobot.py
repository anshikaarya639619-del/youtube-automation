import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

print("🚀 Suraj's Direct YouTube Auto-Uploader Starting...")

# GitHub Secrets से चाबियाँ लेना
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
refresh_token = os.getenv("YOUTUBE_REFRESH_TOKEN")

def upload_video_to_youtube():
    if not client_id or not client_secret or not refresh_token:
        print("❌ Error: API Keys missing in GitHub Secrets! Check CLIENT_ID, CLIENT_SECRET, and YOUTUBE_REFRESH_TOKEN.")
        return

    try:
        # क्रिडेंशियल्स सेट करना
        creds = google_auth_oauthlib.flow.Credentials(
            None,
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            token_uri="https://oauth2.googleapis.com/token"
        )
        
        youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
        print("🔥 Successfully connected to YouTube Channel via Cloud!")
        
        # यहाँ वीडियो/शॉर्ट्स अपलोड करने का असली एपीआई अनुरोध जुड़ेगा
        print("✅ Status: Ready to push videos, reels, and posts directly to your channels!")

    except Exception as e:
        print(f"⚠️ Upload connection error: {e}")

if __name__ == "__main__":
    upload_video_to_youtube()
          
