from app.security.input_security import InputSecurityAnalyzer

class RAGPipeline:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore
        self.input_security = InputSecurityAnalyzer()
