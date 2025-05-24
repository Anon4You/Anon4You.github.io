import os
import time
import threading
from telebot import TeleBot, types
import secrets
import string
import tempfile

# Configuration with your credentials
TOKEN = '7887552005:AAFa0wa2IKyVpioOpmL4mGXPWN2lXJTkLh0'
ADMIN_USER_ID = 1796323661

# Initialize bot
bot = TeleBot(TOKEN)

# File storage (in production, use a database)
file_storage = {}

def generate_unique_link():
    """Generate a unique random string for permanent download links"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(16))

def schedule_message_deletion(chat_id, message_id, delay=900):
    """Schedule a message to be deleted after 15 minutes (900 seconds)"""
    def delete_message():
        time.sleep(delay)
        try:
            bot.delete_message(chat_id, message_id)
        except Exception as e:
            print(f"Error deleting message: {e}")
    
    threading.Thread(target=delete_message, daemon=True).start()

@bot.message_handler(commands=['start'])
def handle_start(message):
    """Handle download requests"""
    args = message.text.split()
    if len(args) > 1:
        file_id = args[1]
        if file_id in file_storage:
            file_data = file_storage[file_id]
            
            try:
                # Send the file without any caption
                with open(file_data['file_path'], 'rb') as f:
                    if file_data['file_type'] == 'document':
                        sent_msg = bot.send_document(message.chat.id, f)
                    elif file_data['file_type'] == 'photo':
                        sent_msg = bot.send_photo(message.chat.id, f)
                    elif file_data['file_type'] == 'video':
                        sent_msg = bot.send_video(message.chat.id, f)
                
                # Schedule auto-deletion of the sent file after 15 minutes
                if sent_msg:
                    schedule_message_deletion(message.chat.id, sent_msg.message_id)
                    bot.reply_to(message, "✅ File sent! (This message will auto-delete in 15 minutes)")
            
            except Exception as e:
                bot.reply_to(message, f"❌ Error sending file: {str(e)}")
        else:
            bot.reply_to(message, "❌ Invalid or expired download link")
    else:
        bot.reply_to(message, "👋 Send me a file to generate a download link")

@bot.message_handler(content_types=['document', 'photo', 'video'])
def handle_file(message):
    """Handle file uploads from admin"""
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ Only admin can upload files")
        return
    
    # Get file details
    if message.document:
        file_type = 'document'
        file_id = message.document.file_id
        file_name = message.document.file_name
    elif message.photo:
        file_type = 'photo'
        file_id = message.photo[-1].file_id
        file_name = f"photo_{file_id}.jpg"
    elif message.video:
        file_type = 'video'
        file_id = message.video.file_id
        file_name = message.video.file_name or f"video_{file_id}.mp4"
    else:
        return
    
    # Generate permanent download link
    download_code = generate_unique_link()
    
    # Download and save the file
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, file_name)
    with open(file_path, 'wb') as f:
        f.write(downloaded_file)
    
    # Store file info with permanent access
    file_storage[download_code] = {
        'file_path': file_path,
        'file_name': file_name,
        'file_type': file_type,
        'upload_time': time.time()
    }
    
    # Send the permanent link to admin
    bot_username = bot.get_me().username
    download_link = f"https://t.me/{bot_username}?start={download_code}"
    
    bot.reply_to(message, f"""
📁 File stored permanently!
🔗 Download link: {download_link}

• Link will NEVER expire
• File messages auto-delete after 15 mins
• No download limits
""")

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    """Handle all other messages"""
    bot.reply_to(message, "🤖 I'm a file sharing bot. Send me a file to generate a permanent download link")

if __name__ == '__main__':
    print("Bot is running with permanent links...")
    bot.infinity_polling()
