import streamlit as st
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    body {
      text-align: center;
      background-image: url('bg1.jpg');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      font-family: sans-serif;
      padding: 30px;
      min-height: 100vh;
    }

    .section {
      display: none;
    }

    .active {
      display: block;
    }

    img.button {
      cursor: pointer;
      width: 450px;
      margin-top: 0.2px;
    }

     img.button2 {
      cursor: pointer;
      width: 350px;
      margin-top: 0.2px;
    }

    img.content {
      width: 100%;
      height: auto;
      display: block;
      margin: 0 auto 20px;
    }

     img.content2 {
      width: 50%;
      height: auto;
      display: block;
      margin: 0 auto 20px;
    }

    audio {
      display: none;
    }

    #backBtn {
      position: fixed;
      top: 20px;
      left: 20px;
      background-color: rgba(255, 255, 255, 0.7);
      border: none;
      padding: 10px 15px;
      font-size: 20px;
      font-weight: bold;
      border-radius: 50%;
      cursor: pointer;
      z-index: 9999;
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
  </style>
</head>
<body>

  <!-- Tombol Back -->
  <button onclick="goBack()" id="backBtn" style="display: none;">←</button>

  <!-- Musik dari GitHub -->
  <audio id="birthdayMusic" src="hbd-svt.mp3" preload="auto" autoplay loop></audio>

  <!-- Halaman 1 -->
  <div id="page1" class="section active">
    <img class="content" src="hbd-fix.png" alt="Happy Birthday">
    <br>
    <img class="button" src="here-fix.png" alt="Click" onclick="goToPage('page2')">
  </div>

  <!-- Halaman 2 -->
  <div id="page2" class="section">
    <img class="content" src="letter-c-fix.png" alt="Pilih">
    <br>
    <img class="button2" src="yes-fix.png" alt="Yes" onclick="goToPage('yesPage')">
    <img class="button2" src="no-fix.png" alt="No" onclick="goToPage('noPage')">
  </div>

  <!-- Halaman No -->
  <div id="noPage" class="section">
    <img class="content" src="please-fix.png" alt="Try Again">
    <br>
    <img class="button" src="ok-fix.png" alt="OK" onclick="goToPage('page1')">
  </div>

  <!-- Halaman Yes -->
  <div id="yesPage" class="section">
    <img class="content" src="cus-on-fix.png" alt="This is for u">
    <br>
    <img class="button" src="letter-o-fix.png" alt="Letter" onclick="goToPage('letterPage')">
    <br>
    <img class="content2" src="or-fix.png" alt="or">
    <br>
    <img class="button" src="sandwich-fix.png" alt="Sandwich" onclick="goToPage('sandwichPage')">
  </div>

  <!-- Halaman Letter -->
  <div id="letterPage" class="section">
    <img class="content" src="n1.jpg" alt="Letter">
    <img class="content" src="n2.jpg" alt="Letter">
    <img class="content" src="n3.jpg" alt="Letter">
  </div>

  <!-- Halaman Sandwich -->
  <div id="sandwichPage" class="section">
    <img class="content" src="s1.jpg" alt="Sandwich">
    <img class="content" src="s2.jpg" alt="Sandwich">
  </div>

  <script>
    function goToPage(pageId) {
      document.querySelectorAll('.section').forEach(sec => sec.classList.remove('active'));
      document.getElementById(pageId).classList.add('active');

      const backButton = document.getElementById('backBtn');
      const pagesWithBack = ['letterPage', 'sandwichPage'];
      backButton.style.display = pagesWithBack.includes(pageId) ? 'flex' : 'none';
    }

    function goBack() {
      goToPage('yesPage');
    }

    // Autoplay trigger
    window.addEventListener('click', function playMusicOnce() {
      document.getElementById('birthdayMusic').play();
      window.removeEventListener('click', playMusicOnce);
    });
  </script>
</body>
</html>




