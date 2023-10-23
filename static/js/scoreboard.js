// static/js/scoreboard.js
const scoreboard = document.getElementById('scoreboard');
const updateButton = document.getElementById('update-button');

updateButton.addEventListener('click', async () => {
    const teamName = prompt('Enter the name of the team that scored the home runs:');
    if (!teamName) return; // Exit if canceled

    const homeRuns = parseInt(prompt(`Enter the number of home runs scored by ${teamName}:`));
    if (!homeRuns) return; // Exit if canceled

    const response = await fetch('/update_score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `team_name=${encodeURIComponent(teamName)}&home_runs=${homeRuns}`,
    });
    const data = await response.json();

    scoreboard.innerHTML = `
        <h2>Scores</h2>
        <ul>
            ${data.scores.map(score => `
                <li>${score.home_team} ${score.home_score} - ${score.away_team} ${score.away_score}</li>
            `).join('')}
        </ul>
    `;
});
