// Add options to dropdowns
const subjectDropdown = document.getElementById('chooseSubject');
const gradeDropdown = document.getElementById('grade');
const questionTypeDropdown = document.getElementById('typeOfQuestions');
const numberDropdown = document.getElementById('numQuestions');
const difficultyDropdown = document.getElementById('difficulty');

const subjects = ['Please Select', 'Math', 'Physics', 'Chemistry', 'Biology'];
const grades = ['Please Select', '6th', '7th', '8th', '9th', '10th', '11th', '12th'];
const questionTypes = ['Please Select', 'Multiple Choice', 'True/False', 'Short Answers', 'Long Answers'];
const numberQuestions = ['Select Number of Questions', '5', '10', '15', '20'];
const difficultyLevels = ['Please Select', 'Easy', 'Medium', 'Hard'];

// Function to add options to a dropdown
function addOptions(dropdown, options) {
    for (let option of options) {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.text = option;
        dropdown.add(optionElement);
    }
}

// Add options to dropdowns
addOptions(subjectDropdown, subjects);
addOptions(gradeDropdown, grades);
addOptions(questionTypeDropdown, questionTypes);
addOptions(numberDropdown, numberQuestions);
addOptions(difficultyDropdown, difficultyLevels);

/////////////////////////////////////////////////////////

// Get the popup and form elements
const rulesPopup = document.getElementById('rulesPopup');
const closeButton = document.querySelector('.close-button');
const startTestButton = document.getElementById('startTestButton');
const form = document.querySelector('form');

// Open the popup when the form is submitted

function validateForm() {
    const chooseSubject = document.getElementById('chooseSubject').value;
    const grade = document.getElementById('grade').value;
    const typeOfQuestions = document.getElementById('typeOfQuestions').value;
    const difficulty = document.getElementById('difficulty').value;

    if (chooseSubject === 'Please Select' || grade === 'Please Select' || typeOfQuestions === 'Please Select' || difficulty === 'Please Select') {
        showErrorPopup();
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}

form.addEventListener('submit', function(event) {
    
    event.preventDefault(); // Prevent the default form submission
    if (validateForm()) {
        // if all fields are filled then show the rulesPopup.
        rulesPopup.style.display = 'block';
    }
});

function showErrorPopup() {
    const errorPopup = document.getElementById('errorPopup');
    errorPopup.style.display = 'block';

    const closeButton = errorPopup.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
        errorPopup.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target === errorPopup) {
            errorPopup.style.display = 'none';
        }
    });
}
// Close the popup when the close button is clicked
closeButton.addEventListener('click', function() {
    rulesPopup.style.display = 'none';
});

// Close the popup when the user clicks outside the popup
window.addEventListener('click', function(event) {
    if (event.target === rulesPopup) {
        rulesPopup.style.display = 'none';
    }
});

// Handle the start test button click to submit the form
startTestButton.addEventListener('click', function() {
    // Hide the popup
    rulesPopup.style.display = 'none';

    // Submit the form
    form.submit();
});

////////////////////////////////////////////////////////////
