import pdfplumber
from gtts import gTTS


article = """
Iयहाँ के हम सिकंदर चाहें तो रख लें सब को अपनी जेब के अंदर अरे हमसे बचके रहना मेरे यार हारी बाज़ीको जीतना हमें आता हैं
"""



####### ARTICLE
language = 'en'
gtts_transformer = gTTS(text=article, lang=language)
gtts_transformer.save("wired_article.mp3")
print("WORK DONE")