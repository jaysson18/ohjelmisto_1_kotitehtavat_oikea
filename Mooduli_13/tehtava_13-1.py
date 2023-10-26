from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:number>')
def check_prime(number):
    is_prime_result = is_prime(number)
    response = {"Number": number, "isPrime": is_prime_result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
