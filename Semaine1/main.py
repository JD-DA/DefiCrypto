text = """Atzx sj ujsxnje ytzy ij rjrj ufx vzj stzx fqqntsx atzx ktzwsnw
lwfyznyjrjsy ytzyjx qjx htwwjhyntsx ? Ifsx qj hfiwj ij qf uwjufwfynts iz
XUWNSY stzx fqqtsx atzx uwtutxjw ijx ijknx mjgitrfifnwjx. Ifsx hmfvzj
ijkn nq d fzwf zsj htwwjhynts i'jcjwhnhjx f wjhzujwjw. Qf nq x'fajwj vzj
ytzy hj vzn xzny jxy knsfqjrjsy zs knhmnjw uik jshtij js gfxj64. F atzx
ij ijhtijw ytzy hjqf jy fnsxn wjhtsxynyzjw qj ithzrjsy yfsy jxujwj.
Fyyjsynts xn atzx atzqje ywfsvznqqjrjsy ijhtijw qj gfxj64 vzn xzny stzx
jxujwtsx vzj atzx faje fuuqnvzj qj ijhfqflj vzn atzx f ujwrnx ij qnwj hj
rjxxflj !"""
if __name__ == '__main__':
    alphabet1 = 'jfxsyzniItvAaqurwheklmgdcFXUWNSY'
    alphabet2 = 'easntuidDoqVvlpmrczfghbyxASPRINT'
    print(text.translate(str.maketrans(alphabet1, alphabet2)))
    print(ord('e') - ord('j'))
    for i in range(len(alphabet1)):
        print(ord(alphabet1[i]) - ord(alphabet2[i]))
    textTraduit = ''
    for i in text:
        textTraduit += chr(ord(i) - 5)
    print(textTraduit)

    reader = open("message2.txt", "r")
    writer = open("correction.pdf", "w")
    txt = reader.readlines()
    for line in txt:
        for i in range(len(line)-2):
            txt[i] = chr(ord(line[i]) - 5)
        writer.write("".join(line))

    reader.close()
    writer.close()
    pass
