const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message");

async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    // -----------------------------
    // User Message
    // -----------------------------
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.textContent = message;

    chatBox.appendChild(userDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";

    // -----------------------------
    // Typing Animation
    // -----------------------------
    const typingDiv = document.createElement("div");

    typingDiv.className = "bot-message";
    typingDiv.id = "typing";

    typingDiv.innerHTML = `
        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    chatBox.appendChild(typingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        // Remove typing animation
        const typing = document.getElementById("typing");

        if (typing) {
            typing.remove();
        }

        // Small AI thinking delay
        await new Promise(resolve => setTimeout(resolve, 700));

        // -----------------------------
        // Bot Message
        // -----------------------------
        const botDiv = document.createElement("div");

        botDiv.className = "bot-message";

        botDiv.innerHTML = `
            <strong>🤖 CampusAI</strong>
            <br><br>
            ${data.response}
        `;

        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    catch (error) {

        const typing = document.getElementById("typing");

        if (typing) {
            typing.remove();
        }

        const errorDiv = document.createElement("div");

        errorDiv.className = "bot-message";

        errorDiv.innerHTML = `
            <strong>⚠ CampusAI</strong>
            <br><br>
            Something went wrong. Please try again.
        `;

        chatBox.appendChild(errorDiv);

        chatBox.scrollTop = chatBox.scrollHeight;

    }

}

// -----------------------------
// Enter Key Support
// -----------------------------
input.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});