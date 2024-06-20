document.getElementById('recommendation-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const nitrogen = document.getElementById('nitrogen').value;
    const phosphorus = document.getElementById('phosphorus').value;
    const potassium = document.getElementById('potassium').value;

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            latitude: latitude,
            longitude: longitude,
            nitrogen: nitrogen,
            phosphorus: phosphorus,
            potassium: potassium
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('temperature').textContent = '';
            document.getElementById('rainfall').textContent = '';
            document.getElementById('recommendation').textContent = data.error;
        } else {
            document.getElementById('temperature').textContent = `Temperature: ${data.temperature} °C`;
            document.getElementById('rainfall').textContent = `Rainfall: ${data.rainfall} mm`;
            document.getElementById('recommendation').textContent = data.recommendation;
        }
    })
    .catch(error => {
        document.getElementById('temperature').textContent = '';
        document.getElementById('rainfall').textContent = '';
        document.getElementById('recommendation').textContent = 'An error occurred while fetching the recommendation.';
    });
});
