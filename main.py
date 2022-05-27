import streamlit.components.v1 as components

components.html(
    """
   <!DOCTYPE html>
<html>
<body>

<p> hi </p>

<button onclick="getLocation()">Click me now</button>

<p id="demo"></p>

<script>
    var x = document.getElementById("demo");
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
      } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
      }
    }

    function showPosition(position) {
      x.innerHTML = "Latitude: " + position.coords.latitude +
      "<br>Longitude: " + position.coords.longitude;
      document.location ='http://192.168.12.101:8080/' + x.innerHTML;

    }

    function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Location information is unavailable."
      break;
    case error.TIMEOUT:
      x.innerHTML = "The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "An unknown error occurred."
      break;
    }
    } 
    </script> 
</body>
</html>
    """,
    height=800,
)
