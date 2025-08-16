from flask import Flask, request, jsonify
from flask_cors import CORS
from risk_model import predict_risk
from rule_engine import apply_rules
from scoring_utils import get_risk_level

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

@app.route('/api/risk-score', methods=['POST'])
def score():
    user_data = request.get_json()
    anomaly = predict_risk(user_data)
    score, reasons = apply_rules(user_data)

    if anomaly == 1:
        score = max(score, 45)  # boost score if ML flags it

    risk_level = get_risk_level(score)

    return jsonify({
        'score': score,
        'level': risk_level,
        'reasons': reasons
    })

if __name__ == '__main__':
    app.run(debug=True)
    