import webview

SERVER_URL = "https://accureai.com/index.html"
APP_UA = "AccureERP-Desktop/1.0 key=YOUR_SECRET"

webview.create_window("Accure Medical ERP", SERVER_URL, width=1400, height=850)
webview.start(user_agent=APP_UA)