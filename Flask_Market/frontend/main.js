const API_URL = "http://127.0.0.1:5000/api/listings";

// Завантаження списку лістингів
async function loadListings() {
  const response = await fetch(API_URL);
  const data = await response.json();

  const list = document.getElementById("listings");
  list.innerHTML = "";

  data.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.title} - ${item.price} грн`;

    // Кнопка видалення
    const delBtn = document.createElement("button");
    delBtn.textContent = "Видалити";
    delBtn.onclick = () => deleteListing(item.id);
    li.appendChild(delBtn);

    // Кнопка редагування (демо)
    const editBtn = document.createElement("button");
    editBtn.textContent = "Редагувати";
    editBtn.onclick = () => updateListing(item.id, "Оновлений товар", "Оновлений опис", 999);
    li.appendChild(editBtn);

    list.appendChild(li);
  });
}

// Додати новий лістинг
async function addListing(title, description, price) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({title, description, price})
  });
  if (response.ok) {
    loadListings();
  }
}

// Видалити лістинг
async function deleteListing(id) {
  const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  if (response.ok) {
    loadListings();
  }
}

// Оновити лістинг
async function updateListing(id, title, description, price) {
  const response = await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({title, description, price})
  });
  if (response.ok) {
    loadListings();
  }
}

// Обробка форми додавання
document.getElementById("addForm").addEventListener("submit", e => {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const price = document.getElementById("price").value;
  addListing(title, description, price);
});

// Автоматичне завантаження при відкритті сторінки
window.onload = loadListings;