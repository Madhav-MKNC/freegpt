#!/bin/bash

# Function to interact with the reverse ChatGPT API
reverse_chat_gpt() {
    message=$1

    # Use headless browser (Chrome) to send message and retrieve response
    response=$(google-chrome --headless --disable-gpu --no-sandbox --disable-dev-shm-usage --dump-dom "https://example.com/chatgpt" <<EOF
        var messageInput = document.getElementById('user_input');
        messageInput.value = "$message";
        var submitButton = document.getElementById('submit_button');
        submitButton.click();
        setTimeout(function() {
            var responseElement = document.getElementById('bot_response');
            console.log(responseElement.innerText);
        }, 2000);
EOF
    )

    # Extract bot response from the response variable
    bot_response=$(echo "$response" | grep -oP '(?<=innerText: ").*(?=")')

    echo "$bot_response"
}

# Main script
while true; do
    read -p "User: " user_message
    if [ "$user_message" = "exit" ]; then
        break
    fi

    response=$(reverse_chat_gpt "$user_message")
    echo "Bot: $response"
done
