async function uploadPDF() {
            const fileInput = document.getElementById('pdfFile');
            const file = fileInput.files[0];
            const statusDiv = document.getElementById('uploadStatus');
            
            if (!file) {
                statusDiv.innerHTML = '<div class="status error">Please select a PDF file</div>';
                return;
            }

            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                statusDiv.innerHTML = `<div class="status success">${data.status}</div>`;
            } catch (error) {
                statusDiv.innerHTML = '<div class="status error">Upload failed</div>';
            }
        }

        async function askQuestion() {
            const input = document.getElementById('questionInput');
            const question = input.value.trim();
            const chatBox = document.getElementById('chatBox');
            
            if (!question) return;

            // Display user message
            chatBox.innerHTML += `<div class="message user-message"><strong>You:</strong> ${question}</div>`;
            input.value = '';

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question })
                });
                const data = await response.json();
                
                // Display bot response
                chatBox.innerHTML += `<div class="message bot-message"><strong>🧠 Brain:</strong> ${data.answer}</div>`;
                chatBox.scrollTop = chatBox.scrollHeight;
            } catch (error) {
                chatBox.innerHTML += '<div class="message bot-message error">Error getting response</div>';
            }
        }