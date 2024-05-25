document.getElementById('eloForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const playerARating = parseFloat(document.getElementById('playerARating').value);
    const playerBRating = parseFloat(document.getElementById('playerBRating').value);
    const outcome = parseFloat(document.getElementById('outcome').value);

    const newRatingA = calculateElo(playerARating, playerBRating, outcome);
    const newRatingB = calculateElo(playerBRating, playerARating, 1 - outcome);

    document.getElementById('newRatingA').textContent = newRatingA.toFixed(2);
    document.getElementById('newRatingB').textContent = newRatingB.toFixed(2);
});

function calculateElo(playerARating, playerBRating, outcome, k = 32) {
    const expectedScoreA = 1 / (1 + 10 ** ((playerBRating - playerARating) / 400));
    return playerARating + k * (outcome - expectedScoreA);
}
