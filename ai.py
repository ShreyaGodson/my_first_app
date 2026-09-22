
import streamlit as st
import pandas as pd

#Page Settings

st.set_page_config(
    page_title="Smart AI Lab-Introduction to Machine Learning",
    layout="wide"
)

#sidebar

st.sidebar.title("Smart AI Lab")
st.sidebar.write(
    "Exlpore the basics of Machine Learning and see"
    "how Streamlit can be used to build interactive ML applications."
)

page=st.sidebar.radio(
    "Choose a topic",
    [
        "Start Here",
        "AI and Machine Learning",
        "How Machines Learn",
        "Types of Machine Learning",
        "Choose the Right Approach",
        "Ml in Different Industries",
        "Final Challenge"]
)


#Start here
if page=="Start Here":
    st.title("Smart AI Lab")
    st.write(""" Welcome to the  firsr session of our Machine Learning Journey,
    Imagine that you have joined the analytics team of a bank.
    The business team does not start by telling you which 
    Machine Learning algorithm to use.
    They start with business problem.
    """)
    st.divider()
    st.subheader("The bank has three questions")
    col1, col2, col3=st.columns(3)
    with col1:
        st.markdown("#### Prediction")
        st.write("""
        Can we predict whether a customer is likely
        to default on a loan?""")
    with col2:
        st.markdown("#### Discovery")
        st.write("""
        Can we discover different types of customers
        from the data?
        """)
    with col3:
        st.markdown("#### Decision")
        st.write("""
        Can a machine learning which action is better 
        based on feedback?
        """)
    st.divider()
    st.write("""
    These three questions are all related to machine learing,
    but they represent different learing problems.

    During this session we will understand the difference 
    between them and also see how Stremlit can help us 
    turn our ideas into interactive applications.
    """)
    st.info(
    "The goal of this session is understanding, not model building."
    )
    #AI and Machine Learning 
elif page =="AI and Machine Learning":
    st.title("Artificial Intelligence and Machine Learning")
    st.write("""
    Before learning machine we need to understand 
    where it fits into the larger field of artificial intelligence.
    """)
    st.subheader("Aritificial Intelligence")
    st.write("""
    Artificial intelligence is the broader field of creating 
    computer system that can perform tasks that normally
    require human intelligence .
    These tasks can include learning ,reasoning, perception,
    language understanding, planning and decision-making .
    """)
    st.subheader("Machine Learning")
    st.write("""
    Machine learning is a subset of Artificial Intelligence.
    Insted of explicitly programming every rule, we provide 
    data to a machine learning system and allow it to learn
    patterns from that data.
    Those learned patterns can then be used to make predictions,
    identify patterns or support decisions.
    """)
    st.subheader("Deep Learning")
    st.write("""
    Deep Learning is a subset of machine learning based on
    multi-layer neural networks.
    It is particularly useful when workinng with complex data
    such as images, speech, video and large amounts of text.
    """)
    st.divider()
    st.markdown("""
    **Artificial Intelligence**- A board field concerned with intelligent behaivour.
    **Machine learing**- A way of buliding AI systems that learn patterns from data.
    **Deep Learning**- A family of Machine Learning methods based on multi layer neural networks
    """)

    st.divider()
    st.subheader("Smart banking")
    st.write("""
    Consider a banking application.
    AI could refer to the overall intelligent system.
    Machine Learning could be used for:
    - predicting load default 
    - detecting unusual transactions
    - forecasting demand
    - understanding customer behaivour

    Deep Learning could be useful for:
    - analysing documents
    - speech recognition
    - understanding text
    - image-based document processing
    """)

#How Machine learn
elif page=="How Machines Learn":
    st.title("What does it mean for a machine to learn?")
    st.write("""
    In traditional programming we normally provide rules and 
    date to produce an output.
    """)
    st.subheader("Traditional programming")
    st.markdown("""
    **Rules+Data=Output**
    """)
    st.write("""
    Example:A programmer may explicitly write rules such as :
    If transaction amount is greater than particular value 
    and the transaction happens in unusual location,
    flag the transaction.
    This works well when the rules are knwon and can be 
    clearly written
    """)
    st.divider()
    st.subheader("Machine Learning")
    st.markdown("""
    **Data+ Expected Outcomes->Learning Process->Model**
    """)

    st.write("""
    In machine learning, instead of manually writing every rule,
    we provide examples to a learning system.
    The system tries to identify patterns in those examples.
    The result is a model that can be used on new data.
    """)

    st.divider()
    st.subheader("Smart Banking")
    st.write("""
    Suppose a bank has historical customer information.
    For each customer we may have:
    - income
    - age
    - credit history
    - loan amount
    - repayment behaivour

    if we also know whether these customes eventually
    defaulted, we can use those historical examples to 
    learn a reationship between the customer information
    and the outcome.
    """)

    st.write("""
    The important idea is:
    **The model learns from examples rather than being given
    every rule explicitly.**
    """)
    st.divider()
    st.subheader("One important point")
    st.warning("""
    Machine Learning does not mean that the computer
    "understands" the data like a human.
    It identifies statistical patterns in the data and
    uses those patterns to produce an output.
    """)
