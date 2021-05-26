from PIL import Image
import requests

url = "https://www.horoscope.com/images-US/signs/profile-aries.png"
im_aries = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-taurus.png"
im_taurus = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-gemini.png"
im_gemini = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-cancer.png"
im_cancer = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-leo.png"
im_leo = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-virgo.png"
im_virgo = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-libra.png"
im_libra = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-scorpio.png"
im_scorpio = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-sagittarius.png"
im_sagittarius = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-capricorn.png"
im_capricorn = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-aquarius.png"
im_aquarius = Image.open(requests.get(url, stream=True).raw)
url = "https://www.horoscope.com/images-US/signs/profile-pisces.png"
im_pisces = Image.open(requests.get(url, stream=True).raw)
image_name = []
image_name.append({'name':'Aries', 'image':im_aries, 'date': 'Mar 21-Apr 20'})
image_name.append({'name':'Taurus', 'image':im_taurus, 'date': 'Apr 21-May 20'})
image_name.append({'name':'Gemini', 'image':im_gemini, 'date': 'May 21-Jun 21'})
image_name.append({'name':'Cancer', 'image':im_cancer, 'date': 'Jun 22-Jul 22'})
image_name.append({'name':'Leo', 'image':im_leo, 'date': 'Jul 23-Aug 22'})
image_name.append({'name':'Virgo', 'image':im_virgo, 'date': 'Aug 23-Sep 22'})
image_name.append({'name':'Libra', 'image':im_libra, 'date': 'Sep 23-Oct 22'})
image_name.append({'name':'Scorpio', 'image':im_scorpio, 'date': 'Oct 23-Nov 22'})
image_name.append({'name':'Sagittarius', 'image':im_sagittarius, 'date': 'Nov 23-Dec 21'})
image_name.append({'name':'Capricorn', 'image':im_capricorn, 'date': 'Dec 22-Jan 19'})
image_name.append({'name':'Aquarius', 'image':im_aquarius, 'date': 'Jan 20-Feb 18'})
image_name.append({'name':'Pisces', 'image':im_pisces, 'date': 'Feb 19-Mar 20'})
st.write("hola")
