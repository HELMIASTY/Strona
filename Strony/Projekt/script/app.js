let webSocket = new WebSocket("wss://api.lanyard.rest/socket");
let discordID = "742840029952606289";

fetch(`https://api.lanyard.rest/v1/users/${discordID}`)
    .then((response) => response.json())
    .then((e) => {
        if (e.data["discord_user"]) {
            if (e.data.discord_status == "online") {
                document.getElementById("discord-status-highlight").innerText = "Aktywny";
                document.getElementById("discord-status-highlight").style.color = "#23a55a";
            }
            else if (e.data.discord_status == "idle") {
                document.getElementById("discord-status-highlight").innerText = "AFK(znaczy online ale jest ten status bo ładnie wygląda)";
                document.getElementById("discord-status-highlight").style.color = "#f0b232";
            }
            else if (e.data.discord_status == "dnd") {
                document.getElementById("discord-status-highlight").innerText = "Niedostępny(też online ale powiadomienia z dc nie przychodzą)";
                document.getElementById("discord-status-highlight").style.color = "#f23f43";
            }
            else if (e.data.discord_status == "offline") {
                document.getElementById("discord-status-highlight").innerText = "Offline(legit mnie nie ma na dc)";
                document.getElementById("discord-status-highlight").style.color = "#80848e";
            }

            if (e.data["listening_to_spotify"]) {
                document.getElementById("spotify-song").innerText = "Słucham " + e.data.spotify.song;
                document.getElementById("spotify-artist").innerText = " od " + e.data.spotify.artist.replaceAll(";", ",");
            }
            else {
                document.getElementById("spotify-song").innerText = "Nic nie słucahm";
                document.getElementById("spotify-artist").innerText = "";
            }

            var test = false;
            var dane;
            e.data.activities.forEach(element => {
                console.log(element);
                if ((element.id == "spotify:1") || (element.id == "custom")) {
                }
                else {
                    test = true;
                    dane = element;
                }
            });
            if (test) {
                document.getElementById("dc").innerText = "Cisne w " + dane.name;
            }
            else {
                document.getElementById("dc").innerText = "Nie gram w nic";
            }
        }

    });

webSocket.addEventListener("message", (event) => {
    let data = JSON.parse(event.data);

    if (event.data == '{"op":1,"d":{"heartbeat_interval":30000}}') {
        webSocket.send(
            JSON.stringify({
                op: 2,
                d: {
                    subscribe_to_id: discordID,
                },
            })
        );
        setInterval(() => {
            webSocket.send(
                JSON.stringify({
                    op: 3,
                    d: {
                        heartbeat_interval: 30000,
                    },
                })
            );
        }, 30000);
    }
    if (data.t == "PRESENCE_UPDATE") {
        if (data.d.spotify) {
            document.getElementById("spotify-song").innerText = "Słucham " + data.d.spotify.song;
            document.getElementById("spotify-artist").innerText = " od " + data.d.spotify.artist.replaceAll(";", ",");
        }
        else {
            document.getElementById("spotify-song").innerText = "";
            document.getElementById("spotify-artist").innerText = "";
        }
    }
});