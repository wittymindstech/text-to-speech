const backendURL = "https://YOUR_BACKEND_URL"; // Replace

async function loadVoices() {
    const res = await fetch(backendURL + "/voices");
    const data = await res.json();
    const dropdown = document.getElementById("voiceList");

    data.voices.forEach(v => {
        const opt = document.createElement("option");
        opt.value = v.id;
        opt.innerText = `${v.name} (${v.lang})`;
        dropdown.appendChild(opt);
    });
}

async function generateAudio() {
    const text = document.getElementById("text").value;
    const language = document.getElementById("language").value;
    const voice_id = document.getElementById("voiceList").value;

    const res = await fetch(backendURL + "/tts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, language, voice_id })
    });

    const data = await res.json();

    if (data.download_url) {
        document.getElementById("download-section").innerHTML =
            `<a href="${backendURL}${data.download_url}" download>Download Audio</a>`;
    }
}

loadVoices();
