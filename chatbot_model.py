from transformers import pipeline

# Load pre-trained QA model
qa_pipeline = pipeline('question-answering')

def get_chatbot_response(query, context_data):
    # Combine the mock database responses into a single context
    context = " ".join(context_data.values())
    
    # Use the NLP model to generate an answer
    nlp_response = qa_pipeline({
        'question': query,
        'context': context
    })
    
    return nlp_response['answer']
