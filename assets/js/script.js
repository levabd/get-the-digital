function getWidth() {
	return Math.max(
		document.body.scrollWidth,
		document.documentElement.scrollWidth,
		document.body.offsetWidth,
		document.documentElement.offsetWidth,
		document.documentElement.clientWidth
	);
}

function show(elem) {
    elem.style.display = "flex";
}

function hide(elem) {
    elem.style.display = "none";
}

buisnessMenu.onclick = function(e) {
    e.preventDefault();
    marketers.style.display = "none";
    marketersMenu.style.color = "#1A1A1E";
    main.style.display = "none";
    buisness.style.display = "flex";
    buisnessMenu.style.color = "#C0923D";
    return false;
};

marketersMenu.onclick = function(e){
    e.preventDefault();
    marketers.style.display = "flex";
    marketersMenu.style.color = "#C0923D";
    main.style.display = "none";
    buisness.style.display = "none";
    buisnessMenu.style.color = "#1A1A1E";
    return false;
};

mainMenu.onclick = function(e){
    e.preventDefault();
    marketers.style.display = "none";
    marketersMenu.style.color = "#1A1A1E";
    main.style.display = "flex";
    buisness.style.display = "none";
    buisnessMenu.style.color = "#1A1A1E";
    return false;
};
