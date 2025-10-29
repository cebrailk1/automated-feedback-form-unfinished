document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('feedbackForm');
  const status = document.getElementById('status');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      rating: form.rating.value,
      comments: form.comments.value.trim()
    };

    console.log('Feedback submitted:', data);
    form.reset();
    status.classList.remove('hidden');
  });
});
