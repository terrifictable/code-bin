
// HTML
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>

<script>
    let apiKey = '1be9a6884abd4c3ea143b59ca317c6b2';
    $.getJSON('https://ipgeolocation.abstractapi.com/v1/?api_key=' + apiKey, function(data) {
        console.log(JSON.stringify(data, null, 2)["ip_address"]);
    });
</script>
// ======
