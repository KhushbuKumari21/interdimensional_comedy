document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('comedyForm');
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        resultDiv.innerHTML = '';
        loadingDiv.classList.remove('hidden');

        const style = document.getElementById('style').value.trim();
        const gender = document.getElementById('gender').value;
        const dimension = document.getElementById('dimension').value;

        if (!style || !gender || !dimension) {
            loadingDiv.classList.add('hidden');
            resultDiv.innerHTML = `<div class="error">All fields are required.</div>`;
            return;
        }

        try {
            const response = await fetch('/api/generate_comedy', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ style, gender, dimension }),
            });

            const data = await response.json();
            loadingDiv.classList.add('hidden');

            if (response.ok) {
                resultDiv.innerHTML = `
                    <div class="success">
                        <h2>Your Comedy Show:</h2>
                        <p>${data.comedy_show}</p>
                    </div>
                `;
            } else {
                resultDiv.innerHTML = `<div class="error">${data.error}</div>`;
            }
        } catch (error) {
            loadingDiv.classList.add('hidden');
            resultDiv.innerHTML = `<div class="error">An unexpected error occurred. Please try again later.</div>`;
            console.error('Error:', error);
        }
    });
});
