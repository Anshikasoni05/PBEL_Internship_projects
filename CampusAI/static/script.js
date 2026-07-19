const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message");

async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    // User Message
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.textContent = message;
    chatBox.appendChild(userDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";

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

        const botDiv = document.createElement("div");
        botDiv.className = "bot-message";
        botDiv.textContent = data.response;

        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    catch (error) {

        const errorDiv = document.createElement("div");
        errorDiv.className = "bot-message";
        errorDiv.textContent = "Something went wrong. Please try again.";

        chatBox.appendChild(errorDiv);

    }

}

input.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        sendMessage();

    }

});