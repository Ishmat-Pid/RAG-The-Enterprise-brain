async function handleUpload() {
    const fileInput = document.getElementById('pdfUpload');
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);
    
    addMessage('System', `Initializing Brain with ${file.name}...`, 'ai-msg');

    try {
        const res = await fetch('/upload', { method: 'POST', body: formData });
        const data = await res.json();
        addMessage('System', data.status || data.error, 'ai-msg');
    } catch (error) {
        addMessage('System', "Upload failed. Check server connection.", 'ai-msg');
    }
}

async function handleChat() {
    const input = document.getElementById('userQuery');
    const question = input.value.trim();
    if (!question) return;

    addMessage('You', question, 'user-msg');
    input.value = '';

    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });
        const data = await res.json();
        addMessage('AI', data.answer, 'ai-msg');
    } catch (error) {
        addMessage('AI', "Error: AI is currently offline.", 'ai-msg');
    }
}

function addMessage(sender, text, type) {
    const window = document.getElementById('chat-window');
    const msgDiv = document.createElement('div');
    msgDiv.className = `msg ${type}`;
    msgDiv.innerHTML = `<strong>${sender}:</strong><br>${text.replace(/\n/g, '<br>')}`;
    window.appendChild(msgDiv);
    window.scrollTop = window.scrollHeight;
}

// Allow pressing "Enter" to send
document.getElementById('userQuery')?.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleChat();
});