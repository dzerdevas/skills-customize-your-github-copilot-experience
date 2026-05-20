const students = [
  { name: "Ava", grade: 10, score: 88 },
  { name: "Noah", grade: 9, score: 92 },
  { name: "Mia", grade: 11, score: 76 },
  { name: "Liam", grade: 10, score: 84 },
  { name: "Zoe", grade: 12, score: 95 }
];

const searchInput = document.getElementById("search");
const results = document.getElementById("results");

function renderStudents(items) {
  // TODO: Clear the results container.
  // TODO: Render each student as a .card element with name, grade, and score.
}

function filterStudents(query) {
  // TODO: Return only students whose names include the query (case-insensitive).
  return students;
}

// TODO: Render all students when the page loads.

// TODO: Add an input event listener to the search box.
// It should call filterStudents and then renderStudents.
