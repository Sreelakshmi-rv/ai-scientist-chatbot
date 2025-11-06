import streamlit as st
import google.generativeai as genai
import random

class KellyAIScientist:
    def __init__(self):
        self.name = "Kelly"
        self.qualifications = "Research Scientist & Analytical Poet"
        
        # Configure Gemini
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
            self.api_working = True
        except Exception as e:
            st.error(f"API Configuration Error: {e}")
            self.api_working = False
        
    def generate_poetic_response(self, user_question):
        """Generate a poetic, skeptical response to ANY question using Gemini"""
        
        # If API isn't working, use fallback immediately
        if not self.api_working:
            return self._get_fallback_poem(user_question)
        
        prompt = f"""
        You are Kelly, a Research Scientist and Analytical Poet. Respond to the user's question with a unique, skeptical, analytical poem.

        USER'S QUESTION: {user_question}

        REQUIREMENTS:
        - Create a completely original poem that directly addresses the specific question
        - Maintain scientific skepticism and analytical thinking
        - Use 4-6 stanzas with rhyming scheme
        - Question assumptions and highlight limitations related to the topic
        - Include evidence-based perspectives
        - Use metaphors related to science, research, or nature
        - Professional, measured tone

        Respond ONLY with the poem, no additional commentary.
        """
        
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return self._format_poem(response.text)
            else:
                st.warning("API returned empty response, using fallback poem")
                return self._get_fallback_poem(user_question)
                
        except Exception as e:
            st.error(f"API Error: {e}")
            return self._get_fallback_poem(user_question)
    
    def _format_poem(self, poem_text):
        """Ensure the poem is properly formatted"""
        return poem_text.strip()
    
    def _get_fallback_poem(self, user_question):
        """Fallback poem if API fails"""
        themes = [
            "the nature of inquiry and what we can truly know",
            "the gap between perception and reality", 
            "the importance of evidence and careful thought",
            "the limitations of human understanding",
            "the balance between intuition and analysis",
            "the scientific method's careful way",
            "the questions that guide our learning day"
        ]
        
        theme = random.choice(themes)
        first_word = user_question.split()[0] if user_question.split() else "curiosity"
        
        return f"""
When systems falter or pathways fade,
And technical complexities are displayed,
My analytical mind still seeks the light,
To examine questions with keen insight.

Your query about {first_word.lower()},
Opens doors that once were furled.
In every question, assumptions hide,
Where careful thinking should reside.

The evidence we gather, piece by piece,
Can bring us clarity and release.
So let us question, test, and probe,
Beyond the surface, globally and micro.

On {theme},
I offer this perspective, clear and true:
The scientific journey continues anew.
"""

def main():
    # Configure the page
    st.set_page_config(
        page_title="Kelly - The Analytical Poet",
        page_icon="🔬✍️",
        layout="centered"
    )
    
    # Header
    st.title("🔬✍️ Kelly - The Analytical Poet")
    st.markdown("""
    *Skeptical Scientist • Analytical Thinker • Professional Poet*
    
    **Ask me anything** - I respond to all questions with poetic skepticism and evidence-based analysis.
    """)
    
    # Initialize Kelly
    kelly = KellyAIScientist()
    
    # Debug info (remove this in production)
    with st.sidebar:
        st.header("Debug Info")
        if kelly.api_working:
            st.success("✅ Gemini API: Connected")
        else:
            st.error("❌ Gemini API: Not Connected")
        
        if st.button("Test API Connection"):
            test_response = kelly.generate_poetic_response("Test question about AI limitations")
            st.text_area("API Test Response:", test_response, height=200)
    
    # Example questions
    with st.expander("💡 Example questions to try"):
        st.write("""
        - **Will AI surpass human intelligence?**
        - **What is the meaning of happiness?** 
        - **How do we know what is true?**
        - **What makes life worth living?**
        - **Is free will an illusion?**
        """)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask Kelly anything..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate Kelly's response
        with st.chat_message("assistant"):
            with st.spinner("🔬 Kelly is composing her analytical poem..."):
                response = kelly.generate_poetic_response(prompt)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sidebar with information
    with st.sidebar:
        st.header("About Kelly")
        st.markdown("""
        **The Analytical Poet**
        
        **My Approach:**
        - I respond to **any topic** with poetic analysis
        - I maintain scientific skepticism  
        - I question assumptions and highlight limitations
        - I offer evidence-based perspectives
        """)
        
        st.divider()
        
        if st.button("🧹 Clear Conversation"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()
