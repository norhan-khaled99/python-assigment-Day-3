import random
import webbrowser

websites = ['https://www.google.com', 'https://www.youtube.com', 'https://www.facebook.com']

random_website = random.choice(websites)
webbrowser.open(random_website)
