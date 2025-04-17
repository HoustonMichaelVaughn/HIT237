/*
# Sources
# https://www.w3schools.com/jsref/met_element_setattribute.asp
*/

function expandText() {
    // A function for the expansion of text for cards in project_detail.
    // To avoid in-line css, we set and remove hidden attributes.
    const moreText = document.getElementById("more-text");
    const btn = document.getElementById("read-more-btn");
    const truncText = document.getElementById("summary-text");

    if (moreText.hasAttribute('hidden')) {
        truncText.setAttribute("hidden", "");;
        moreText.removeAttribute("hidden", "");
        btn.innerText = "Show less";
    } else {
        truncText.removeAttribute("hidden", "");
        moreText.setAttribute("hidden", "");
        btn.innerText = "Read more";
    }
}