from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)
print(random_number)


@app.route("/")
def title():
    return '<h1>"Guess a number between 0 and 9"</h1>' \
           '<img src="https://media0.giphy.com/media/WiXMlla4ZFR8Q/200w.webp?cid=ecf05e47jvmhmr0ckvghcfb0qfgr2pyhkfnyf75u5kzafutt&rid=200w.webp&ct=g" width=200>'


@app.route("/<number>")
def check_number(number):
    if int(number) == random_number:
        return "<h1 style='color:blue'>GOOD JOB!</h1>" \
               "<img src='https://media4.giphy.com/media/kBZBlLVlfECvOQAVno/200.webp?cid=ecf05e470ywuxtj7k2u8k8l7u1m1rrch1mdg94v1g99ouzfk&rid=200.webp&ct=g' width=200px>"
    elif int(number) < random_number:
        return "<h1 style='color:red'>TOO LOW</h1>" \
               "<img src='https://media0.giphy.com/media/W0c3xcZ3F1d0EYYb0f/200.webp?cid=ecf05e47dybmuz4ou59dzzkjoyn57j8b6432p79rnmaenrtd&rid=200.webp&ct=g' width=200px>"
    elif int(number) > random_number:
        return "<h1 style='color:green'>TOO HIGH</h1>" \
               "<img src='https://media0.giphy.com/media/W0c3xcZ3F1d0EYYb0f/200.webp?cid=ecf05e47dybmuz4ou59dzzkjoyn57j8b6432p79rnmaenrtd&rid=200.webp&ct=g' width=200px>"


if __name__ == "__main__":
    app.run(debug=True)
