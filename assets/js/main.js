const allNotes = [
  {
    id: 1,
    title: 'Title 1',
    text: 'Text 1',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 2,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 3,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 4,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 5,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 6,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 7,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 8,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 9,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 10,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
  {
    id: 11,
    title: 'Title 2',
    text: 'Text 2',
    isDeleted: false,
    solutionsNum: 0
  },
];

function creatNote(title, text) {
  const note = {
    id: getId(),
    title,
    text,
    isDeleted: false,
    solutionsNum: 0
  };

  allNotes.push(note);
}

function editNote(id, title, text, solutionsNum) {
  const note = findById(id);

  note.title = title;
  note.text = text
  note.solutionsNum = 0
}

function getId() {
  return allNotes.length + 1
}

function findById(id) {
  return allNotes.find((item) => (item.id === id));
}

function renderAllNotes() {
  const parent = document.getElementById('notes');

  parent.innerHTML = '';

  for (let i = 0; i < allNotes.length; i += 1) {
    parent.append(renderNote(allNotes[i]));
  }
}

function renderNote(note) {
  const noteElement = document.createElement('div');

  noteElement.classList.add('card');
  const innerHTML = '<h2 class="card__title"> <a href="question.html" class="card__title" id="1" onclick="matchQuestion(this.id)">' + note.title + '</a></h2> <p class="card__text">solved: ' +  note.solutionsNum + '</p>';

  noteElement.innerHTML = innerHTML;

  return noteElement;
}

renderAllNotes();

const noteForm = document.getElementById('noteForm');

noteForm.addEventListener('submit', handleSubmit);

function handleSubmit(e) {
  e.preventDefault();

  const title = document.getElementById('noteTitle').value;
  const text = document.getElementById('noteText').value;

  document.getElementById('noteTitle').value = ""
  document.getElementById('noteText').value = ""

  creatNote(title, text);

  renderAllNotes();
}

function matchQuestion(id){
  document.getElementById('question-title').innerText = allNotes[id].title
  document.getElementById('question-text').innerText = allNotes[id].text
}