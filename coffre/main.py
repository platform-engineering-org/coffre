#!/usr/bin/env python

from flask import Flask, request

app = Flask(__name__)


@app.route("/api/secrets", methods=["GET"])
def secrets():
    "endpoint - /api/secrets?name=<secret name>"
    if request.method == "GET":
        name = request.args.get("name")
        return {
            "message": "This endpoint should return the secret value for "
            f"secret named: {name}"
        }


@app.route("/")
def home():
    return "Hello World"


def main() -> None:
    app.run()


if __name__ == "__main__":
    main()
