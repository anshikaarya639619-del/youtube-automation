import random
from datetime import datetime

print("🚀 MrBeast + Tony Stark Level Autobot Active!")

# चैनल 1 और चैनल 2 के लिए अलग-अलग महा-कैटेगरी
categories_ch1 = ["Tech Experiments", "Gadget Unboxing", "Future Tech Hacks"]
categories_ch2 = ["Extreme Challenges", "24 Hours Survival", "Mind-Blowing Secrets"]

hooks = [
    "I Spent 100 Hours Doing This...", 
    "Nobody Expected This To Happen!", 
    "This Changes Everything Forever...", 
    "I Tested The World's Craziest..."
]

def run_daily_autopilot():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\n📅 Date: {today} | Running Automated Engine...")
    
    # चैनल 1 के लिए कंटेंट
    c1 = random.choice(categories_ch1)
    h1 = random.choice(hooks)
    print(f"\n--- [CHANNEL 1: DAILY PLAN] ---")
    print(f"📌 Title: {h1} ({c1} Special)")
    print(f"📝 Description: 🔥 Welcome back! Today we crossed all limits in {c1}. Watch till the end for the shocking twist! Like & Subscribe.")
    print(f"🏷️ Tags: #MrBeast #Viral #{c1.replace(' ', '')} #Trending2026")
    
    # चैनल 2 के लिए कंटेंट
    c2 = random.choice(categories_ch2)
    h2 = random.choice(hooks)
    print(f"\n--- [CHANNEL 2: DAILY PLAN] ---")
    print(f"📌 Title: {h2} ({c2} Challenge)")
    print(f"📝 Description: ⚡ You won't believe what happened in this {c2} challenge! Don't forget to subscribe for more 24/7 epic content.")
    print(f"🏷️ Tags: #Challenge #Epic #{c2.replace(' ', '')} #TopTrending")
    print("\n==========================================")

if __name__ == "__main__":
    run_daily_autopilot()
  
