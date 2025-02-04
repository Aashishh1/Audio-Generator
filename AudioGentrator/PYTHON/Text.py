import pdfplumber  # Library to extract text from PDFs
from gtts import gTTS  # Google Text-to-Speech library to convert text to speech

# Define the article text (you can replace this with text extracted from a PDF)
article = """
Iयहाँ के हम सिकंदर चाहें तो रख लें सब को अपनी जेब के अंदर अरे हमसे बचके रहना मेरे यार हारी बाज़ीको जीतना हमें आता हैं
"""

# Specify the language for text-to-speech conversion
language = 'en'  # 'en' is for English; change this to 'hi' for Hindi text

# Create a gTTS object to convert the article into speech
gtts_transformer = gTTS(text=article, lang=language)

# Save the generated speech to an MP3 file
gtts_transformer.save("wired_article.mp3")
print("WORK DONE")  # Notify the user that the task is complete
