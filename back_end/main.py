from flask import Flask, request, escape


app = Flask(__name__)


@app.route("/")
def practice():
    action = request.args.get("action", "play")
    return f"Let's {escape(action)}!"


def main():
    app.run()


if __name__ == "__main__":
    main()