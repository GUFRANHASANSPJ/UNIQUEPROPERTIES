

// city suggestion

function fetchCitySuggestions(query) {
    const suggestionsBox = document.getElementById('citySuggestions');
    suggestionsBox.innerHTML = ''; // Clear previous suggestions

    // Hide dropdown if query is empty
    if (!query || query.length < 2) {
        suggestionsBox.style.display = 'none';
        return;
    }

    // Fetch suggestions
    fetch(`https://wft-geo-db.p.rapidapi.com/v1/geo/cities?namePrefix=${query}`, {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': "579bb90280mshd97d7764cae77c7p1937fajsn6726ac6004ae",
            'X-RapidAPI-Host': 'wft-geo-db.p.rapidapi.com'
        }
    })
        .then(response => response.json())
        .then(data => {
            const cities = data.data;

            if (cities.length > 0) {
                // Show dropdown
                suggestionsBox.style.display = 'block';

                // Add suggestions to the dropdown
                cities.forEach(city => {
                    const suggestion = document.createElement('div');
                    suggestion.textContent = `${city.name}, ${city.country}`;
                    suggestion.onclick = () => {
                        // Set input value to the selected city
                        document.getElementById('citySearch').value = city.name;
                        // Hide dropdown after selection
                        suggestionsBox.style.display = 'none';
                    };
                    suggestionsBox.appendChild(suggestion);
                });
            } else {
                // Hide dropdown if no results
                suggestionsBox.style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error fetching city suggestions:', error);
        });
        
}