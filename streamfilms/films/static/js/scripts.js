// Add star rating
//const rating = document.querySelector('form[name=rating]');
//
//rating.addEventListener("change", function (e) {
//    // Получаем данные из формы
//    let data = new FormData(this);
//    fetch(`${this.action}`, {
//        method: 'POST',
//        body: data
//    })
//        .then(response => alert("Рейтинг встанолено"))
//        .catch(error => alert("Помилка"))
//});
const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function (e) {
    // Получаем данные из формы
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Парсим JSON-відповідь
        } else {
            throw new Error('Помилка відправлення рейтингу');
        }
    })
    .then(data => {
        alert("Рейтинг встановлено");
        // Оновлюємо відображення рейтингу на сторінці
        const ratingSpan = document.querySelector('.editContent');
        ratingSpan.innerText = data.rating; // Припустимо, що сервер повертає новий рейтинг
    })
    .catch(error => {
        alert("Помилка: " + error.message);
    });
});
