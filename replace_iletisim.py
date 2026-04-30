import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the iletisim section and the following map section
pattern = r'<section id="iletisim".*?</section><section class="section mcb-section" style="padding-bottom:100px;">.*?</section>'

new_section = """<section id="iletisim" class="section mcb-section" style="padding-top:100px;padding-bottom:100px;background-color:#ffffff">
<div class="section_wrapper mfn-wrapper-for-wraps mcb-section-inner">
<div class="wrap mcb-wrap one valign-top clearfix">
<div class="mcb-wrap-inner" style="display: flex; flex-wrap: wrap; box-shadow: 0 0 20px rgba(0,0,0,0.1);">
<div style="flex: 1 1 33.33%; background: #161922; color: #fff; padding: 40px; display: flex; flex-direction: column; justify-content: center;">
<h3 style="color: #fff; margin-bottom: 20px;">Bize Ulaşın</h3>
<form action="#" method="post" class="contact-form">
<input type="text" name="name" placeholder="Adınız Soyadınız" style="width: 100%; margin-bottom: 15px; background: rgba(255,255,255,0.1); border: none; color: #fff; padding: 10px;">
<input type="email" name="email" placeholder="E-Posta" style="width: 100%; margin-bottom: 15px; background: rgba(255,255,255,0.1); border: none; color: #fff; padding: 10px;">
<input type="tel" name="phone" placeholder="Telefon" style="width: 100%; margin-bottom: 15px; background: rgba(255,255,255,0.1); border: none; color: #fff; padding: 10px;">
<textarea name="message" placeholder="Mesajınız" rows="4" style="width: 100%; margin-bottom: 15px; background: rgba(255,255,255,0.1); border: none; color: #fff; padding: 10px;"></textarea>
<button type="submit" class="button button_primary" style="background: #ffffff; color: #000; width: 100%;">Gönder</button>
</form>
</div>
<div style="flex: 1 1 66.66%; min-height: 450px;">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12051.87321558503!2d28.6291667!3d40.9833333!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14caa1177696478d%3A0x6b4f70b4d45c58a5!2sKavakl%C4%B1%2C%2034520%20Beylikduzu%2F%C4%B0stanbul!5e0!3m2!1str!2str!4v1714460000000!5m2!1str!2str" width="100%" height="100%" style="border:0; display:block; min-height: 450px;" allowfullscreen="" loading="lazy"></iframe>
</div>
</div>
</div>
</div>
</section>"""

# Replace and write back
new_content, count = re.subn(pattern, new_section, content, flags=re.DOTALL)
if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced.")
else:
    print("Pattern not found.")
