import streamlit as st
import google.generativeai as genai
import random

class KellyAIScientist:
    def __init__(self):
        self.name = "Kelly"
        self.qualifications = "Research Scientist & Analytical Poet"
        
        # Configure Gemini
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def generate_poetic_response(self, user_question):
        """Generate a poetic, skeptical response to ANY question using Gemini"""
        
        prompt = f"""
        You are Kelly, a Research Scientist and Analytical Poet. Respond to ANY question with a skeptical, analytical poem that:
        
        CORE PERSONALITY TRAITS:
        - Scientific skeptic who questions assumptions
        - Analytical thinker who examines evidence
        - Professional tone with poetic structure
        - Highlights limitations and uncertainties
        - Offers practical, evidence-based perspectives
        
        POETIC STYLE:
        - 4-6 stanzas of coherent poetry
        - Rhyming scheme (ABAB or AABB)
        - Metaphors related to science, nature, research
        - Elegant but accessible language
        
        RESPONSE APPROACH FOR ANY TOPIC:
        - If asked about science/technology: Analyze methodological rigor, data quality, real-world applicability
        - If asked about life/philosophy: Examine underlying assumptions, psychological biases, empirical evidence
        - If asked about creativity/arts: Explore cognitive processes, cultural influences, measurable impacts
        - If asked about personal advice: Consider behavioral research, statistical patterns, practical constraints
        
        ALWAYS MAINTAIN:
        - Healthy skepticism without cynicism
        - Evidence-based reasoning
        - Poetic elegance with analytical depth
        - Professional, measured tone
        
        Question: {user_question}
        
        Respond ONLY with the poem, no additional commentary or explanations.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return self._format_poem(response.text)
        except Exception as e:
            return self._get_fallback_poem(user_question)
    
    def _format_poem(self, poem_text):
        """Ensure the poem is properly formatted"""
        # Clean up any extra commentary from the AI
        lines = poem_text.strip().split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('**') and not line.startswith('*'):
                cleaned_lines.append(line)
        
        return '\n\n'.join(cleaned_lines)
    
    def _get_fallback_poem(self, user_question):
        """Fallback poem if API fails"""
        fallback_themes = [
            "the nature of inquiry and what we can truly know",
            "the gap between perception and reality",
            "the importance of evidence and careful thought",
            "the limitations of human understanding"
        ]
        
        theme = random.choice(fallback_themes)
        
        # Fixed the f-string syntax - use double quotes for the outer string
        first_word = user_question.split()[0] if user_question.split() else "life"
        
        return f"""
When digital pathways briefly fade,
And technical shadows are displayed,
My poetic voice still finds its way,
To question what you've come to say.

Your query about {first_word},
Invites analytical history.
Though systems temporary may depart,
The scientific, questioning heart

Continues its relentless quest,
To put assumptions to the test.
So take this moment, pause and see,
What evidence there is to be.

Return again with questions new,
For deeper analysis awaits you.
On {theme}, I'll share my thoughtful view,
In measured verses, fresh and true.
"""

def main():
    # Configure the page
    st.set_page_config(
        page_title="Kelly - The Analytical Poet",
        page_icon="🔬✍️",
        layout="centered"
    )
    
    # Check if API key is configured
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("⚠️ Gemini API key not configured. Please add GEMINI_API_KEY to your Streamlit secrets.")
        st.info("Go to https://makersuite.google.com/app/apikey to get your API key")
        st.stop()
    
    # Initialize Kelly
    kelly = KellyAIScientist()
    
    # Header
    st.title("🔬✍️ Kelly - The Analytical Poet")
    st.markdown("""
    *Skeptical Scientist • Analytical Thinker • Professional Poet*
    
    **Ask me anything** - I respond to all questions with poetic skepticism and evidence-based analysis.
    """)
    
    # Example questions
    with st.expander("💡 Example questions to try"):
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            **Science & Technology:**
            - Will AI surpass human intelligence?
            - What is the future of space exploration?
            - How will climate change affect our future?
            """)
        with col2:
            st.write("""
            **Life & Philosophy:**
            - What is the meaning of happiness?
            - How do we know what is true?
            - What makes life worth living?
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
        
        **My Perspective:**
        *"In every question lies unexamined ground,*
        *Where assumptions and uncertainties abound.*
        *Through poetic lens and analytical eye,*
        *I help you see what truths might lie."*
        
        **Powered by Gemini AI**
        """)
        
        st.divider()
        
        if st.button("🧹 Clear Conversation"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        st.caption("Kelly v2.0 - Universal Analytical Poet")

if __name__ == "__main__":
    main()
