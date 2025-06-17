
mood = {
    "happy": ("😊", "That's great to hear! Keep smiling!"),
    "sad": ("😢", "Cheer up! Better days are ahead."),
    "angry": ("😠", "Take a deep breath. It's okay to be upset."),
    "excited": ("🤩", "Yay! Enjoy the moment!"),
    "tired": ("😴", "Get some rest. You deserve it.")
}
user = input("How are you feeling right now? ").lower()
if user in mood:
    emoji, message = mood[user]
    print(f"{emoji} {message}")
else:
    print("🙂 I'm here for you, no matter how you're feeling!")

