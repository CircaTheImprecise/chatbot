<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dialogflow Messenger with Audio</title>
</head>
<body>

<!-- Dialogflow Messenger iframe -->
<iframe
  allow="microphone;"
  width="350"
  height="430"
  src="https://console.dialogflow.com/api-client/demo/embedded/6746f9a3-8a06-4470-bec7-558815732850">
</iframe>

<!-- Audio player -->
<audio id="audioPlayer" controls style="display: none;">
  <source src="your-audio-file.mp3" type="audio/mp3">
  Your browser does not support the audio tag.
</audio>

<!-- Dialogflow Messenger script -->
<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    document.addEventListener("DFMChatMessage", function(event) {
      var message = event.detail;
      if (message.payload === "play_audio") {
        playAudio();
      }
    });
  });

  function playAudio() {
    var audioPlayer = document.getElementById("audioPlayer");
    audioPlayer.play();
  }
</script>

</body>
</html>
