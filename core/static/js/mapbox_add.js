if (!mapboxgl.supported()) {
        alert('Your browser does not support Mapbox GL');
    } else {
        const map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [85, 60],
            zoom: 2,
            minZoom: 2,
        });
        const coordinatesGeocoder = function (query) {
        // Match anything which looks like
        // decimal degrees coordinate pair.
        const matches = query.match(
            /^[ ]*(?:Lat: )?(-?\d+\.?\d*)[, ]+(?:Lng: )?(-?\d+\.?\d*)[ ]*$/i
            );
            if (!matches) {
                return null;
            }

        function coordinateFeature(lng, lat) {
            return {
                center: [lng, lat],
                geometry: {
                type: 'Point',
                coordinates: [lng, lat]
                },
            place_name: 'Lat: ' + lat + ' Lng: ' + lng,
            place_type: ['coordinate'],
            properties: {},
            type: 'Feature'
        };
        }

        const coord1 = Number(matches[1]);
        const coord2 = Number(matches[2]);
        const geocodes = [];

        if (coord1 < -90 || coord1 > 90) {
        // must be lng, lat
            geocodes.push(coordinateFeature(coord1, coord2));
        }

        if (coord2 < -90 || coord2 > 90) {
        // must be lat, lng
            geocodes.push(coordinateFeature(coord2, coord1));
        }

        if (geocodes.length === 0) {
        // else could be either lng, lat or lat, lng
            geocodes.push(coordinateFeature(coord1, coord2));
            geocodes.push(coordinateFeature(coord2, coord1));
        }

        return geocodes;
        };

        // Add the control to the map.
        map.addControl(
            new MapboxGeocoder({
                accessToken: mapboxgl.accessToken,
                localGeocoder: coordinatesGeocoder,
                zoom: 4,
                placeholder: 'Your place',
                mapboxgl: mapboxgl,
                reverseGeocode: true
            })
        );
        map.addControl(new mapboxgl.GeolocateControl({
            positionOptions: {
                enableHighAccuracy: true
            },
            trackUserLocation: true,
            showUserHeading: true
        }));


        const popup = new mapboxgl.Popup({ offset: 25 });
        const el = document.createElement('div');
        el.id = 'marker';
        pop = new mapboxgl.Marker(el)
            .setLngLat([85, 60])
            .setPopup(popup)
            .addTo(map);


        map.on('click', (e) => {
            const url = new URL(window.location.href);
            url.searchParams.set('points', JSON.stringify(e.lngLat.wrap()));
            window.history.pushState({ path: url.href }, '', url.href);
            const popup = new mapboxgl.Popup({ offset: 25 });
            const el = document.createElement('div');
            el.id = 'marker';
            pop.setLngLat([Object.values(e.lngLat.wrap())[0], Object.values(e.lngLat.wrap())[1]]).addTo(map);
        });

    }