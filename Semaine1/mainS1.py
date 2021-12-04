import base64

text = """Atzx sj ujsxnje ytzy ij rjrj ufx vzj stzx fqqntsx atzx ktzwsnw
lwfyznyjrjsy ytzyjx qjx htwwjhyntsx ? Ifsx qj hfiwj ij qf uwjufwfynts iz
XUWNSY stzx fqqtsx atzx uwtutxjw ijx ijknx mjgitrfifnwjx. Ifsx hmfvzj
ijkn nq d fzwf zsj htwwjhynts i'jcjwhnhjx f wjhzujwjw. Qf nq x'fajwj vzj
ytzy hj vzn xzny jxy knsfqjrjsy zs knhmnjw uik jshtij js gfxj64. F atzx
ij ijhtijw ytzy hjqf jy fnsxn wjhtsxynyzjw qj ithzrjsy yfsy jxujwj.
Fyyjsynts xn atzx atzqje ywfsvznqqjrjsy ijhtijw qj gfxj64 vzn xzny stzx
jxujwtsx vzj atzx faje fuuqnvzj qj ijhfqflj vzn atzx f ujwrnx ij qnwj hj
rjxxflj !"""


def traduction(text):
    textTraduit = ''
    for i in text:
        if (i.islower() and i.isalpha()):
            textTraduit += chr(97 + (ord(i) - 5 - 97) % 26)
        elif (not (i.islower()) and i.isalpha()):
            textTraduit += chr(65 + (ord(i) - 5 - 65) % 26)
        else:
            textTraduit += i
    return textTraduit


if __name__ == '__main__':
    alphabet1 = 'jfxsyzniItvAaqurwheklmgdcFXUWNSY'
    alphabet2 = 'easntuidDoqVvlpmrczfghbyxASPRINT'
    print(traduction(text))

    reader = open("extractPDF.txt", "r")
    writer = open("correction.pdf", "w+b",)
    txt = reader.readlines()
    texteComplet=""
    for line in txt:
        texteComplet+=line
    pdfText=traduction(texteComplet)

    base64_bytes = pdfText.encode()
    message_bytes = base64.b64decode(base64_bytes + b'==')
    writer.write(message_bytes)
    reader.close()
    writer.close()
    pass
