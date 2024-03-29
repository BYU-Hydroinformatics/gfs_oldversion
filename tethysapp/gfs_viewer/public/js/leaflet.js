// creating the map
var map = L.map('map', {
    zoom: 2,
    minZoom: 1.25,
    boxZoom: true,
    maxBounds: L.latLngBounds(L.latLng(-100.0,-270.0), L.latLng(100.0, 270.0)),
    timeDimension: true,
    timeDimensionControl: true,
    timeDimensionControlOptions: {
        position: "bottomleft",
        autoPlay: true,
        loopButton: true,
        backwardButton: true,
        forwardButton: true,
        timeSliderDragUpdate: true,
        minSpeed: 1,
        maxSpeed: 6,
        speedStep: 1,
    },
    center: [20, 0],
});


// create the basemap layers (default basemap is world imagery)
var Esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}');
var Esri_Imagery_Labels = L.esri.basemapLayer('ImageryLabels');
var basemaps = {"Basemap": L.layerGroup([Esri_WorldImagery, Esri_Imagery_Labels]).addTo(map)};


// Add controls for user drawings
var drawnItems = new L.FeatureGroup();      // FeatureGroup is to store editable layers
map.addLayer(drawnItems);

var drawControl = new L.Control.Draw({
    edit: {
        featureGroup: drawnItems,
        edit: false,
    },
    draw: {
        polyline: false,
        circlemarker:false,
        circle:false,
        polygon:false,
        rectangle:false,
    },
});
map.addControl(drawControl);


// Listeners that control what happens when the user draws things on the map
map.on("draw:drawstart", function () {
    drawnItems.clearLayers();
});
map.on("draw:created", function (e) {
    var layer = e.layer;
    layer.addTo(drawnItems);
});


var legend = L.control({position:'topright'});
legend.onAdd = function(map) {
    var div = L.DomUtil.create('div', 'legend');
    url = thredds_wms + "?REQUEST=GetLegendGraphic&LAYER=" + variable + "&PALETTE=" + color + "&COLORSCALERANGE=" + boundaries[time][variable][0] + ',' + boundaries[time][variable][1];
    lookup = '<img src="' + url + '" alt="legend" style="width:100%; float:right;">';
    div.innerHTML = lookup;
    return div
};


function newLayer(variable, color) {
    url = thredds_wms;
    wmsLayer = L.tileLayer.wms(url, {
        layers: variable,
        useCache: true,
        crossOrigin: false,
        format: 'image/png',
        transparent: true,
        BGCOLOR:'0x000000',
        opacity: $("#opacity").val(),
        styles: 'boxfill/' + color,
        colorscalerange: min_bnd + ',' + max_bnd,
        });

    timedLayer = L.timeDimension.layer.wms(wmsLayer, {
        name: 'TimeSeries',
        requestTimefromCapabilities: true,
        updateTimeDimension: true,
        updateTimeDimensionMode: 'replace',
        cache: 15,
        }).addTo(map);
}


// removes old controls and adds new ones. Must be called after changeLayer
function newControls() {
    lyrControls = L.control.layers(basemaps, {'GFS Layer': timedLayer}).addTo(map);
}


function clearmap() {
    lyrControls.removeLayer(timedLayer);
    map.removeLayer(wmsLayer);
    map.removeLayer(timedLayer);
    map.removeControl(lyrControls);
}


function zoomMap(zoomLocation) {
    map.setZoom(zoomOpts[zoomLocation][2])
    map.panTo(L.latLng(zoomOpts[zoomLocation][0], zoomOpts[zoomLocation][1]));
}


function updateMap() {
    variable = $('#layers').val();
    time = 'alltimes';              //time = $("#times").val();
    color= $('#colors').val();
    clearmap();
    setParams(configs, time, variable);
    newLayer(variable, color);
    newControls();
    legend.addTo(map);
}
