/* Javascript for Home.html */

function openNav() {
    document.getElementById("mySidenav").style.width = "20%";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0%";
}

function displayDirections() {
    document.getElementById("instructions").style.visibility = "visible";
}

function toggleMapOutline() {
    if (map.getLayoutProperty('YellowStoneID', 'visibility') === 'visible'){
      map.setLayoutProperty('YellowStoneID', 'visibility', 'none');
    }
    else {
      map.setLayoutProperty('YellowStoneID', 'visibility', 'visible');
    }
}
function toggleTrails() {
    if (map.getLayoutProperty('YellowTrailID', 'visibility') === 'visible'){
      map.setLayoutProperty('YellowTrailID', 'visibility', 'none');
    }
    else {
      map.setLayoutProperty('YellowTrailID', 'visibility', 'visible');
    }
}
function toggleGeothermal() {
    if (map.getLayoutProperty('YellowThermalID', 'visibility') === 'visible'){
      map.setLayoutProperty('YellowThermalID', 'visibility', 'none');
    }
    else {
      map.setLayoutProperty('YellowThermalID', 'visibility', 'visible');
    }
    if (map.getLayoutProperty('YellowThermalOutlineID', 'visibility') === 'visible'){
      map.setLayoutProperty('YellowThermalOutlineID', 'visibility', 'none');
    }
    else {
      map.setLayoutProperty('YellowThermalOutlineID', 'visibility', 'visible');
    }
}
function toggleCalderna() {
    if (map.getLayoutProperty('YellowCaldernaID', 'visibility') === 'visible'){
      map.setLayoutProperty('YellowCaldernaID', 'visibility', 'none');
    }
    else {
      map.setLayoutProperty('YellowCaldernaID', 'visibility', 'visible');
    }
}

function toggleTop10() {
    if (map.getLayoutProperty('top10', 'visibility') === 'visible'){
      map.setLayoutProperty('top10', 'visibility', 'none');
    }
    else {
      map.setLayoutProperty('top10', 'visibility', 'visible');
    }
}

function testingfunction() {
  
}