document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chatBox");

    // Fetch and display messages every 5 seconds
    function fetchMessages() {
        fetch("/get_messages")
            .then(response => response.json())
            .then(data => {
                chatBox.innerHTML = "";  // Clear existing messages
                data.forEach(message => {
                    const messageDiv = document.createElement("div");
                    messageDiv.className = "message";
                    messageDiv.innerHTML = `
                        <span class="timestamp">[${new Date(message.timestamp).toLocaleString()}]</span>
                        <span class="author">${message.author}:</span>
                        <span class="text">${message.text}</span>
                    `;
                    chatBox.appendChild(messageDiv);
                });
                chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll to the bottom
            })
            .catch(error => console.error("Error fetching messages:", error));
    }

    setInterval(fetchMessages, 5000);  // Fetch messages every 5 seconds
});
