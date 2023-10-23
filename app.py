from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data (will be updated)
scores = [
    {'home_team': 'Mets', 'away_team': 'Phillies', 'home_score': 5, 'away_score': 3},
    {'home_team': 'Astros', 'away_team': 'Blue Jays', 'home_score': 2, 'away_score': 4},
]


players = [
    {'name': 'Kodai Senga', 'team': 'Mets', 'position': 'Pitcher'},
    {'name': 'Jose Altuve', 'team': 'Astros', 'position': 'Second Baseman'},
    {'name': 'Vladimir Guerrero Jr.', 'team': 'Blue Jays', 'position': 'First Baseman'},
    {'name': 'Bryce Harper', 'team': 'Phillies', 'position': 'Outfielder'},
]

@app.route('/')
def index():
    return render_template('index.html', scores=scores, players=players)

@app.route('/update_score', methods=['POST'])
def update_score():
    team_name = request.form.get('team_name')
    home_runs_scored = int(request.form.get('home_runs'))

    for score in scores:
        if score['home_team'] == team_name:
            score['home_score'] += home_runs_scored
        elif score['away_team'] == team_name:
            score['away_score'] += home_runs_scored

    return jsonify({'scores': scores})

if __name__ == '__main__':
    app.run(debug=True)
