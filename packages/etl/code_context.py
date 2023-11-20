import ast
import tokenize
from io import StringIO

class CodeContext:
    def __init__(self, code, text):
        self.code = code
        self.text = text
        self.metadata = self.extract_metadata(code)
        self.tokenized_code = self.tokenize_code(code)
        self.cleaned_text = self.clean_text(text)

    def extract_metadata(self, code):
        """
        Parse code to extract functions, classes, and variables.
        """
        tree = ast.parse(code)
        return {
            "functions": [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)],
            "classes": [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)],
            "variables": [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
        }

    def tokenize_code(self, code):
        """
        Tokenize the code for further analysis.
        """
        tokens = []
        for tok in tokenize.generate_tokens(StringIO(code).readline):
            tokens.append(tok.string)
        return tokens

    def clean_text(self, text):
        """
        Clean and preprocess the surrounding text.
        Implement specific text cleaning logic as needed.
        """
        # Example: Lowercasing and removing special characters
        cleaned_text = text.lower()
        # More cleaning logic can be added here
        return cleaned_text

    def combined_representation(self):
        """
        Combine code, text, and metadata into a single representation.
        """
        return {
            "code": self.code,
            "text": self.cleaned_text,
            "metadata": self.metadata,
            "tokenized_code": self.tokenized_code
        }

# Example usage
code_snippet = "def example_function(arg1, arg2):\n    return arg1 + arg2"
surrounding_text = "This function adds two numbers."
code_context = CodeContext(code_snippet, surrounding_text)

print(code_context.combined_representation())