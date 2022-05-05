$('.addmem').on('click', function () {
        var url = new URLSearchParams(window.location.search);
        params = {};
        url.forEach((p, key) => {
                params[key] = p;
            });
        if (Object.keys(params).length == 0) {
            alert('Pick your place on a map');
            return false
        };
        });