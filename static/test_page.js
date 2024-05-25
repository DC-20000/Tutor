// Calculate the test duration in minutes
const numQuestions = "{{ num_questions }}";
const testDurationMinutes = parseInt(numQuestions) * 2;
// const testDurationMinutes = .1

// Start the timer
startTimer(testDurationMinutes);

function startTimer(duration) {
    let timer = duration * 60;
    const timerElement = document.getElementById('timer');

    const timerInterval = setInterval(function() {
        const minutes = Math.floor(timer / 60);
        let seconds = timer % 60;
        seconds = seconds < 10 ? '0' + seconds : seconds;

        timerElement.textContent = `Time Remaining: ${minutes}:${seconds}`;

        if (--timer < 0) {
            clearInterval(timerInterval);
            timerElement.textContent = 'Time is up!';
            // Show the popup or perform any other actions when the time is up
            showTimesUpPopup();
        }
    }, 1000);
}

function showTimesUpPopup() {
    // Create a popup or perform any other actions when the time is up
    alert('Time is up! The test has ended.');
}