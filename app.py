import streamlit as st
import requests

api_url=st.secrets["api_url"]


st.title("AI Content Creator")

st.write("Generate Blogs, linkedin post, Captions, Email and more...")
topic=st.text_input("Enter your Topic.")

technology=st.selectbox("Select Technology",["python","React","Java","MERN","NodeJs","AI","GenAI"])
content_type=st.selectbox("select type of content",["Linkedin post","Blogs","Email","Youtube Description","Instagram content","Twitter post"])

tone=st.selectbox("Tone",
    [
        "Professional",
        "Formal",
        "simple",
        "Friendly",
        "Casual",
    ])
generate= st.button("Generate Content")

if generate:
    if topic == "":
        st.warning("please enter topic")
    else:
        with st.spinner("Generating Content..."):
            response=requests.post(f"{api_url}/get_content",
                            params={
                                "topic":topic,
                                "technology":technology,
                                "content_type":content_type,
                                "tone":tone
                            }
                        )
            st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.json()["content"])

            st.success("Content Generated Successfully")

            st.subheader("Generated Content")

            


