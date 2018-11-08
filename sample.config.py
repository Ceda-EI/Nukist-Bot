# Create a new bot by messaging @BotFather and follow the instructions
# Replace the key by the actual token recieved from BotFather
api_key = "123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Update method
# Available Modes: "polling", "webhook"
update_method = "polling"

# Webhook Config
# Check the following urls for more details
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks

webhook = {"listen": "0.0.0.0",
           "url": "https://example.com/" + api_key,
           "url_path": api_key,
           "port": 9999,
           }
