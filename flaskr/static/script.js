// List of all subjects
const subjects = [
  { key: 'mathsF', display: 'Maths Foundation' },
  { key: 'mathsH', display: 'Maths Higher' },
  { key: 'englishL', display: 'English Language' },
  { key: 'englishLit', display: 'English Literature' },
  { key: 'scienceF', display: 'Combined Science Foundation' },
  { key: 'scienceH', display: 'Combined Science Higher' },
  { key: 'biologyTriple', display: 'Biology Triple Science' },
  { key: 'chemistryTriple', display: 'Chemistry Triple Science' },
  { key: 'physicsTriple', display: 'Physics Triple Science' },
  { key: 'history', display: 'History' },
  { key: 'geography', display: 'Geography' },
  { key: 'CS', display: 'Computer Science' },
  { key: 'french', display: 'French' },
  { key: 'spanish', display: 'Spanish' },
  { key: 'german', display: 'German' }
];

// Containers
const inputContainer = document.getElementById("inputContainer");
const checkboxContainer = document.getElementById("checkboxContainer");

// Input fields
subjects.forEach(subject => {
  const div = document.createElement('div');
  div.className = 'input-row';
  
  const label = document.createElement('label');
  label.textContent = subject.display + ":";
  label.htmlFor = subject.key;

  const input = document.createElement('input');
  input.type = 'number';
  input.name = subject.key;
  input.id = subject.key;
  input.placeholder = 'Enter score';

  div.appendChild(label);
  div.appendChild(input);
  inputContainer.appendChild(div);
});

// Checkboxes
subjects.forEach(subject => {
  const row = document.createElement("div");
  row.className = "checkbox-row";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "subject-checkbox";
  checkbox.id = subject.key + "-check";
  checkbox.value = subject.key;

  const label = document.createElement("label");
  label.textContent = subject.display;
  label.htmlFor = checkbox.id;

  row.appendChild(checkbox);
  row.appendChild(label);
  checkboxContainer.appendChild(row);
});
