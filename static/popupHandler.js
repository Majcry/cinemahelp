document.querySelectorAll(".moviePreview").forEach(preview => {
    preview.addEventListener("click", async () => {
        const movieId = preview.dataset.movieId;

        const response = await fetch(`/movie/${movieId}`)

        const movie = await response.json();

        console.log(movieId);

        document.getElementById("popupPoster").src = "https://image.tmdb.org/t/p/w342" + movie.poster_path;

        document.getElementById("popupTitle").innerText = movie.title;
        document.getElementById("popupOverview").innerText = movie.overview;
        document.getElementById("popupReleaseDate").innerText = movie.release_date;
        document.getElementById("popupGenres").innerText = movie.genres.map(genre => genre.name).join(", ");
        document.getElementById("popupRating").innerText = movie.vote_average;

        document.getElementById("movieDetails").style.display = "block";
    });
});

document.getElementById("closePopup").addEventListener("click", () => {
    document.getElementById("movieDetails").style.display = "none";
});


function closePopup() {
    document.getElementById("movieDetails").style.display = "none";
}