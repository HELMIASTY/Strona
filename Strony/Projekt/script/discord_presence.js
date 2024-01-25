async function fetchDiscordActivity() {
    const url = 'https://api.lanyard.rest/v1/users/742840029952606289';
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching Discord activity:', error);
        return null;
    }
}

async function updateDiscordPresence() {
    const spotifyCard = document.querySelector('.spotify-card');
    if (!spotifyCard) {
        console.error('Spotify card element not found');
        return;
    }

    const jsonData = await fetchDiscordActivity();

    if (!jsonData || !jsonData.data) {
        spotifyCard.textContent = 'This user isn\'t listening to anything';
        return;
    }

    if (jsonData.data.listening_to_spotify) {
        const { spotify } = jsonData.data;
        const artistName = spotify.artist.replace(/;/g, '');
        spotifyCard.innerHTML = `
            <img src="${spotify.album_art_url}" alt="Album Art">
            <div class="spotify-track-info">
                <strong>${spotify.song}</strong>
                <small>by ${artistName}</small>
                <small>on ${spotify.album}</small>
            </div>
        `;
    } else {
        spotifyCard.textContent = 'This user isn\'t listening to anything';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateDiscordPresence();
    setInterval(updateDiscordPresence, 60000);
});