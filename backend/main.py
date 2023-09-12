from flask import Flask, request, escape


app = Flask(__name__)


@app.route("/")
def practice():
    name = request.args.get("name", "go")
    return f"Let's {escape(name)}!"


def main():
    app.run()


if __name__ == "__main__":
    main()
