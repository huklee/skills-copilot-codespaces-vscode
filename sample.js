// write a function to
// find all images without alternate text
// and give them a red border
function calculateDaysBetweenDates(begin, end) {
    const date1 = new Date(begin);
    const date2 = new Date(end);
    const difference = date2 - date1;
    return Math.floor(difference / (1000 * 60 * 60 * 24));
}


// write a function to
// find all images without alternate text
// and give them a red border
function highlightImagesWithoutAltText() {
    const images = document.querySelectorAll('img');
    images.forEach(image => {
        if (!image.alt) {
            image.style.border = '1px solid red';
        }
    });
}