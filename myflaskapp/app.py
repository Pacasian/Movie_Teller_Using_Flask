from flask import Flask, render_template, request, redirect, url_for
import wikipedia
import urllib.request
from gtts import gTTS
lang="en"
sumith=" "



app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home1.html")
@app.route('/button', methods=["POST"])
def gettingText():
    text=request.form['movie']
    processed_text = text.upper()
    sumith = result(processed_text)
    myObj = gTTS(text=str(sumith), lang=lang, slow=False)
    myObj.save("static/sample.mp3")
    return render_template("contact1.html", sumith=sumith,sumith_title=processed_text)


def search(movie):
    AlResult=(wikipedia.search(movie))
    for i in range(0,len(AlResult)):
        print(str(i+1)+"-> "+AlResult[i])
    UserSQ=int(input())
    print("_".join((AlResult[UserSQ-1]).split()))
    result("_".join((AlResult[UserSQ-1]).split()))


def result(movie):
    page = (wikipedia.page(movie))
    content = ((page.content)).split()
    # print(page.content)
    # print("Hai")
    plot = "Plot"
    cast = "Cast"
    pIndex = 0
    cIndex = 0
    cOccur = 0
    i = 0
    # checking where the plot and cast starting with the == or not
    for i in range(0, len(content)):
        if content[i] == plot and content[i - 1] == "==":
            pIndex = i + 2
        if content[i] == cast and content[i - 1] == "==":
            cIndex = i - 1
            cOccur = 1
    # print(" ".join(content[pIndex:cIndex]))
    if (" ".join(content[pIndex:cIndex])) == "":
        search(page)
    else:
        print("\n\n")
        musick = ((" ".join(content[pIndex:cIndex])))

    cOccur = 0
    st1=" ".join(content[pIndex:cIndex])
    len1=len(st1)
    return (st1)


@app.route('/getFileName')
def getFileName():
    return 'static/sample.mp3'


def contact():
    if "Return" in request.form:
        pass
    return render_template('home1.html')


if __name__ == '__main__':
    #app.secret_key='secret123'
    app.run(debug=True)
